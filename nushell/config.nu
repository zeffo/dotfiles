# config.nu
#
# Installed by:
# version = "0.101.0"
#
# This file is used to override default Nushell settings, define
# (or import) custom commands, or run any other startup tasks.
# See https://www.nushell.sh/book/configuration.html
#
# This file is loaded after env.nu and before login.nu
#
# You can open this file in your default editor using:
# config nu
#
# See `help config nu` for more options
#
# You can remove these comments if you want or leave
# them for future reference.

use std/util "path add"

source ~/zoxide/.zoxide.nu
source ~/.local/share/atuin/init.nu
source ~/.config/nushell/theme.nu

$env.PROMPT_COMMAND = {
  [
    (ansi {fg: $theme.pink})
    (char -u e0b6)
    (ansi {fg: $theme.crust bg: $theme.pink attr: b})
    ($env.USER)
    (ansi {fg: $theme.pink bg: $theme.red})
    (char -u e0bc)
    (ansi {fg: $theme.red bg: $theme.peach})
    (char -u e0bc)
    (ansi {fg: $theme.peach bg: $theme.yellow})
    (char -u e0bc)
    (ansi {fg: $theme.yellow bg: $theme.green})
    (char -u e0bc)
    (ansi {fg: $theme.green bg: $theme.blue})
    (char -u e0bc)
    (ansi {fg: $theme.mauve bg: $theme.blue})
    (char -u e0ba )
    (ansi reset)
    (ansi {fg: $theme.base bg: $theme.mauve})
    (pwd | str replace $env.HOME '~')
    (ansi {fg: $theme.mauve bg: $theme.base})
    (char -u e0b4)
    (ansi {fg: $theme.pink})
    (char newline)
    ($"(char -u f4c8) ")
  ] | str join
}
$env.PROMPT_INDICATOR = " "
$env.PROMPT_INDICATOR_VI_NORMAL = " "
$env.PROMPT_INDICATOR_VI_INSERT = " "
$env.PROMPT_MULTILINE_INDICATOR = "~  "

def in_git_repo [] {
  (do -i { git rev-parse --abbrev-ref HEAD } | complete | get stderr | is-empty)
}
$env.PROMPT_COMMAND_RIGHT = {
  let in_repo = in_git_repo
  if $in_repo {
    [
      (ansi reset)
      (ansi { fg: $theme.pink attr: b })
      (char -u e0b6)
      (ansi {fg: $theme.crust bg: $theme.pink })
      (git branch --show-current)
      (ansi {fg: $theme.pink bg: $theme.crust})
      (char -u e0b4)
    ] | str join
  } else {
    ""
  }
}

$env.config.show_banner = false

let MENU_STYLE = {
  text: $theme.pink,
  selected_text: {fg: $theme.base, bg: $theme.pink, attr: b}, 
  description_text: {fg: $scheme.virtual_text, attr: i},
  selected_match_text: {fg: $theme.base, bg: $theme.pink, attr: bui},
  match_text: $theme.mauve
} 

$env.config = {
  edit_mode: "vi"
  buffer_editor: "nvim"
  cursor_shape: {
    vi_insert: "line"
    vi_normal: "block"
  }
  history: {
    sync_on_enter: true,
    file_format: "sqlite"
    max_size: 5_000_000
  }
  menus: [
    {
      name: completion_menu
      only_buffer_difference: false
      marker: " "
      type: {
        layout: columnar
        columns: 1               
        col_width: 5             
        col_padding: 2
      }
      style: $MENU_STYLE
    }
    {
      name: history_menu
      only_buffer_difference: true
      marker: " "
      type: {
        layout: list
        page_size: 10
      }
      style: $MENU_STYLE
    }
  ]
  keybindings: [
    {
      name: complete_history_hint_word
      modifier: control
      keycode: space
      mode: [vi_normal vi_insert]
      event: {send: HistoryHintWordComplete}
    }
    {
      name: complete_history_hint
      modifier: control_alt
      keycode: space
      mode: [vi_normal vi_insert]
      event: {send: HistoryHintComplete}
    }
  ]
}

$env.config = (
    $env.config | upsert keybindings (
        $env.config.keybindings
        | append {
            name: atuin
            modifier: control
            keycode: char_r
            mode: [emacs, vi_normal, vi_insert]
            event: { send: executehostcommand cmd: (_atuin_search_cmd) }
        }
    )
)

# Completers

let fish_completer = {|spans|
  fish --command $'complete "--do-complete=($spans | str join " ")"'
    | from tsv --flexible --noheaders --no-infer
    | rename value description
}


$env.config.completions.external = {
  enable: true
  max_results: 10
  completer: {|spans|
    match $spans.0 {
      _ => $fish_completer
    } | do $in $spans
  }
}

# Custom

def rand_file_name [] {
  let randuuid = random uuid
  return $'/tmp/($randuuid).md'
}

def sp [fp?: string ] {
  if ($fp | describe) == "nothing" {
    let path = rand_file_name
    nvim $path
    rm $path
  } else { 
    nvim $fp
  }
}

def --env av [] {
  let venv = ls -af | where name =~ .venv
  if (($venv | is-not-empty) and (($venv | first | get type) == dir)) {
    let path = ($venv | first | get name)
    nu -e $"overlay use ($path)/bin/activate.nu"
  } else {
    let poetry = poetry env activate | complete
    if ($poetry | get exit_code) == 0 {
      nu -e ($poetry | get stdout)
    }
  }
}

def syu [] {
  topgrade --only cargo firmware go rustup system tldr vim
}

def compress [quality: int] {
  wl-paste | magick - -format PNG -quality $quality - | wl-copy
}


def c-complete [context: string] {
  let target = ($context | split row " " | skip 1)

  if ($target | is-empty) or (($target | get 0 | str trim) == "") {
    return null
  }

  let zox = (
    zoxide query -l -s --exclude $env.PWD -- ...$target
    | lines
    | first 20
    | each {|row|
        let sp = ($row | str trim | split row " " -n 2)
        {
          value: ($sp | get 1 | str replace $"($env.PWD)/" "")
          description: ($sp | get 0)
        }
      }
  )

  let done = ($zox | get value)

  let local = (
    ls -a
    | where type == dir
    | get name
    | where {|n| not ($n in $done) }
    | each {|n| { value: $n } }
  )

  let results = ($zox | append $local | uniq-by value)

  if ($results | is-empty) {
    return null
  }

  {
    options: {
      case_sensitive: false
      completion_algorithm: fuzzy
      positional: false
      sort: false
    }
    completions: $results
  }
}


export def --env c [...path: string@c-complete] {
  z ($path | str join " ")
}


# Aliases

alias gitui = gitui -t mocha.ron
alias fox = firefox-developer-edition
alias grep = rg
alias cat = bat
alias spire = spotify_player
alias tclock = tclock -c magenta
alias fetch = fastfetch
alias erd = erd -H
alias v = nvim .

# Environment

path add "~/.cargo/bin"
path add "/usr/local/bin"
path add "~/go/bin"
path add "~/.local/bin"
$env.BAT_THEME = "Catppuccin Mocha"
$env.EDITOR = "nvim"
$env.TERMINAL = "kitty"
$env.TERM = "kitty"

# Misc

$env.LS_COLORS = (vivid generate ~/.config/nushell/vivid_theme.yml)

# Interactive

pokeget random --hide-name
char newline

