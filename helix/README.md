# Ashen For Helix

- [Update Philosophy](#update-philosophy)
- [Manual Install](#manual-install)
- [Recommended Configuration](#recommended-configuration)

![](preview_compact.png)

Ashen is now packaged with Helix! If you have the latest `master` branch of
Helix installed, you already have access to Ashen. Please note that Ashen is
also developed against the latest `master` branch: any new highlight elements
will be supported as soon as possible.

You can preview Ashen with the command `:theme ashen`. To enable it permanently,
set `theme = "ashen"` in the top level of your `config.toml`:

```toml
theme = "ashen"
```

## Update Philosophy

I actively maintain Ashen in this repository. I won't overwhelm Helix's
maintainers with a PR every time I update Ashen here. However, if I make any
significant changes to the theme, and those changes remain stable for a while,
_then_ I will contribute an update to Helix.

Thus, if you want the _latest_ version of Ashen, you may consider manually
installing from this repository. Otherwise, the last _stable_ version is
included with Helix.

## Manual Install

To install Ashen for Helix, please download the `ashen.toml` file and place it
inside your Helix configuration's `themes` folder. I recommend naming the file
`ashen-dev.toml` to avoid conflicting with the theme already bundled with Helix.

For example:

```Bash
# create theme directory if it doesn't exist
mkdir -p ~/.config/helix/themes && \
# download latest version of ashen
curl https://codeberg.org/ficd/ashen/raw/branch/main/helix/ashen.toml \
# save the file as ashen-dev.toml
-o ~/.config/helix/themes/ashen-dev.toml
```

```toml
# ~/.config/helix/config.toml

theme = "ashen-dev"
```

## Recommended Configuration

I recommend enabling certain off-by-default settings for the best experience.

```toml
# ~/.config/helix/config.toml

theme = "ashen"
# or theme = "ashen-dev" if you've
# installed it manually

# The following is not required
# but recommended for the best experience:
[editor]
cursorline = true
# for the colorful mode indicator
color-modes = true
# certain diagnostics are styled as curl
undercurl = true
[editor.indent-guides]
render = true
skip-levels = 1
```
