# Bat Extra

To install the `bat` theme:

```Bash
mkdir -p "$(bat --config-dir)/themes"
cd "$(bat --config-dir)/themes"
# Download ashen.tmTheme and put it in this folder
# Then generate the cache
bat cache --build
# Add Ashen to the config file
echo '--theme="ashen"'>> $(bat --config-dir)/config

```
