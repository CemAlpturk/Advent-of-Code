import os
import time
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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    steps = int(lines[0])

    buffer = [0]
    n = 2017
    pos = 0
    for i in range(1, n+1):
        pos = (pos + steps) % len(buffer)
        buffer = buffer[:pos+1] + [i] + buffer[pos+1:]
        pos += 1

    return buffer[pos+1]


def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    steps = int(lines[0])

    buffer = deque([0])

    for i in range(1, 50000001):
        buffer.rotate(-steps)
        buffer.append(i)

    return buffer[buffer.index(0) + 1]




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
