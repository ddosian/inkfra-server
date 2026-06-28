import environment

import socket
import ipaddress

def dns_lookup(hostname):
    if not hostname:
        return None

    try:
        ipaddress.ip_address(hostname)
        return hostname
    except ValueError:
        pass

    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return hostname
    
class log:
    def info(message):
        print(f"[INFO] {message}")
    def warning(message):
        print(f"[WARNING] {message}")
    def error(message):
        print(f"[ERROR] {message}")
    def debug(message):
        if environment.DEBUG.lower() == 'true':
            print(f"[DEBUG] {message}")
    