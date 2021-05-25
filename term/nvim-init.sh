mkdir -p ~/.config/nvim

git clone https://github.com/PokemonWei/nvim-configuration.git ~/tool/nvim-configuration

if [ ! -f "~/.config/nvim/init.vim" ]; then
	echo "source ~/tool/nvim-configuration/init.vim" >> ~/.config/nvim/init.vim
    nvim +PlugInstall +qall
    echo "create init.vim for nvim"
fi
