term_dir=$(dirname $(readlink -f "$0"))

ln -s -f "$term_dir/.tmux.conf"  /etc/tmux.conf

git clone https://github.com/tmux-plugins/tpm /root/.tmux/plugins/tpm && /root/.tmux/plugins/tpm/bin/install_plugins

echo "source $term_dir/zshrc.zsh" >> /etc/zsh/zshrc

git clone https://github.com/zdharma/zinit.git ~/.zinit

zsh

exit