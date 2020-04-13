#!/bin/sh

sudo apt update

# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"

# zsh including set as default
# sudo apt install zsh -y
# echo "if [ -t 1 ]; then exec zsh fi" >> ~/.bashrc
# sudo apt install powerline fonts-powerline -y
# git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
# replace ZSH_THEME in .zshrc with ZSH_THEME="agnoster"
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$HOME/.zsh-syntax-highlighting" --depth 1
# echo "source $HOME/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> "$HOME/.zshrc"
# source ~/.zshrc

# ssh
# ls -al ~/.ssh
# echo "Did this show nothing? in that case run following"
# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# eval $(ssh-agent -s)
# ssh-add ~/.ssh/id_rsa
# sudo apt install xclip
# xclip -sel clip < ~/.ssh/id_rsa.pub

# anaconda
# cd ~/Downloads
# wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
# bash Anaconda3-2020.02-Linux-x86_64.sh
# bash --login
# which python
# cd ~

# julia
# cd ~/Downloads
# wget https://julialang-s3.julialang.org/bin/linux/x64/1.4/julia-1.4.0-linux-x86_64.tar.gz
# tar -xvzf julia-1.4.0-linux-x86_64.tar.gz
# sudo cp -r julia-1.4.0 /opt/
# sudo ln -s /opt/julia-1.4.0/bin/julia /usr/local/bin/julia
# julia -version
# cd ~

# rust
# sudo curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# java 1.8
# sudo apt install openjdk-8-jre
