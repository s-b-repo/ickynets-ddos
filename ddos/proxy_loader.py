# proxy_loader.py

from typing import List
import os

def load_proxies(args) -> List[str]:
    proxy_file = "proxies.txt"
    proxies = []

    if not os.path.isfile(proxy_file):
        print(f"[!] Proxy file '{proxy_file}' not found.")
        return []

    with open(proxy_file, "r") as file:
        for line in file:
            proxy = line.strip()
            if proxy and is_valid_proxy_format(proxy):
                proxies.append(proxy)

    if not proxies:
        print("[!] No valid proxies found.")
    else:
        print(f"[+] Loaded {len(proxies)} proxies.")

    return proxies


def is_valid_proxy_format(proxy: str) -> bool:
    parts = proxy.split(":")
    return len(parts) == 2 and all(part.strip().isdigit() or "." in part for part in parts)
