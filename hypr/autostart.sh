#!/usr/bin/env bash

waybar &
hyprctl setcursor catppuccin-mocha-pink-cursors 24
blueman-applet &

wl-paste --watch cliphist store &

# swaync
killall swaync
pkill swaync
swaync &

swww kill
swww-daemon &
swww img ~/.config/hypr/wallpapers/sakuracat.gif -o DP-2 -f Nearest
swww img ~/.config/hypr/wallpapers/cat.gif -o HDMI-A-1 -f Nearest

# eww
eww daemon &

# rgb
sudo modprobe cdc-acm
glowworm &

openrgb -p gay



