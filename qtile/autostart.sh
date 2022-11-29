#!/usr/bin/env bash 

# /usr/bin/prismatik &    # Prismatik (For Ambient Lighting)

picom -b

alac="alacritty --hold -e"

htop="$alac htop"
pipes="$alac pipes.sh"
matrix="$alac unimatrix -s 97"
nfetch="bash -i -c neofetch"
gotop="$alac gotop"
alacritty="alacritty"

$htop &
$matrix &
$pipes &
$alacritty &
$gotop &


# systemctl restart bluetooth.service # restart bluetooth because it f**king sucks
