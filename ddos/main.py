# main.py

from parser import parse_arguments
from attack_launcher import launch_attack
from proxy_loader import load_proxies

def main():
    args = parse_arguments()

    # Optional: Load proxies
    proxies = []
    if args.use_proxy:
        proxies = load_proxies(args)

    # Launch the actual attack
    launch_attack(args, proxies)

if __name__ == "__main__":
    main()
