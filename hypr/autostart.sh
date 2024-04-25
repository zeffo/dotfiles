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
swww img ~/.config/hypr/wallpapers/blahaj.png -o DP-2 --transition-fps 255 
wallpapers=("pixelmountain.gif" "pixeltrain.gif") 
size=${#wallpapers[@]}
index=$(($RANDOM % $size))
swww img ~/.config/hypr/wallpapers/${wallpapers[$index]} -o HDMI-A-1 --transition-fps 255

# eww
eww daemon &

# rgb
sudo modprobe cdc-acm
sleep  10
openrgb --startminimized -p MAIN0 &


