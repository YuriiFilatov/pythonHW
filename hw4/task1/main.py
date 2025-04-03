#!/usr/bin/env python3

import time 
import threading 
import multiprocessing

def fib(n):
    if n < 2: 
        return n 
    return fib(n-1) + fib(n-2)

def measure_synchronous(n, repeats=10):
    start = time.time() 
    for _ in range(repeats): 
        fib(n) 
    end = time.time() 
    return end - start

def measure_threads(n, repeats=10):
    threads = []
    start = time.time()
    for _ in range(repeats): 
        t = threading.Thread(target=fib, args=(n,)) 
        threads.append(t)
    for t in threads: 
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start

def measure_processes(n, repeats=10):
    processes = []
    start = time.time()
    for _ in range(repeats):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start

def main():
    n = 33
    sync_time = measure_synchronous(n)
    thread_time = measure_threads(n)
    process_time = measure_processes(n)
    with open("task1.txt", "w") as f:
        f.write(f"Nothing: {sync_time:.4f}\n")
        f.write(f"Threading: {thread_time:.4f}\n")
        f.write(f"Multiprocessing: {process_time:.4f}\n")

if __name__ == "__main__": 
    main()