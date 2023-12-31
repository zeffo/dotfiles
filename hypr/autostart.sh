#!/usr/bin/env bash


waybar &
blueman-applet &
spotify-launcher &


# swaync
killall swaync
pkill swaync
swaync &

# swww
swww init &
swww img ~/.config/hypr/wallpapers/blahaj.png -o DP-2
swww img ~/.config/hypr/wallpapers/tree.png -o HDMI-A-1


# eww
eww daemon &

obs --startreplaybuffer --minimize-to-tray --disable-shutdown-check &



