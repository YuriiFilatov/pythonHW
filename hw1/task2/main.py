#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) == 1:
        lines = sys.stdin.read().splitlines() 
        for line in lines[-17:]:
            print(line) 
    else:
        num_files = len(sys.argv) - 1 
        for i, filename in enumerate(sys.argv[1:], start=1): 
            if num_files != 1:
                print(f"==> {filename} <==")
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines() 
                for line in lines[-10:]:
                    print(line)
                if i < num_files:
                    print()

if __name__ == "__main__": 
    main()
