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
swww img ~/.config/hypr/wallpapers/blahaj.png -o DP-2 --transition-fps 255 
wallpapers=("pixelmountain.gif" "pixeltrain.gif" "sakura.gif") 
size=${#wallpapers[@]}
index=$(($RANDOM % $size))
swww img ~/.config/hypr/wallpapers/${wallpapers[$index]} -o HDMI-A-1 --transition-fps 255

# eww
eww daemon &

# rgb
sudo modprobe cdc-acm
glowworm &

openrgb -p gay



