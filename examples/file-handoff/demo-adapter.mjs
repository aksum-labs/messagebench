// Synthetic-only file producer, run separately from MessageBench.
// This is not an XML translator or a production adapter. It only accepts the six
// bundled Gate 1 sources, whose structure is fixed and whose bytes are synthetic.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const destination = process.argv[2];
if (!destination || process.argv.length !== 3) {
  throw new Error('Usage: node demo-adapter.mjs OUTPUT_DIRECTORY');
}
mkdirSync(destination, { recursive: true });
const manifest = JSON.parse(readFileSync(resolve(root, 'corpus/gate1-index.json'), 'utf8'));
for (const fixture of manifest.cases) {
  if (!/^[a-z0-9-]+$/.test(fixture.id) || !/^(positive|negative)\/[a-z0-9-]+\.source\.xml$/.test(fixture.source)) {
    throw new Error('Only bundled synthetic fixtures are accepted');
  }
  let xml = readFileSync(resolve(root, 'corpus', fixture.source), 'utf8');
  if (!xml.includes('AKSUM-SYNTHETIC-0001')) throw new Error('Unexpected synthetic source');
  xml = xml.replace('<MsgId>AKSUM-SYNTHETIC-0001</MsgId>', '<MsgId>EXTERNAL-STYLE-NEW-ID</MsgId>');
  xml = xml.replace('>1250.50</IntrBkSttlmAmt>', '>1250.5000</IntrBkSttlmAmt>');
  xml = xml.replace('<Ustrd>INVOICE 000123</Ustrd><Ustrd>ሙከራ</Ustrd>',
                    '<Ustrd>ሙከራ</Ustrd><Ustrd>INVOICE 000123</Ustrd>');
  xml = xml.replace('xmlns=', 'xmlns:p=');
  xml = xml.replace(/<(\/?)([A-Za-z][A-Za-z0-9]*)/g, '<$1p:$2');
  writeFileSync(resolve(destination, fixture.id + '.xml'), xml, { flag: 'wx', mode: 0o600 });
}
console.log(`Wrote ${manifest.cases.length} synthetic adapter outputs`);
