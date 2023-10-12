#!/usr/bin/python3

"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys
import signal

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{status_code}: {count}")

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) == 6:
        status_code = int(parts[3])
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += int(parts[4])
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
