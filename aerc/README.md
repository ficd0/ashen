# Aerc Theme

`aerc` is an excellent TUI email client. To install the theme, you first need to
create a folder called `stylesets` in your `aerc` configuration:

```bash
mkdir -p $HOME/.config/aerc/stylesets
```

Next, you need to download the
[ashen](https://codeberg.org/ficd/ashen/raw/branch/main/aerc/ashen) file and place it
inside that folder. Finally, you have to select it in you `aerc.conf`:

```ini
styleset-name=ashen
```
