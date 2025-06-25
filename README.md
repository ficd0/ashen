# Ashen

> _**Let the fire fade — not your focus**._
>
> _Designed for long nights and longer thoughts._

![](helix/preview_wide.png)

[Ashen](https://sr.ht/~ficd/ashen/) is a warm, muted theme born from the glow of
dying embers — rich in reds, orange highlights, and layers of gray. Inspired by
_Dark Souls III_, it's crafted to be gentle on the eyes and steady on the mind.
Whether you're deep in the terminal or writing code by candlelight — Ashen
offers a calm, focused atmosphere for development after dark.

This monorepository contains official implementations of Ashen across a range of
editors, terminals, tools, and more — each carefully tuned to carry the same
muted warmth. The project is developed on
[sourcehut](https://sr.ht/~ficd/ashen/) and provides a read-only mirror on
[GitHub](https://github.com/ficcdaf/ashen). Please see
[Contributing](#contributing) to learn how to contribute to Ashen.

- [Editors](#editors)
- [Terminals](#terminals)
- [Tools & Interfaces](#tools--interfaces)
- [Desktop & UI](#desktop--ui)
- [Theme Formats](#theme-formats)
- [Contributing](#contributing)

![](preview/palette.png)

## Editors

> _Where syntax takes shape._

- [Helix](./helix/README.md) — the best theme for the best editor.
- [Neovim](https://git.sr.ht/~ficd/ashen.nvim) — Lua plugin for modern Vim
  sorcerers.
- [Kakoune](https://git.sr.ht/~ficd/kak-ashen) — POSIX compliant editing, in
  style.

## Terminals

> _Words against the dark — quiet, deliberate._

- [Ghostty](./ghostty/README.md) — sleek and spectral.
- [Kitty](./kitty/README.md) — for configuration fiends seeking warm tones.
- [Alacritty](./alacritty/README.md) — no distractions, just firepower.
- [Windows Terminal](./windows-terminal/README.md) — Ashen for the dark side.
- [WezTerm](./wezterm/README.md) — endlessly configurable, never loud.
- [foot](./foot/README.md) — a dark theme for a light terminal.

## Tools & Interfaces

> _Terminal tools softened by firelight._

- [bat](./bat/README.md) — like `cat`, but warmer.
- [eza](./eza/README.md) — a modern `ls` with subtle highlights.
- [lazygit](./lazygit/README.md) — `git` bathed in ember tones.
- [yazi](./ashen.yazi/README.md) — fast, clean file browsing.
- [fzf](./fzf/README.md) — fuzzy finding with focus.
- [fish](./fish/README.md) — the friendly shell made even friendlier.
- [television](./television/README.md) — fuzzier `fzf` in gray.
- [aerc](./aerc/README.md) — email done plainly, with muted elegance.
- [zellij](./zellij/README.md) — terminal multiplexed with subdued grace.

## Desktop & UI

> _Let your environment glow._

- [waybar](./waybar/README.md) — a status bar with just enough light.
- [sway](./sway/README.md) — a tiled workspace in quiet tones.
- [fuzzel](./fuzzel/README.md) — launch your apps with a whisper.
- [zathura](./zathura/README.md) — focused reading for tired eyes.
- [Firefox](./firefox/README.md) — the web, dimmed for comfort.
- [Monkeytype](./monkeytype/README.md) — compose Shakespeare, Ashen style.

## Theme Formats

> _For bringing Ashen elsewhere._

- [tmTheme](./tmtheme/README.md) — classic syntax format (TextMate, Sublime, and
  more).
- [Base16](./base16/README.md) — highly portable, no-nonsense theme
  specification.
- [Pygments](./pygments/README.md) — Python library and CLI tool for syntax
  highlighting.

## Contributing

To submit bug reports and requests, please visit the
[ticket tracker](https://todo.sr.ht/~ficd/ashen). For any other discussions,
contact the [mailing list](https://lists.sr.ht/~ficd/ashen) (_possibly by
carrier pigeon_.)

I do not accept PRs on GitHub! Please consult
[the documentation](https://man.sr.ht/git.sr.ht/#sending-patches-upstream) to
learn how to contribute on sourcehut. Send your patches to
[~ficd/ashen-devel](https://lists.sr.ht/~ficd/ashen-devel).

If you're porting Ashen, use the existing ports as a reference for the palette
and overall feel. Treat [Helix](./helix/README.md) as the "ultimate" guide on
the colors to be assigned to syntax elements.

As a rule of thumb: numbers and builtin literal types should be `blue`, strings
`red_glowing`, keywords `red_ashen`, operators `orange_blaze`, delimiters
`orange_smolder`, brackets `g_6`, and special punctuation `orange_golden`.
`red_flame` should _only_ be used for errors, and `orange_golden` is the
preferred color for warnings. Ashen doesn't use green, so you can pick an
appropriate substitute from the palette. For example, the terminal themes use
`orange_blaze` for green, which looks good in most applications.
