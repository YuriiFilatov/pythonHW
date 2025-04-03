#!/usr/bin/env python3
import math
import time
import os
import concurrent.futures
from multiprocessing import cpu_count

def chunk_integrate(f, a, step, start_i, end_i): 
    acc = 0.0
    for i in range(start_i, end_i):
        acc += f(a + i * step) * step 
    return acc

def integrate_parallel(f, a, b, *, n_jobs=1, n_iter=10_000_000, executor_class=concurrent.futures.ThreadPoolExecutor): 
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs 
    futures = [] 
    result_integral = 0.0

    with executor_class(max_workers=n_jobs) as executor:
        start_index = 0
        for _ in range(n_jobs):
            end_index = start_index + chunk_size
            if end_index > n_iter:
                end_index = n_iter
            futures.append(
                executor.submit(chunk_integrate, f, a, step, start_index, end_index)
            )
            start_index = end_index

        if start_index < n_iter:
            futures.append(
                executor.submit(chunk_integrate, f, a, step, start_index, n_iter)
            )

        for fut in futures:
            result_integral += fut.result()

    return result_integral
def main(): 
    cpu_num = cpu_count()
    max_n_jobs = 2 * cpu_num
    f = math.cos
    a = 0
    b = math.pi / 2

    n_iter = 10000000

    results = []
    for n_jobs in range(1, max_n_jobs + 1):
        start_thread = time.perf_counter()
        res_thread = integrate_parallel(f, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_class=concurrent.futures.ThreadPoolExecutor)
        end_thread = time.perf_counter()
        thread_time = end_thread - start_thread

        start_proc = time.perf_counter()
        res_proc = integrate_parallel(f, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_class=concurrent.futures.ProcessPoolExecutor)
        end_proc = time.perf_counter()
        proc_time = end_proc - start_proc

        results.append( (n_jobs, thread_time, proc_time) )

    with open("task2.txt", "w") as f_out:
        f_out.write(f"CPU = {cpu_num}\n")
        f_out.write("n_jobs\tThreadPool(s)\tProcessPool(s)\n")
        for n_jobs, t_time, p_time in results:
            f_out.write(f"{n_jobs}\t{t_time:.6f}\t{p_time:.6f}\n")

if __name__ == "__main__": 
    main()

