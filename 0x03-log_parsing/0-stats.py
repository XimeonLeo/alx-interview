#!/usr/bin/python3
""" This module contains a script that reads
    stdin line by line and computes metrics
    """
import sys

possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_num = 0
status_codes_map = {}
total_file_size = 0


def print_stats():
    """prints out the statistics"""
    print("File size: {}".format(total_file_size))
    for status, count in sorted(status_codes_map.items()):
        print("{}: {}".format(status, count))


try:
    for line in sys.stdin:
        line_tokens = line.split()
        try:
            file_size = int(line_tokens[-1])
            total_file_size += file_size
            status_code = int(line_tokens[-2])
            if status_code in possible_status_codes:
                if status_code in status_codes_map:
                    status_codes_map[status_code] += 1
                else:
                    status_codes_map[status_code] = 1
        except ValueError:
            pass
        line_num += 1
        if line_num % 10 == 0:
            print_stats()

    if (line_num == 0) or (line_num % 10 != 0):
        print_stats()

except (KeyboardInterrupt):
    print_stats()
