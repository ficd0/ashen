#!/usr/bin/env zsh

typeset -A ZSH_HIGHLIGHT_STYLES

# brackets
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#C53030'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#737373'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#949494'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#a7a7a7'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#b4b4b4'
ZSH_HIGHLIGHT_STYLES[bracket-level-5]='fg=#d5d5d5'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='standout'

# cursor
ZSH_HIGHLIGHT_STYLES[cursor]='standout'

# line
ZSH_HIGHLIGHT_STYLES[line]=''

# main
ZSH_HIGHLIGHT_STYLES[default]='none'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#C53030'
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#B14242'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#4A8B8B,underline'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#4A8B8B'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#D87C4A,underline'
ZSH_HIGHLIGHT_STYLES[commandseparator]='none'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#D87C4A,underline'
ZSH_HIGHLIGHT_STYLES[path]='underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]=''
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=''
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#E5A72A'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#4A8B8B'
ZSH_HIGHLIGHT_STYLES[command-substitution]='none'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#E5A72A'
ZSH_HIGHLIGHT_STYLES[process-substitution]='none'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#E5A72A'
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='none'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='none'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#E5A72A'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#DF6464'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#DF6464'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#DF6464'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=cyan'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#DF6464,bold'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#DF6464,bold'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#DF6464,bold'
ZSH_HIGHLIGHT_STYLES[assign]='none'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#E5A72A'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#737373'
ZSH_HIGHLIGHT_STYLES[named-fd]='none'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='none'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#C4693D,bold'

# root
ZSH_HIGHLIGHT_STYLES[root]='standout'

export ZSH_HIGHLIGHT_STYLES
