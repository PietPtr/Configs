#!/bin/bash

xrandr --output DVI-I-1 --primary --output DVI-D-0 --left-of DVI-I-1 --output HDMI-1 --right-of DVI-I-1
xmobar ~/.xmobarrc &
nitrogen --restore &
compton --config ~/.config/compton.conf &
python /home/pieter/Coding/Scripts/updateBarValues.py &
redshift &
disown
