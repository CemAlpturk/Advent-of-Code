import os
import time
from typing import Callable
from functools import reduce


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


def circular_apply(
    xs: list[int],
    start: int,
    length: int,
    fn: Callable[[list[int]], list[int]],
) -> None:

    n = len(xs)
    if n == 0 or length == 0:
        return 

    idxs = [(start + i) % n for i in range(length)]
    chunk = [xs[i] for i in idxs]
    new_chunk = fn(chunk)
    if len(new_chunk) != len(chunk):
        raise ValueError 

    for i, v in zip(idxs, new_chunk):
        xs[i] = v 

    

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    lengths = list(map(int, lines[0].split(",")))
    n = 256
    xs = list(range(n))
    current_pos = 0 
    skip_size = 0 

    def fn(vals: list[int]) -> list[int]:
        return vals[::-1]

    for l in lengths:
        circular_apply(xs, current_pos, l, fn)
        current_pos += l + skip_size 
        current_pos %= n 
        skip_size += 1 

    return xs[0] * xs[1]
        

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    s = lines[0].strip(" ")
    lengths = [ord(c) for c in s]
    lengths += [17, 31, 73, 47, 23]

    n = 256 
    k = 64 
    xs = list(range(n))
    current_pos = 0
    skip_size = 0 

    def fn(vals: list[int]) -> list[int]:
        return vals[::-1]

    for _ in range(k):
        for l in lengths:
            circular_apply(xs, current_pos, l ,fn)
            current_pos += l + skip_size 
            current_pos %= n 
            skip_size += 1 

    hsh = ""
    for i in range(16):
        start = i * 16  
        stop = start + 16 

        val = reduce(lambda x, y: x ^ y, xs[start:stop], 0)
        h = hex(val).replace("0x", "")
        if len(h) == 1:
            h = "0" + h 
        hsh += h

    return hsh





if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
