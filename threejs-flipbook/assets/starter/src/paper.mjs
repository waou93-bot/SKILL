export const PAGE_WIDTH = 2.42;
export const PAGE_HEIGHT = 3.4;
export const SHEETS = 7;
export const THICKNESS = 0.012;

/** Arc-length integration preserves paper width while turning around the spine. */
export function paperProfile(progress, segments = 64, sheet = 0, curlDirection = 1) {
  const t = Math.max(0, Math.min(1, progress));
  const points = [];
  let x = 0;
  let z = (SHEETS - sheet) * THICKNESS * (1 - t) + (sheet + 1) * THICKNESS * t;
  points.push({ x, z });
  for (let step = 1; step <= segments; step++) {
    const u = (step - 0.5) / segments;
    const curl = Math.sin(t * Math.PI) * Math.sin(u * Math.PI / 2) * 0.72;
    // The free edge trails the spine: it bends towards the source side.
    const angle = t * Math.PI - curl * Math.max(-1,Math.min(1,curlDirection));
    x += Math.cos(angle) * PAGE_WIDTH / segments;
    z += Math.sin(angle) * PAGE_WIDTH / segments;
    points.push({ x, z });
  }
  return points;
}

export function boundedPage(page) {
  return Math.max(0, Math.min(SHEETS - 1, Math.round(page)));
}

export function spreadFaces(page) {
  const p = boundedPage(page);
  return p === 0 ? [{ sheet: 0, side: 'front' }] : [
    { sheet: p - 1, side: 'back' },
    { sheet: p, side: 'front' }
  ];
}
