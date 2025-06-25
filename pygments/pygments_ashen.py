# pyright: basic
"""Implementation of Ashen for Pygments."""

from dataclasses import dataclass
from typing import final
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)


@final
@dataclass
class AshenPalette:
    cursorline = "#191919"
    text = "#b4b4b4"
    red_flame = "#C53030"
    red_glowing = "#DF6464"
    red_ember = "#B14242"
    orange_glow = "#D87C4A"
    orange_blaze = "#C4693D"
    orange_muted = "#6D3B22"
    orange_smolder = "#E49A44"
    orange_golden = "#E5A72A"
    golden_muted = "#6D4D0D"
    brown = "#89492a"
    brown_dark = "#322119"
    brown_darker = "#22150F"
    blue = "#4A8B8B"
    background = "#121212"
    g_1 = "#e5e5e5"
    g_2 = "#d5d5d5"
    g_3 = "#b4b4b4"
    g_4 = "#a7a7a7"
    g_5 = "#949494"
    g_6 = "#737373"
    g_7 = "#535353"
    g_8 = "#323232"
    g_9 = "#212121"
    g_10 = "#1d1d1d"
    g_11 = "#191919"
    g_12 = "#151515"


class AshenStyle(Style):
    c = AshenPalette()
    styles = {
        Comment: f"{c.g_6} italic",
        Generic: c.text,
        Generic.Deleted: c.red_flame,
        Generic.Emph: f"{c.text} underline",
        Generic.Error: c.red_flame,
        Generic.Heading: f"{c.red_glowing} bold",
        Generic.Inserted: f"{c.text} bold",
        Generic.Output: c.g_5,
        Generic.Prompt: c.orange_glow,
        Generic.Strong: f"{c.text} bold",
        Generic.Subheading: f"{c.red_glowing} bold",
        Generic.Traceback: c.text,
        Error: c.red_flame,
        # `as`
        Keyword: c.red_ember,
        Keyword.Constant: c.blue,
        Keyword.Declaration: f"{c.red_ember} italic",
        # `from`, `import`
        Keyword.Namespace: c.red_ember,
        Keyword.Pseudo: c.red_ember,
        Keyword.Reserved: c.red_ember,
        Keyword.Type: c.blue,
        Literal: c.text,
        Literal.Date: c.text,
        # from xxx import NAME
        # NAME = NAME
        # NAME.NAME()
        Name: c.text,
        Name.Attribute: c.g_4,
        # `len`, `print`
        Name.Builtin: f"{c.blue}",
        # `self`
        Name.Builtin.Pseudo: c.red_ember,
        # class Name.Class:
        Name.Class: c.blue,
        Name.Constant: c.blue,
        Name.Decorator: f"{c.g_3} italic bold",
        Name.Entity: c.blue,
        Name.Exception: c.blue,
        # def __Name.Label__(
        Name.Function: c.text,
        Name.Label: c.text,
        Name.Namespace: f"{c.orange_glow} bold",
        Name.Other: c.g_2,
        Name.Tag: f"{c.orange_glow} italic",
        Name.Variable: c.g_3,
        Name.Variable.Class: c.g_3,
        Name.Variable.Global: c.g_3,
        Name.Variable.Instance: c.g_3,
        Number: c.blue,
        Number.Bin: c.blue,
        Number.Float: c.blue,
        Number.Hex: c.blue,
        Number.Integer: c.blue,
        Number.Integer.Long: c.blue,
        Number.Oct: c.blue,
        # `=`
        Operator: c.orange_glow,
        # `not`, `in`
        Operator.Word: c.orange_glow,
        Other: c.text,
        # `(`, `)`, `,`, `[`, `]`, `:`
        Punctuation: c.g_2,
        String: c.red_glowing,
        String.Backtick: c.red_glowing,
        String.Char: c.red_glowing,
        String.Doc: c.red_glowing,
        String.Double: c.red_glowing,
        String.Escape: c.g_2,
        String.Heredoc: c.red_glowing,
        String.Interpol: c.red_glowing,
        String.Other: c.red_glowing,
        String.Regex: c.orange_glow,
        String.Single: c.red_glowing,
        String.Symbol: c.red_glowing,
        Text: c.text,
        Whitespace: c.text,
    }
