# SUBSPYDER

SubSpyder is a simple tool designed to assist users in finding subdomains of a website. This tool combines the results from popular subdomain search tools, such as Subfinder, with information gathered from Certificate Fingerprint searches.

By using SubSpyder, users can easily discover additional subdomains associated with a domain, which can aid in system security management, penetration testing, or web infrastructure monitoring.


# Installation 

```bash
git clone https://github.com/khuluqilkarim/subspyder.git
cd subspyder
sudo pip install .
```

You can use this to install Golang on your OS.
```bash
chmod +x install_go.sh
./install_go.sh
```
add this in your bashrc or zshrc 

```bash
export PATH=$PATH:/usr/local/go/bin
```
Reload your shell configuration to apply the changes:
```bash
source ~/.bashrc
```
# Usage 

```bash
subspyder -u domain.com
```

# Support 
If you find SubSpyder helpful, consider supporting its development: [trakteer.id](https://trakteer.id/khuluqilkarim/tip)