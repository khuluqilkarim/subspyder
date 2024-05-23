#!/bin/bash

wget https://go.dev/dl/go1.22.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.22.3.linux-amd64.tar.gz

echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bash_profile
source ~/.bash_profile

rm go1.22.3.linux-amd64.tar.gz

if command -v go &> /dev/null
then
    go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

    sudo ln -s ~/go/bin/subfinder /usr/local/bin/subfinder

    echo -e "\e[32mGo and Subfinder installation success!\e[0m"
else
    echo -e "\e[31mFailed to install Go. Please check your internet connection and try again.\e[0m"
fi
