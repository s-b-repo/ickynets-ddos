from typing import Dict, List
import os
import aiofiles
import asyncio

PROXY_FILES = {
    "socks4": "socks4.txt",
    "socks5": "socks5.txt",
    "http": "http.txt",
    "https": "https.txt",
}

async def load_proxies(args) -> Dict[str, List[str]]:
    proxies: Dict[str, List[str]] = {}
    lock = asyncio.Lock()  # 🛡️ to prevent race conditions when writing to `proxies`

    async def load_proxy_file(proxy_type: str, filename: str):
        if os.path.isfile(filename):
            async with aiofiles.open(filename, mode='r') as file:
                lines = await file.readlines()
                proxy_list = [line.strip() for line in lines if is_valid_proxy_format(line)]
            async with lock:
                proxies[proxy_type] = proxy_list
            print(f"[+] Loaded {len(proxy_list)} {proxy_type.upper()} proxies.")
        else:
            async with lock:
                proxies[proxy_type] = []
            print(f"[!] Proxy file missing: {filename}")

    await asyncio.gather(*(load_proxy_file(proxy_type, filename) for proxy_type, filename in PROXY_FILES.items()))
    return proxies


def is_valid_proxy_format(proxy: str) -> bool:
    parts = proxy.strip().split(":")
    return len(parts) == 2 and parts[0].count('.') == 3 and parts[1].isdigit()
