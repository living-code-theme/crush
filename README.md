<!-- living-code-readme:1 -->
# 💘 Living Code for Crush

**Calm slate. Living color.** Living Code for Crush: complete native palette files with UI surfaces, status colors, review diffs and all sixteen ANSI colors.

[Installation](#installation) · [Flavors](#flavors) · [Configuration](#configuration) · [All ports](https://github.com/living-code-theme)

## Previews

Real application screenshots have not been captured yet.

## Installation

```sh
git clone https://github.com/living-code-theme/crush.git
cd crush
```

On Linux with the default config location:

```sh
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/crush/themes"
cp themes/*.json "${XDG_CONFIG_HOME:-$HOME/.config}/crush/themes/"
```

Open Crush, press **Ctrl+P**, choose **Themes**, and select `living-code-night`. If you use `CRUSH_GLOBAL_CONFIG`, place `themes/` alongside that global config file instead. On other platforms, use the `themes/` directory beside Crush’s global config.

## Flavors

Expand a flavor for its full-size preview and activation instructions.

<details data-lc-flavor="night">
<summary><strong>Night</strong> · Dark · full palette</summary>

A real application capture is not available yet.

Choose `living-code-night` in **Ctrl+P → Themes**.

</details>

<details data-lc-flavor="frost">
<summary><strong>Frost</strong> · Dark · softer chroma</summary>

A real application capture is not available yet.

Choose `living-code-frost` in **Ctrl+P → Themes**.

</details>

<details data-lc-flavor="paper">
<summary><strong>Paper</strong> · Light · near-white slate</summary>

A real application capture is not available yet.

Choose `living-code-paper` in **Ctrl+P → Themes**.

</details>

<details data-lc-flavor="signal">
<summary><strong>Signal</strong> · Dark · teal accent</summary>

A real application capture is not available yet.

Choose `living-code-signal` in **Ctrl+P → Themes**.

</details>

## Configuration

For a persistent config selection, merge the following into your existing Crush config:

```json
{ "options": { "tui": { "active_theme": "living-code-night" } } }
```

The files specify every public `Palette` field and do not rely on an unrelated base theme. Diff code and gutter backgrounds have independent tints, and raw terminal output gets all sixteen Living Code ANSI colors.

## Compatibility

Requires a Crush release supporting standalone JSON theme files and `options.tui.active_theme`. This API was verified against the source revision recorded in `test/fixtures/upstream.json`; older builds without custom themes need an update. The field contract is extracted from Crush’s own palette implementation. No custom providers or credentials are installed.

## Contributing

Found a problem? [Open an issue](https://github.com/living-code-theme/crush/issues/new/choose) with the app version, the flavor and a screenshot. Want Living Code somewhere else? [Request a port](https://github.com/living-code-theme/core/issues/new?template=port-request.yml).

Pull requests are welcome. Keep this README, `port.json` and `images/` in sync, and use real screenshots of the app, never mockups.

🦎 **One chameleon, many habitats.** Part of [Living Code](https://github.com/living-code-theme).

## License

[MIT](LICENSE) © Elliot Luque
