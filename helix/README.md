# Ashen For Helix

> [!WARNING]
> The Helix theme is still in beta! I recommend checking this repo for updates often. I'm still new to using Helix myself, so I'm certain I'll find ways to improve the theme.

To install Ashen for Helix, please download the `ashen.toml` file 
and place it inside your Helix configuration's `themes` folder.
For example:

```Bash
mkdir -p ~/.config/helix/themes && \
curl https://raw.githubusercontent.com/ficcdaf/ashen/refs/heads/main/helix/ashen.toml \
-o ~/.config/helix/themes/ashen.toml
```

To enable the theme, add the following to your Helix `config.toml`:

```toml
# This should be in the root level
# of the toml file
theme = "ashen"

# The following is not required
# but recommended for the best experience:
[editor]
cursorline = true
color-modes = true
# if your terminal supports undercurl
undercurl = true
[editor.indent-guides]
render = true
skip-levels = 1
```
