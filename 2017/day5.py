import os
import time


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
    vals = list(map(int, lines))
    
    n = len(vals)
    i = 0 
    steps = 0 

    while 0 <= i < n:
        j = i + vals[i]
        vals[i] += 1 
        steps += 1 
        i = j 

    return steps


def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals = list(map(int, lines))

    n = len(vals)
    i = 0 
    steps = 0 

    while 0 <= i < n:
        j = i + vals[i] 
        if vals[i] >= 3:
            vals[i] -= 1 
        else:
            vals[i] += 1 
        steps += 1 
        i = j 
    
    return steps


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
