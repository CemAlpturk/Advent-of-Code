import os
import time
import math


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
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = int(lines[0])
    
    return 1 + 2 * (n - 2**(math.floor(math.log2(n))))

def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = int(lines[0])
    w = 1 
    for i in range(1, n):
        w = w % i + 1
        if w > (i + 1)/2:
            w += 1 

    return w




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
