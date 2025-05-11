# Ashen for Kakoune

To install this theme, please download the [ashen.kak](./ashen.kak) file, and
place it inside your `$kak_config/colors` directory. Then, you can run
`:colorscheme ashen` in the command prompt, or add `colorscheme ashen` to your
`kakrc`. **Note: in the near future, the theme will be migrated to a separate repository to facilitate easy installation and updating via plugin managers.**

## Extra Features

### Dynamic Cursor

Ashen also provides a dynamic cursor option. When it's enabled, the cursor
changes color dynamically; the default orange for normal mode, and light gray
for insert mode. The colors are tuned such that it's always easy to tell which
is your primary selection. To enable this feature, set the
`ashen_dynamic_cursor` option _after_ loading the theme:

```kak
colorscheme ashen
set-option global ashen_dynamic_cursor true
```

### Tree-Sitter

The [kak-tree-sitter](https://sr.ht/~hadronized/kak-tree-sitter/) plugin is
supported. You should take care to load Ashen _after_ initializing
`kak-tree-sitter`. Otherwise, `kak-tree-sitter` may overwrite some of our faces.

```kak
eval %sh{ kak-tree-sitter -dks --init $kak_session }
colorscheme ashen
```

Besides the plugin's default faces, Ashen also supports all of Helix's capture
groups. In practice, this means that as long as you're using a `highlights.scm`
query file taken from the Helix repository, the highlighting will look as close
as possible to how it does in Ashen for Helix.

**For this to work, you need to update your `kak-tree-sitter` configuration.**
Please add the following to your `$XDG_CONFIG_HOME/kak-tree-sitter/config.toml`:

```
[highlight]

groups = [
    "punctuation.bracket",
    "punctuation.delimiter",
    "constant.builtin",
    "constant.character.escape",
    "constant.numeric",
    "string.special.url",
    "comment.block.documentation",
    "keyword.operator",
    "markup.list",
]
```

### Color Definitions

If you want to use Ashen's colors in your own face definitions, they are
available as Kakoune options:

```kak
%opt{cursorline}
%opt{text}
%opt{red_flame}
%opt{red_glowing}
%opt{red_ember}
%opt{orange_glow}
%opt{orange_blaze}
%opt{orange_muted}
%opt{orange_smolder}
%opt{orange_golden}
%opt{golden_muted}
%opt{brown}
%opt{brown_dark}
%opt{blue}
%opt{background}
%opt{g_1}
%opt{g_2}
%opt{g_3}
%opt{g_4}
%opt{g_5}
%opt{g_6}
%opt{g_7}
%opt{g_8}
%opt{g_9}
%opt{g_10}
%opt{g_11}
%opt{g_12}
```
