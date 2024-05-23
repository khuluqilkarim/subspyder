import subprocess
import requests
import re
import argparse
import shutil
import sys
import os

import subprocess

def install_subfinder():
    try:
        print("\033[93mSubfinder is not installed. Installing...\033[0m")
        subprocess.run(['go', 'install', '-v', 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest'], check=True)
        print("\033[92mSubfinder installed successfully.\033[0m")
        print("Reload your terminal")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing subfinder: {e}")


def get_subdomains(address):
    try:
        result = subprocess.run(['subfinder', '-silent', '-nc', '-d', address], capture_output=True, text=True, check=True)
        subfinder_output = result.stdout.splitlines()
        subfinder_domains = {domain.strip() for domain in subfinder_output}

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(f'https://crt.sh/?q={address}', headers=headers)
        response.raise_for_status()

        pattern = re.compile(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        matches = pattern.findall(response.text)

        crt_domains = {match for match in matches if match.endswith(address)}

        combined_domains = subfinder_domains.union(crt_domains)

        print(f"Combined and sorted subdomains for {address}:\n")
        for domain in sorted(combined_domains):
            print(domain)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running subfinder: {e}")
    except FileNotFoundError:
        print("Subfinder is not installed. Attempting to install...")
        install_subfinder()
    except requests.RequestException as e:
        print(f"Error occurred while fetching the URL: {e}")

def main():
    parser = argparse.ArgumentParser(description='Process a URL to find subdomains.')
    parser.add_argument('-u', '--url', type=str, required=True, help='URL to process')
    args = parser.parse_args()

    get_subdomains(args.url)

if __name__ == "__main__":
    main()
