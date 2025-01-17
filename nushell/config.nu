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
$env.PROMPT_COMMAND_RIGHT = {""}
$env.config.show_banner = false
