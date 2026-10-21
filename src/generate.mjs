// Crush Palette JSON: every public palette token, including diff surfaces and the ANSI palette.
import { ANSI_ORDER } from '../scripts/palette.mjs';
const roles = {
  primary: 'accent', secondary: 'decorator', accent: 'info', keyword: 'keyword', fg_base: 'fg',
  fg_subtle: 'fgAlt', fg_more_subtle: 'fgMuted', fg_most_subtle: 'fgSubtle', bg_base: 'bg',
  bg_most_visible: 'selection', bg_less_visible: 'lineHighlight', bg_least_visible: 'bgAlt',
  on_primary: 'bg', separator: 'border', destructive: 'removed', error: 'error', warning: 'warning',
  warning_subtle: 'warning', attention: 'number', busy: 'warning', info: 'info', info_more_subtle: 'info',
  info_most_subtle: 'fgSubtle', success: 'success', success_more_subtle: 'success', success_most_subtle: 'hint',
  diff_insert_fg: 'added', diff_delete_fg: 'removed', yolo: 'warning', plan: 'info', plan_more_subtle: 'fgSubtle',
  button: 'accent', button_subtle: 'lineHighlight', button_inactive: 'border', button_hovered: 'selection',
};
export function generate(flavors) {
  return flavors.map(f => ({ path: `themes/${f.slug}.json`, content: JSON.stringify({
    ...Object.fromEntries(Object.entries(roles).map(([key, role]) => [key, f.r(role)])),
    diff_insert_code_bg: f.mix('bg', 'added', 0.10), diff_insert_gutter_bg: f.mix('bg', 'added', 0.16),
    diff_delete_code_bg: f.mix('bg', 'removed', 0.10), diff_delete_gutter_bg: f.mix('bg', 'removed', 0.16),
    ...Object.fromEntries(ANSI_ORDER.flatMap((name, i) => [[`ansi_${name}`, f.ansi.normal[i]], [`ansi_bright_${name}`, f.ansi.bright[i]]])),
  }, null, 2) + '\n' }));
}
