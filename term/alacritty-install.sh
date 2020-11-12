#! /bin/bash

CUR_DIR=$(pwd)

git clone https://github.com/alacritty/alacritty.git ~/.local/alacritty

alacritty_dir=~/.local/alacritty

cd $alacritty_dir

tic -xe alacritty,alacritty-direct extra/alacritty.info

cd $CUR_DIR
