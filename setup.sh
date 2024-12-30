#!/bin/sh

# Applying config
cp -r $(pwd)/.config ~/

# Packages that are included in HyDE
yay -S eza fish starship

# Fixes for HyDE
yay -S noto-fonts-emoji

# Very important packages
yay -S helix htop

# Others
yay -S telegram-desktop cava krita libreoffice steam obs-studio byedpi-bin
