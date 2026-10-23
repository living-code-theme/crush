import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { resolveAll } from '../scripts/palette.mjs';
const reference = JSON.parse(await readFile(new URL('./fixtures/neovim-syntax.json', import.meta.url)));
// Palette parity is NOT a claim that this application's highlighter exposes these roles.
// See the README's syntax-highlighting limitation; do not invent unsupported theme keys.
for (const f of resolveAll()) test(`${f.name}: available palette matches Neovim, independently of native syntax limitations`, () => {
  for (const [role, color] of Object.entries(reference.flavors[f.id])) assert.equal(f.r(role), color, role);
});
