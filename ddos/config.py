# config.py (updated with new LAYER7_METHODS)

# === Layer 4 Methods ===
LAYER4_METHODS = [
    "TCP", "UDP", "SYN", "ICMP", "CPS", "CONNECTION",
    "VSE", "TS3", "FIVEM", "MEM", "DNS", "CHAR",
    "CLDAP", "ARD", "RDP", "MINECRAFT", "MCPE", "MCBOT"
]

# === Layer 7 Methods (Extended) ===
LAYER7_METHODS = [
    "GET", "POST", "OVH", "OVH:RHEX", "RHEX", "OVH-STOMP", "STOMP",
    "STRESS", "DYN", "DOWNLOADER", "SLOW", "HEAD", "NULL",
    "COOKIE", "PPS", "EVEN", "GSB", "DGB", "AVB", "BOT",
    "APACHE", "XMLRPC", "CFB", "CFBUAM", "BYPASS", "BOMB",
    "KILLER", "TOR",

    # Newly added methods:
    "CF-BYPASS", "DDOS", "XBOMB", "JUNK", "BIGUA", "CACHEBUSTER",
    "RNDQUERY", "POSTSPAM", "INVALIDHDR", "BROWSERMIX", "PATHBOMB",
    "MIXEDMETHOD", "REFERERSPAM", "CUSTOMHDRBOMB", "JSONSPAM",
    "UAFLOOD", "METHODFUZZ", "RANDENCODING", "RANGESPLIT", "ACCEPTOVERLOAD"
]

# === File Defaults ===
DEFAULT_PROXY_FILE = "proxies.txt"
