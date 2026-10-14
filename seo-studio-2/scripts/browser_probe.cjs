#!/usr/bin/env node
'use strict';
// Optional Playwright adapter. Inputs are data; no supplied executable code is evaluated.
const fs = require('node:fs');
const crypto = require('node:crypto');
const sha256 = text => crypto.createHash('sha256').update(text).digest('hex');

async function probe(manifest) {
  const base = new URL(manifest.base_url);
  if (!['http:', 'https:'].includes(base.protocol) || base.username || base.password ||
      !['localhost', '127.0.0.1', '[::1]'].includes(base.hostname)) {
    throw new Error('Only explicitly scoped localhost HTTP(S) URLs without credentials are supported');
  }
  if (manifest.mobile !== true || !Array.isArray(manifest.pages) || !manifest.pages.length) {
    throw new Error('Manifest requires mobile:true and a nonempty pages array');
  }
  for (const record of manifest.pages) {
    if (!record || typeof record.route !== 'string' || typeof record.essential_text !== 'string' ||
        !record.essential_text.trim() || !Array.isArray(record.essential_links) || !record.essential_links.length ||
        record.essential_links.some(link => typeof link !== 'string' || new URL(link, base).origin !== base.origin) ||
        new URL(record.route, base).origin !== base.origin) {
      throw new Error('Each route requires essential text and internal essential links');
    }
  }
  const { chromium } = require('playwright');
  const browser = await chromium.launch({ headless: true });
  const output = { status: 'PASS', target: base.href, evidence_id: null, runs: [] };
  try {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 },
      isMobile: true, hasTouch: true, deviceScaleFactor: 1 });
    // Fail closed for redirects, remote requests, popups and third-party subresources.
    await context.route('**/*', route => {
      try {
        const url = new URL(route.request().url());
        return url.origin === base.origin ? route.continue() : route.abort('blockedbyclient');
      } catch { return route.abort('blockedbyclient'); }
    });
    for (const spec of manifest.pages) {
      const page = await context.newPage();
      const failures = [];
      page.on('pageerror', error => failures.push(String(error.message)));
      page.on('console', message => { if (message.type() === 'error') failures.push(message.text()); });
      page.on('popup', popup => { failures.push('Unexpected popup'); popup.close().catch(() => {}); });
      const run = { tool: 'Playwright Chromium', version: browser.version(), route: spec.route,
        requested_url: new URL(spec.route, base).href, final_url: null,
        profile: 'mobile 390x844, touch, deviceScaleFactor=1', observed_at: new Date().toISOString(),
        checks: { rendered_dom: false, navigation: false, console_errors: false,
          raw_content_present: false, raw_links_present: false }, errors: failures };
      try {
        const response = await page.goto(new URL(spec.route, base).href, { waitUntil: 'networkidle', timeout: 15000 });
        if (!response || response.status() !== 200) throw new Error('Page HTTP status must be 200');
        if (new URL(page.url()).origin !== base.origin) throw new Error('Navigation left scoped origin');
        run.final_url = page.url();
        const raw = await response.text();
        const expectedLinks = spec.essential_links.map(link => new URL(link, base).href);
        const observed = await page.evaluate(({ html, expectedText, expectedLinks, documentUrl }) => {
          const normalize = text => text.replace(/\s+/g, ' ').trim();
          const source = new DOMParser().parseFromString(html, 'text/html');
          source.querySelectorAll('script,style,template').forEach(node => node.remove());
          const rawLinks = Array.from(source.querySelectorAll('a[href]')).map(node => new URL(node.getAttribute('href'), documentUrl).href);
          const renderedLinks = Array.from(document.querySelectorAll('a[href]')).map(node => node.href);
          const rendered = document.querySelector('main') || document.body;
          return { raw_content_present: normalize(source.body.textContent || '').includes(normalize(expectedText)),
            raw_links_present: expectedLinks.every(link => rawLinks.includes(link)),
            rendered_dom: normalize(rendered.innerText || '').includes(normalize(expectedText)) &&
              expectedLinks.every(link => renderedLinks.includes(link)) };
        }, { html: raw, expectedText: spec.essential_text, expectedLinks, documentUrl: page.url() });
        Object.assign(run.checks, observed);
        run.raw_html_sha256 = sha256(raw);
        run.rendered_html_sha256 = sha256(await page.content());
        const navigationTarget = expectedLinks[0];
        const anchor = page.locator('a[href]').filter({ hasText: '' });
        let clicked = false;
        for (let i = 0; i < await anchor.count(); i++) {
          const item = anchor.nth(i);
          if (await item.evaluate(node => node.href) === navigationTarget) {
            await item.click({ timeout: 10000 });
            await page.waitForURL(navigationTarget, { timeout: 10000 });
            clicked = true; break;
          }
        }
        run.checks.navigation = clicked && page.url() === navigationTarget;
        await page.waitForLoadState('networkidle', { timeout: 10000 });
      } catch (error) { failures.push(String(error.message)); }
      run.checks.console_errors = failures.length > 0;
      if (!run.checks.rendered_dom || !run.checks.navigation || run.checks.console_errors ||
          !run.checks.raw_content_present || !run.checks.raw_links_present) output.status = 'FAIL';
      output.runs.push(run);
      await page.close();
    }
    await context.close();
  } finally { await browser.close(); }
  return output;
}

async function main() {
  const [inputPath, outputPath, ...extras] = process.argv.slice(2);
  if (!inputPath || !outputPath || extras.length) throw new Error('Usage: node browser_probe.cjs manifest.json output.json');
  // Refuse overwrites before launching a browser.
  const fd = fs.openSync(outputPath, 'wx');
  let output;
  try { output = await probe(JSON.parse(fs.readFileSync(inputPath, 'utf8'))); }
  catch (error) { output = { status: 'NOT_RUN', evidence_id: null, runs: [], error: String(error.message) }; }
  try { fs.writeFileSync(fd, JSON.stringify(output, null, 2) + '\n', 'utf8'); }
  finally { fs.closeSync(fd); }
  process.stdout.write(JSON.stringify({ status: output.status, routes: output.runs.length, output: outputPath }) + '\n');
  process.exitCode = output.status === 'PASS' ? 0 : 1;
}

if (require.main === module) main().catch(error => { process.stderr.write(error.message + '\n'); process.exitCode = 2; });
module.exports = { probe };
