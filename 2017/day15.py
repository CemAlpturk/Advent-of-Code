import os
import time
from tqdm import tqdm


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


def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)

    prevA = 289
    prevB = 629

    kA = 16807
    kB = 48271

    r = 2147483647
    n = 40000000 

    c = 0 
    for _ in tqdm(range(n)):
        xA = (prevA * kA) % r 
        xB = (prevB * kB) % r 

        c += (xA & 0xFFFF) == (xB & 0xFFFF)
        prevA = xA 
        prevB = xB 

    return c


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)
    xA = 289
    xB = 629

    kA = 16807
    kB = 48271

    r = 2147483647
    n = 5000000

    c = 0 
    for _ in tqdm(range(n)):
        xA = (xA * kA) % r 
        while xA % 4 != 0:
            xA = (xA * kA) % r 
        xB = (xB * kB) % r 
        while xB % 8 != 0:
            xB = (xB * kB) % r 

        c += (xA & 0xFFFF) == (xB & 0xFFFF)

    return c


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
