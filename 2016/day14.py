import os
import time
import hashlib
from functools import cache
from collections import deque


def read_input(filename: str) -> list[str]:
    dir = os.path.basename(__file__).split(".")[0]

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "data",
            dir,
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip("\n") for line in lines]

@cache
def get_hash(salt: str, idx: int, k: int = 1) -> str:
    s = salt + str(idx)
    for _ in range(k):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

@cache
def has_repeating(h: str, n: int) -> str | None:
    prev = None 
    count = 0 

    for ch in h:
        if ch == prev:
            count += 1 
        else:
            prev = ch 
            count = 1 

        if count == n:
            return ch 

    return None

@cache 
def has_repeating_val(h: str, n: int, c: str) -> bool:
    target = c * n
    for i in range(len(h) - n + 1):
        if h[i:i+n] == target:
            return True
    return False


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    salt = lines[0]
    c = 0
    idx = 0
    while True: 
        h = get_hash(salt, idx)
        a = has_repeating(h, 3)
        if a:
            for i in range(1000):
                h_i = get_hash(salt, idx + i + 1)
                if has_repeating_val(h_i, 5, a):
                    c += 1 
                    if c == 64:
                        return idx 
                    break 

        idx += 1 



def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    salt = lines[0]
    c = 0
    idx = 0
    while True: 
        h = get_hash(salt, idx, 2017)
        a = has_repeating(h, 3)
        if a:
            for i in range(1000):
                h_i = get_hash(salt, idx + i + 1, 2017)
                if has_repeating_val(h_i, 5, a):
                    c += 1
                    if c == 64:
                        return idx 
                    break 

        idx += 1 




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
