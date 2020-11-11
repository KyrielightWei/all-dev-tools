# ! /bin/bash

term_dir=$(dirname $(readlink -f "$0"))

wget https://sourceforge.net/projects/zsh/files/zsh/5.8/zsh-5.8.tar.xz

tar -xvf zsh-5.8.tar.xz

cd zsh-5.8

./configure --prefix=$HOME/.zsh-install

make && make install

cd ..

rm -rf zsh-5.8.tar.xz zsh-5.8

curl -o $HOME/.zsh-install/bin/tmux -L https://github.com/tmux/tmux/releases/download/3.1b/tmux-3.1b-x86_64.AppImage

chmod +x $HOME/.zsh-install/bin/tmux

git clone https://github.com/zdharma/zinit.git ~/.zinit

ln -s -f "$term_dir/.tmux.conf"  ~/.tmux.conf

echo "source $term_dir/zshrc.zsh" >> ~/.zshrc
echo 'export PATH="$HOME/.zsh-install/bin:$PATH"' >> ~/.bashrc
