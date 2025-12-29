import os
import time
from itertools import combinations


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
    vals = [list(map(int,  (x for x in line.split("\t") if x))) for line in lines]

    return sum(max(row) - min(row) for row in vals)


def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals = [list(map(int, (x for x in line.split("\t") if x))) for line in lines]

    c = 0 
    for row in vals:
        for a, b in combinations(row, 2):
            a, b = max(a, b), min(a, b)
            if a % b == 0:
                c += a // b 

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
