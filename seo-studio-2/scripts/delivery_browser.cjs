// Browser delivery checks. Requires installed free Playwright; no automatic download.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const hash = b => crypto.createHash('sha256').update(b).digest('hex');
async function main() {
  const project = path.resolve(process.argv[2] || '');
  const target = new URL(process.argv[3]);
  const allowHosts = process.argv.slice(4);
  if (!['127.0.0.1','localhost','[::1]'].includes(target.hostname))
    throw new Error('Local target required');
  const plan = JSON.parse(fs.readFileSync(path.join(project,'EXECUTION.json'),'utf8'));
  const state = JSON.parse(fs.readFileSync(path.join(project,'state.json'),'utf8'));
  if (plan.run_id !== state.run_id || !plan.build_receipt) throw new Error('Build/context absent');
  const { chromium } = require('playwright');
  const browser = await chromium.launch({headless:true});
  const root = path.join(project,'EXECUTION-browser');
  if (!fs.existsSync(root)) fs.mkdirSync(root);
  if (fs.lstatSync(root).isSymbolicLink()) throw new Error('Symbolic output forbidden');
  const report = {run_id:state.run_id, tool:'Playwright', version:require('playwright/package.json').version,
    observed_at:new Date().toISOString(), build_sha256:hash(Buffer.from(JSON.stringify(plan.build_receipt))),
    site_sha256:plan.build_receipt.site_sha256, status:'PASS', errors:[], runs:[]};
  try {
    for (const [profile,viewport] of [['desktop',{width:1440,height:900}],['mobile',{width:390,height:844}]]) {
      const context = await browser.newContext({viewport});
      await context.route('**/*', route => {
        const req = route.request(), u = new URL(req.url());
        if (!['GET','HEAD'].includes(req.method()) ||
            (u.origin !== target.origin && !allowHosts.includes(u.hostname) && !['data:','blob:'].includes(u.protocol)))
          return route.abort();
        return route.continue();
      });
      for (let i=0;i<plan.pages.length;i++) {
        const binding=plan.pages[i], intended=state.pages.find(x=>x.id===binding.id);
        if (!intended) throw new Error('Unplanned browser page');
        const page=await context.newPage(), errors=[];
        page.on('pageerror',error=>errors.push(String(error.message)));
        const url=new URL(intended.path,target).href;
        const run={page_id:binding.id, profile, requested_url:url, checks:{}, errors};
        try {
          const response=await page.goto(url,{waitUntil:'networkidle',timeout:20000});
          if (!response || response.status()!==200 || page.url()!==url) throw new Error('Page HTTP/destination mismatch');
          run.html_sha256=hash(await response.body());
          run.final_url=page.url();
          run.checks.rendered=await page.locator('h1').isVisible();
          run.checks.images=await page.locator('img').evaluateAll(images=>images.every(x=>x.complete&&x.naturalWidth>0));
          run.checks.hero_artwork=await page.locator('[data-hero]').evaluateAll((heroes,required)=>{
            if(required&&heroes.length===0)return false;
            return heroes.every(hero=>{
              const img=hero.querySelector('img[data-hero-artwork]');
              if(!img||!img.complete||img.naturalWidth<=0||img.naturalHeight<=0)return false;
              const bounds=hero.getBoundingClientRect(), image=img.getBoundingClientRect(), style=getComputedStyle(img);
              return bounds.width>0&&bounds.height>0&&Math.abs(img.naturalWidth/img.naturalHeight-16/9)<0.02
                &&image.left<=bounds.left+2&&image.top<=bounds.top+2
                &&image.right>=bounds.right-2&&image.bottom>=bounds.bottom-2
                &&style.objectFit==='cover'&&Number(style.opacity)>0&&style.visibility!=='hidden'
                &&['absolute','fixed'].includes(style.position);
            });
          },binding.id===plan.entry_page_id);
          run.checks.entry_products_visible=true;
          if (plan.affiliation && binding.id===plan.entry_page_id) {
            run.checks.entry_products_visible=await page.locator('[data-product-id]').evaluateAll(nodes=>
              nodes.some(n=>{
                const image=n.querySelector('img'), a=n.querySelector('a[rel~="sponsored"]');
                if(!image || !a) return false;
                const r=image.getBoundingClientRect(), b=a.getBoundingClientRect();
                return image.complete&&image.naturalWidth>0&&r.width>0&&r.height>0&&r.top>=0&&r.bottom<=innerHeight&&b.width>0&&b.height>0&&b.top>=0&&b.bottom<=innerHeight;
              }));
          }
          const screenshot='EXECUTION-browser/'+i+'-'+profile+'.png';
          await page.screenshot({path:path.join(project,screenshot),fullPage:true});
          run.screenshot_path=screenshot;
          run.screenshot_sha256=hash(fs.readFileSync(path.join(project,screenshot)));
          run.checks.search=intended.kind==='landing';
          if (intended.kind!=='landing') {
            const search=binding.search;
            if (!search || !search.query || !search.expected_path) throw new Error('Search scenario absent');
            const input=page.locator('input[type="search"],[role="searchbox"]').first();
            await input.fill(search.query);
            await input.press('Enter');
            await page.waitForTimeout(300);
            run.checks.search=await page.locator('[data-search-results] a').evaluateAll((links,expected)=>
              links.some(a=>new URL(a.href,location.href).pathname===expected&&a.getBoundingClientRect().height>0),search.expected_path);
            await input.fill('ZZZ_NO_RESULT_98614');
            await input.press('Enter');
            await page.waitForTimeout(300);
            run.checks.search_empty=await page.locator('[data-search-results] a').evaluateAll(links=>
              links.every(a=>a.getBoundingClientRect().height===0));
            await page.goto(url,{waitUntil:'networkidle'});
          } else run.checks.search_empty=true;
          run.checks.navigation=false;
          const links=page.locator('a[href]');
          for(let n=0;n<await links.count();n++) {
            const href=await links.nth(n).getAttribute('href');
            const next=new URL(href,url);
            if(next.origin!==target.origin || next.href===url || next.hash ||
               !state.pages.some(p=>p.public&&p.wave==='V1'&&p.path===next.pathname) ||
               !(await links.nth(n).isVisible())) continue;
            await links.nth(n).click();
            await page.waitForURL(next.href,{timeout:10000});
            run.checks.navigation=true;
            break;
          }
          if (!Object.values(run.checks).every(Boolean) || errors.length) throw new Error('Browser checks failed');
        } catch(error) {
          errors.push(String(error.message)); report.status='BLOCKED';
          report.errors.push(binding.id+'/'+profile+': '+error.message);
        }
        report.runs.push(run);
        await page.close();
      }
      await context.close();
    }
    report.feature_runs=[];
    for(const feature of plan.features||[]) {
      if(feature.decision==='EXCLUDE'||feature.id==='internal_search') continue;
      const rel=feature.case_path;
      if(typeof rel!=='string'||rel.includes('\\\\')||rel.split('/').some(x=>x==='..'||x==='.')||path.isAbsolute(rel))
        throw new Error('Invalid feature case path');
      const casePath=path.join(project,rel);
      if(!fs.realpathSync(casePath).startsWith(fs.realpathSync(project)+path.sep)) throw new Error('Feature path outside project');
      const raw=fs.readFileSync(casePath), definition=JSON.parse(raw);
      if(definition.feature_id!==feature.id) throw new Error('Feature identity mismatch');
      for(let index=0;index<definition.scenarios.length;index++) {
        const scenario=definition.scenarios[index];
        const intended=state.pages.find(x=>x.id===scenario.page_id);
        if(!intended||!['desktop','mobile'].includes(scenario.profile)) throw new Error('Feature scope invalid');
        const viewport=scenario.profile==='desktop'?{width:1440,height:900}:{width:390,height:844};
        const context=await browser.newContext({viewport});
        await context.route('**/*',route=>{
          const req=route.request(), u=new URL(req.url());
          if(!['GET','HEAD'].includes(req.method())||(u.origin!==target.origin&&!allowHosts.includes(u.hostname))) return route.abort();
          return route.continue();
        });
        const page=await context.newPage();
        const run={feature_id:feature.id,scenario_index:index,case_sha256:hash(raw),page_id:scenario.page_id,profile:scenario.profile,status:'PASS',errors:[]};
        try {
          await page.goto(new URL(intended.path,target).href,{waitUntil:'networkidle'});
          for(const action of scenario.actions||[]) {
            const locator=page.locator(action.selector||'html').first();
            switch(action.action) {
              case 'click': await locator.click();break;
              case 'fill': await locator.fill(String(action.value));break;
              case 'press': await locator.press(String(action.value));break;
              case 'select': await locator.selectOption(String(action.value));break;
              case 'check': await locator.check();break;
              case 'uncheck': await locator.uncheck();break;
              case 'set_input':
                await locator.evaluate((el,value)=>{if(!(el instanceof HTMLInputElement))throw new Error('Expected input');el.value=value;el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}));},String(action.value));break;
              default: throw new Error('Unsupported action');
            }
          }
          for(const expected of scenario.expects||[]) {
            const locator=page.locator(expected.selector);
            if(Object.hasOwn(expected,'count')&&(await locator.count())!==expected.count) throw new Error('Count assertion failed');
            if(Object.hasOwn(expected,'text_contains')&&!(await locator.first().innerText()).includes(expected.text_contains)) throw new Error('Text assertion failed');
            if(Object.hasOwn(expected,'visible')&&(await locator.first().isVisible())!==expected.visible) throw new Error('Visibility assertion failed');
            if(expected.attribute&&(await locator.first().getAttribute(expected.attribute))!==expected.value) throw new Error('Attribute assertion failed');
          }
        } catch(error) {
          run.status='BLOCKED';run.errors.push(String(error.message));report.status='BLOCKED';report.errors.push(feature.id+': '+error.message);
        } finally {await context.close();}
        report.feature_runs.push(run);
      }
    }
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(project,'EXECUTION-browser.json'),JSON.stringify(report,null,2)+'\n');
  }
  process.stdout.write(JSON.stringify({status:report.status,runs:report.runs.length,errors:report.errors})+'\n');
  if(report.status!=='PASS') process.exitCode=2;
}
main().catch(error=>{process.stderr.write(String(error.message)+'\n');process.exitCode=2;});
