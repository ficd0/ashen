# Ashen for Kakoune
# Author: Daniel Fichtinger
# License: MIT
# Upstream: https://sr.ht/~ficd/ashen

evaluate-commands %sh{
    cursorline="rgb:191919"
    text="rgb:b4b4b4"
    red_flame="rgb:C53030"
    red_glowing="rgb:DF6464"
    red_ember="rgb:B14242"
    orange_glow="rgb:D87C4A"
    orange_blaze="rgb:C4693D"
    orange_muted="rgb:6D3B22"
    orange_smolder="rgb:E49A44"
    orange_golden="rgb:E5A72A"
    golden_muted="rgb:6D4D0D"
    brown="rgb:89492a"
    brown_dark="rgb:322119"
    blue="rgb:4A8B8B"
    background="rgb:121212"
    g_1="rgb:e5e5e5"
    g_2="rgb:d5d5d5"
    g_3="rgb:b4b4b4"
    g_4="rgb:a7a7a7"
    g_5="rgb:949494"
    g_6="rgb:737373"
    g_7="rgb:535353"
    g_8="rgb:323232"
    g_9="rgb:212121"
    g_10="rgb:1d1d1d"
    g_11="rgb:191919"
    g_12="rgb:151515"
    echo "
        # Code highlighting
        face global value         ${blue}
        face global type          ${blue}
        face global variable      ${g_3}
        face global module        ${orange_glow}+b
        face global function      ${g_3}+b
        face global string        ${red_glowing}
        face global keyword       ${red_ember}
        face global operator      ${orange_glow}
        face global attribute     ${g_4}
        face global comment       ${g_6}+i
        face global documentation comment
        face global meta          ${red_ember}
        face global builtin       ${blue}

        # Markdown highlighting
        face global title     ${red_glowing}+b
        face global header    ${red_glowing}
        face global mono      ${g_2,},${g_10}
        face global block     ${g_2,},${g_10}
        face global link      ${red_glowing}+ui
        face global bullet    ${orange_glow}
        face global list      ${orange_glow}

        face global Default            ${text},${background}
        face global PrimaryCursor   ${background},${orange_blaze}+gfb
        face global SecondaryCursor ${background},${orange_muted}+gf
        face global PrimarySelection      ,${brown_dark}+g
        face global SecondarySelection    ,${brown_dark}+g
        # face global PrimaryCursorEol   ${background},${orange_golden}+fg
        # face global SecondaryCursorEol ${background},${golden_muted}+fg
        face global PrimaryCursorEol   PrimaryCursor
        face global SecondaryCursorEol SecondaryCursor
        face global LineNumbers        ${g_8}
        face global LineNumberCursor   ${g_5},${brown_dark}
        face global LineNumbersWrapped LineNumbers
        face global MenuForeground     ${background},${orange_blaze}+b
        face global MenuBackground     ${g_3},${g_9}
        face global MenuInfo           ${text},${g_9}
        face global Information        MenuBackground
        face global InlineInformation  ${g_6}+i
        face global Error              ${red_flame},${g_10}
        face global DiagnosticError    ,,${red_flame}+c
        face global DiagnosticWarning  ,,${red_flame}+c
        face global StatusLine         ${g_3},${g_9}
        face global StatusLineMode     ${orange_glow}+b
        face global StatusLineInfo     ${red_ember}
        face global StatusLineValue    ${blue}
        face global StatusCursor       ${background},${g_3}+b
        face global Prompt             ${orange_glow}
        face global MatchingChar       ${orange_smolder}+uf
        face global BufferPadding      LineNumbers
        face global Whitespace         ${g_7}+f
    "
}
