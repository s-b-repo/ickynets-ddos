import asyncio
from parser import parse_arguments
from attack_launcher import launch_attack
from proxy_loader import load_proxies

async def main():
    args = parse_arguments()

    # Load proxies (async)
    proxies = []
    if args.use_proxy:
        proxies = await load_proxies(args)

    # Launch the attack (async)
    await launch_attack(args, proxies)

if __name__ == "__main__":
    asyncio.run(main())
