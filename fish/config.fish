if status is-interactive
    # Commands to run in interactive sessions can go here
    atuin init fish | source
    zoxide init fish | source
    set -x EDITOR nvim
    set -x BAT_THEME Catppuccin-mocha

    alias ...="cd ../.."
    alias gitui="gitui -t mocha.ron"
    alias cd="z" 
    alias fox='firefox-developer-edition'
    alias ls='eza --icons=always --no-quotes --group-directories-first --hyperlink'
    alias grep='ag'
    alias pdf="termpdf.py"
    alias cat="bat"
    alias spire="spotify_player"
    alias av="source .venv/bin/activate.fish"

    pokeget random --hide-name; echo;
end





