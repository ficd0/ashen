# Television

Please download
[ashen.toml](https://codeberg.org/ficd/ashen/raw/branch/main/television/ashen.toml) and
place it inside your television configuration's theme directory, usually
`~/.config/television/themes`. Then, you can enable Ashen in your television
`config.toml`:

```toml
[ui]
theme = "ashen"
```

If you've installed the [bat](/bat/README.md) integration, you can also add the
following to your `config.toml`:

```toml
[previewers.file]
theme = "Ashen"
```
