#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys

possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
read = 0
status_code = {}
file_size = 0


def print_stats():
    """prints out the statistics"""
    print("File size: {}".format(file_size))
    for status, count in sorted(status_code.items()):
        print("{}: {}".format(status, count))


try:
    for line in sys.stdin:
        line_tokens = line.split()
        try:
            file_size += int(line_tokens[-1])  # Update file_size
            status = int(line_tokens[-2])  # Store status temporarily
            if status in possible_status_codes:
                if status in status_code:
                    status_code[status] += 1
                else:
                    status_code[status] = 1
        except ValueError:
            pass
        read += 1
        if read % 10 == 0:
            print_stats()

    if read == 0 or read % 10 != 0:
        print_stats()

except KeyboardInterrupt:
    print_stats()

