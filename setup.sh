#!/bin/sh

# Applying config
cp -r $(pwd)/.config ~/

# Fixes for HyDE
yay -S noto-fonts-emoji

# My packages
yay -S telegram-desktop krita libreoffice steam helix obs-studio cava byedpi-bin
