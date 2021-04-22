mkdir -p ~/.config/nvim

git clone https://github.com/PokemonWei/nvim-configuration.git $ALL_DEV_ENV/nvim-configuration

if [ ! -f "~/.config/nvim/init.vim" ]; then
	echo "source $ALL_DEV_ENV/nvim-configuration/init.vim" >> ~/.config/nvim/init.vim
    echo "create init.vim for nvim"
fi
