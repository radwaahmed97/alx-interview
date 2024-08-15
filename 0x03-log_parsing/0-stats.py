#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys


total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
counter = 0

try:
    for line in sys.stdin:
        parsed_state = line.split(" ")
        if len(parsed_state) > 2:
            status_line = parsed_state[-2]
            file_size = parsed_state[-1]
            if status_line in status_codes:
                status_codes[status_line] += 1
            total_file_size += int(file_size)
            counter += 1
            if counter == 10:
                print("File size: {:d}".format(total_file_size))
                keys_sorted = sorted(status_codes.keys())
                for key in keys_sorted:
                    val = status_codes[key]
                    if val != 0:
                        print("{}: {}".format(key, val))
                counter = 0
except Exception:
    pass
finally:
    print("File size: {:d}".format(total_file_size))
    keys_sorted = sorted(status_codes.keys())
    for key in keys_sorted:
        val = status_codes[key]
        if val != 0:
            print("{}: {}".format(key, val))
