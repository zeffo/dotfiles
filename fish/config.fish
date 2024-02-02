if status is-interactive
    # Commands to run in interactive sessions can go here
    atuin init fish | source
end

set -x EDITOR nvim
set -x BAT_THEME Catppuccin-mocha

alias hx="helix"
alias fox='firefox-developer-edition'
alias ls='eza --icons=always --no-quotes --group-directories-first --hyperlink'
alias grep='ag'
alias pdf="termpdf.py"
alias cat="bat"
