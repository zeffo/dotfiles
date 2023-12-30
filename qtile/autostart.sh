#!/usr/bin/env bash 

/usr/bin/prismatik &    # Prismatik (For Ambient Lighting)


alac="alacritty --hold -e"

alacritty="alacritty"
sxhkd="sxhkd"
bottom="$alac btm"
neovim="$alac nvim"

$neovim &
picom -b
$sxhkd &
$bottom &
$alacritty &
