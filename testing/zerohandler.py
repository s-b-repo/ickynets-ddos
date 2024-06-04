import aiohttp
import asyncio

async def send_request(session, url, proxy):
    async with session.get(url, proxy=proxy) as response:
        result = await response.text()
        print(f"Response from {proxy}: {result}")

async def main():
    url = "https://example.com"  # Replace with your desired URL
    payload = "your_variable"  # Replace with the variable you want to send
    proxy_type = "socks4"  # Replace with the proxy type you want to use
    port_type = "portnumber"
    file_path = "proxies.txt"  # Replace with the path to your proxies file

    proxies = []
    with open(file_path, "r") as file:
        for line in file:
            proxies.append(line.strip())

    async with aiohttp.ClientSession() as session:
        tasks = []
        for proxy in proxies:
            if proxy_type == "http":
                tasks.append(send_request(session, url, f"http://{proxy}{port_type}"))
            elif proxy_type == "socks5":
                tasks.append(send_request(session, url, f"socks5://{proxy}{port_type}"))
            else:
                tasks.append(send_request(session, url, f"socks4://{proxy}{port_type}"))
        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
