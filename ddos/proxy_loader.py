# proxy_loader.py

from typing import Dict, List
import os

PROXY_FILES = {
    "socks4": "socks4.txt",
    "socks5": "socks5.txt",
    "http": "http.txt",
    "https": "https.txt",
}

def load_proxies(args) -> Dict[str, List[str]]:
    proxies = {}

    for proxy_type, filename in PROXY_FILES.items():
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                proxy_list = [line.strip() for line in file if is_valid_proxy_format(line)]
                proxies[proxy_type] = proxy_list
                print(f"[+] Loaded {len(proxy_list)} {proxy_type.upper()} proxies.")
        else:
            proxies[proxy_type] = []
            print(f"[!] Proxy file missing: {filename}")

    return proxies


def is_valid_proxy_format(proxy: str) -> bool:
    parts = proxy.strip().split(":")
    return len(parts) == 2 and parts[0].count('.') == 3 and parts[1].isdigit()
