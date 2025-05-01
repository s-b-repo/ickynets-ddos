# attack_launcher.py

from config import LAYER4_METHODS, LAYER7_METHODS
from methods.layer4 import run_layer4_attack
from methods.layer7 import run_layer7_attack

def launch_attack(args, proxies):
    method = args.method.upper()

    if method in LAYER4_METHODS:
        print(f"[+] Launching Layer 4 attack: {method}")
        run_layer4_attack(args)
    elif method in LAYER7_METHODS:
        print(f"[+] Launching Layer 7 attack: {method}")
        run_layer7_attack(args, proxies)
    else:
        print(f"[!] Unknown method: {method}")
