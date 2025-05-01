# parser.py

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Refactored MHDDoS Tool")

    parser.add_argument("method", help="Attack method (e.g., UDP, TCP, GET, POST)")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("threads", type=int, help="Number of threads to use")
    parser.add_argument("--duration", type=int, default=60, help="Attack duration in seconds")
    parser.add_argument("--use-proxy", action="store_true", help="Use proxies (for L7)")

    return parser.parse_args()
