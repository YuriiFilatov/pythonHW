#!/usr/bin/env python3 
import multiprocessing 
import time 
import sys 
import codecs 
import threading


def processA(q_in, q_to_B): 
    while True: 
        msg = q_in.get() 
        msg_lower = msg.lower()
        q_to_B.put(msg_lower)
        time.sleep(5)


def processB(q_from_A, q_out_B): 
    while True:
        msg = q_from_A.get()
        encoded = codecs.encode(msg, 'rot_13')
        print(f"{encoded}") 
        q_out_B.put(encoded)


def input_thread(q_in_A): 
    while True:
        line = sys.stdin.readline()
        if not line:
            break 
        line = line.strip() 
        q_in_A.put(line)

        
def output_thread(q_out_B):
    while True: 
        encoded_msg = q_out_B.get()


def main():
    q_in_A = multiprocessing.Queue()
    q_A_B = multiprocessing.Queue()
    q_out_B = multiprocessing.Queue()
    pA = multiprocessing.Process(target=processA, args=(q_in_A, q_A_B))
    pB = multiprocessing.Process(target=processB, args=(q_A_B, q_out_B))
    pA.start()
    pB.start()
    t_in = threading.Thread(target=input_thread, args=(q_in_A, ), daemon=True)
    t_out = threading.Thread(target=output_thread, args=(q_out_B, ), daemon=True)
    t_in.start()
    t_out.start()
    try:
        while t_in.is_alive():
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    pA.terminate()
    pB.terminate()
    pA.join()
    pB.join()

if __name__ == "__main__": 
    main()

