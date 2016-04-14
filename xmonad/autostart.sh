#!/bin/bash

echo ----- xrandr
xrandr --output DVI-I-1 --primary --output DVI-D-0 --left-of DVI-I-1 --output HDMI-0 --right-of DVI-I-1
echo ----- updateBarValues
python /home/pieter/Coding/Scripts/update-bar-mem.py &
echo ----- xmobar
xmobar ~/.xmobarrc &
echo ----- background
nitrogen --restore &

compton --config /home/pieter/.config/compton.conf -b &

echo ----- redshift
redshift &
xsetroot -cursor_name arrow
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libv4l/v4l2convert.so
xbindkeys
disown
