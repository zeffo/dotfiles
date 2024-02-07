#!/usr/bin/env bash



waybar &
hyprctl setcursor Catppuccin-Mocha-Pink-Cursors 24
blueman-applet &

# swaync
killall swaync
pkill swaync
swaync &

# swww
swww kill
swww init
swww img ~/.config/hypr/wallpapers/blahaj.png -o eDP-1 --transition-fps 255 

# eww
eww daemon &

# rgb
openrgb --startminimized -p MAIN0 &


