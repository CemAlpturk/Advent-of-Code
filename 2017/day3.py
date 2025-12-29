import os
import time
import math
from functools import cache


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
def get_coords(n: int) -> tuple[int, int]:
    if n == 1:
        return (0, 0)

    k = math.ceil((math.sqrt(n) - 1) / 2)
    side_len = 2 * k 
    max_val = (2 * k + 1) ** 2
    offset = max_val - n 

    if offset < side_len:
        x = k - offset 
        y = -k 

    elif offset < 2 * side_len:
        x = -k 
        y = -k + (offset - side_len)

    elif offset < 3 * side_len:
        x = -k + (offset - 2 * side_len)
        y = k

    else:
        x = k
        y = k - (offset - 3 * side_len)

    return x,y


    


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = int(lines[0])

    x, y = get_coords(n)
    return abs(x) + abs(y)



def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    n = int(lines[0])

    i = 2
    vals = {}
    vals[(0, 0)] = 1 
    
    while True:
        x, y = get_coords(i)
        d = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]

        c = sum(vals[di] for di in d if di in vals)
        vals[(x, y)] = c 
        if c >= n:
            return c 
        i += 1


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
