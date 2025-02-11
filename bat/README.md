# Bat Extra

Please note, the syntax highlighting in this theme is not 1:1 with the base theme.

To install the `bat` theme:

```Bash
mkdir -p "$(bat --config-dir)/themes"
cd "$(bat --config-dir)/themes"
# Download ashen.tmTheme and put it in this folder
# Then generate the cache
bat cache --build
# Add Ashen to the config file
echo '--theme="Ashen"'>> $(bat --config-dir)/config

```
