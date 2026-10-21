import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { resolveAll } from '../scripts/palette.mjs';
import { keys, hexColors, assertContrast } from './helpers.mjs';
const fixture = JSON.parse(await readFile(new URL('./fixtures/upstream.json', import.meta.url)));
const read = path => readFile(new URL('../' + path, import.meta.url), 'utf8');

for (const f of resolveAll()) test(f.name + ': every Crush Palette field and ANSI slot', async () => {
  const t = JSON.parse(await read('themes/' + f.slug + '.json'));
  keys(t, fixture.colors); hexColors(t);
  assert.equal(t.primary, f.r('accent')); assert.equal(t.keyword, f.r('keyword')); assert.equal(t.error, f.r('error'));
  for (const [index, color] of ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'].entries()) {
    assert.equal(t['ansi_' + color], f.ansi.normal[index]); assert.equal(t['ansi_bright_' + color], f.ansi.bright[index]);
  }
  for (const bg of [t.bg_base, t.bg_least_visible, t.bg_most_visible, t.diff_insert_code_bg, t.diff_delete_code_bg]) assertContrast(t.fg_base, bg);
  assertContrast(t.on_primary, t.primary);
});
