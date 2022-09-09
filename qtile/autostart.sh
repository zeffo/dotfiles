#!/usr/bin/env bash 

/usr/bin/prismatik &    # Prismatik (For Ambient Lighting)

nfetch="alacritty --hold -e neofetch"
$nfetch &    # Alacritty with Neofetch (Cosmetic)

picom -b # Compositor (for transparency)


