import { writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const [origin, output] = process.argv.slice(2);
const page = await fetch(origin);
if (!page.ok) throw new Error(`Home returned ${page.status}`);
const html = await page.text();
const scripts = [...html.matchAll(/<script\b[^>]*src="([^"]+)"/g)].map(m => new URL(m[1], origin).href);
const bundles = [];
const pending = [...scripts];
const visited = new Set();
while (pending.length) {
  const url = pending.shift();
  if (visited.has(url)) continue;
  visited.add(url);
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Bundle returned ${response.status}`);
  const source = await response.text();
  bundles.push({ url, sha256: createHash('sha256').update(source).digest('hex'), updatedCards: source.includes('Cards follow the audio. Tap to flip.') });
  for (const match of source.matchAll(/import\([`'"](\.\/[^`'"]+\.js)[`'"]\)/g)) pending.push(new URL(match[1], url).href);
}
if (!bundles.some(bundle => bundle.updatedCards)) throw new Error('New card behavior is missing from served bundle');
const healthResponse = await fetch(new URL('/_health', origin));
const health = await healthResponse.json();
const certificateStatus = (await fetch(new URL('/api/certificate', origin))).status;
if (health.app !== 'ok' || health.db !== 'ok' || certificateStatus !== 401) throw new Error('Hosted health or authentication check failed');
const proof = { origin, verifiedAt: new Date().toISOString(), health, certificateStatus, bundles };
writeFileSync(output, JSON.stringify(proof, null, 2) + '\n');
console.log(JSON.stringify(proof));
