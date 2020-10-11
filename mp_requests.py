import multiprocessing as mp
import time

import requests


def foo(q):
    while True:
        r = requests.get("https://google.ru")
        print("proc2", r.status_code)
        time.sleep(1)


def check():
    while True:
        r = requests.get("https://ya.ru")
        print("proc1", r.status_code)
        time.sleep(1)


if __name__ == "__main__":
    mp.set_start_method("spawn")
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    check()
