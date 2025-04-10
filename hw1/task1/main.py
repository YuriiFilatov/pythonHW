#!/usr/bin/env python3 
import sys
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1] 
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    else: 
        lines = sys.stdin.readlines()
    line_number = 1
    for line in lines:
        clean_line = line.rstrip('\n')
        print(f"{line_number}\t{clean_line}")
        line_number += 1

if __name__ == "__main__":
    main()