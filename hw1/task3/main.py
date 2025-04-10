#!/usr/bin/env python3
import sys

def count_stats_from_bytes(data: bytes):
    lines = data.count(b'\n')
    words = len(data.split())
    bytes_count = len(data)
    return lines, words, bytes_count


def main():
    if len(sys.argv) == 1: 
        data = sys.stdin.buffer.read() 
        lines, words, bytes_count = count_stats_from_bytes(data)
        print(f"{lines:7d} {words:7d} {bytes_count:7d}") 
    else: 
        total_lines = 0 
        total_words = 0 
        total_bytes = 0
    for filename in sys.argv[1:]:
        with open(filename, 'rb') as f:
            data = f.read()
        lines, words, bytes_count = count_stats_from_bytes(data)
        total_lines += lines
        total_words += words
        total_bytes += bytes_count
        print(f"{lines:7d} {words:7d} {bytes_count:7d} {filename}")

    if len(sys.argv) > 2:
        print(f"{total_lines:7d} {total_words:7d} {total_bytes:7d} total")


if __name__ == "__main__": 
    main()