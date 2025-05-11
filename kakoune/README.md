# Ashen for Kakoune

To install this theme, please download the [ashen.kak](./ashen.kak) file, and
place it inside your `$kak_config/colors` directory. Then, you can run
`:colorscheme ashen` in the command prompt, or add `colorscheme ashen` to your
`kakrc`.

## Notes

The [kak-tree-sitter](https://sr.ht/~hadronized/kak-tree-sitter/) plugin is
supported by default. However, you should take care to load Ashen _after_
initializing `kak-tree-sitter`:

```kak
eval %sh{ kak-tree-sitter -dks --init $kak_session }
colorscheme ashen
```

The color definitions are also declared as Kakoune options:

```kak
declare-option str cursorline "rgb:191919"
declare-option str text "rgb:b4b4b4"
declare-option str red_flame "rgb:C53030"
declare-option str red_glowing "rgb:DF6464"
declare-option str red_ember "rgb:B14242"
declare-option str orange_glow "rgb:D87C4A"
declare-option str orange_blaze "rgb:C4693D"
declare-option str orange_muted "rgb:6D3B22"
declare-option str orange_smolder "rgb:E49A44"
declare-option str orange_golden "rgb:E5A72A"
declare-option str golden_muted "rgb:6D4D0D"
declare-option str brown "rgb:89492a"
declare-option str brown_dark "rgb:322119"
declare-option str blue "rgb:4A8B8B"
declare-option str background "rgb:121212"
declare-option str g_1 "rgb:e5e5e5"
declare-option str g_2 "rgb:d5d5d5"
declare-option str g_3 "rgb:b4b4b4"
declare-option str g_4 "rgb:a7a7a7"
declare-option str g_5 "rgb:949494"
declare-option str g_6 "rgb:737373"
declare-option str g_7 "rgb:535353"
declare-option str g_8 "rgb:323232"
declare-option str g_9 "rgb:212121"
declare-option str g_10 "rgb:1d1d1d"
declare-option str g_11 "rgb:191919"
declare-option str g_12 "rgb:151515"
```
