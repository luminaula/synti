#!/usr/bin/env python3

# Copyright (c) 2021   Lumi Miettinen <luminaula@gmail.com>
# LICENSE: MIT, see LICENSE on:
# https://github.com/luminaula/synti

import sys
import socket


if len(sys.argv) != 4:
    sys.exit(1)
retval = 0
dest_ip = sys.argv[1]
dest_port = int(sys.argv[2])
timeout = int(sys.argv[3])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout)
try:
    sock.connect((dest_ip, dest_port))
except:
    print("Connection failed", file=sys.stderr)
    retval = 1

print(sock.getsockname()[1])
sys.exit(retval)