#!/usr/bin/env python3
"""reads stdin line by line and computes metrics"""

import random
import sys
import time
import datetime


def print_stats(total_file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(total_file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
counter = 0
code = 0
try:
    for line in sys.stdin:
        parsed_state = line.split()
        parsed_state = parsed_state[::-1]
        if len(parsed_state) > 2:
            counter += 1
            if counter <= 10:
                total_file_size += int(parsed_state[0])
                code = parsed_state[1]
                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if counter == 10:
                print_stats(total_file_size, status_codes)
                counter = 0
finally:
    print_stats(total_file_size, status_codes)
