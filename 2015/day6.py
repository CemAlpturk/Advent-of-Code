import os
import time

import numpy as np


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

    n = 1000 
    grid = np.zeros((n, n), dtype=bool)

    for line in lines:
        words = line.split(" ") 

        if words[0] == "turn":
            command = words[1] == "on"

            p1 = tuple(map(int, words[2].split(",")))
            p2 = tuple(map(int, words[-1].split(",")))

            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] = command 
        else:
            p1 = tuple(map(int, words[1].split(",")))
            p2 = tuple(map(int, words[-1].split(",")))

            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] = np.logical_not(grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1])

    return int(np.sum(grid))


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    n = 1000 
    grid = np.zeros((n, n), dtype=int)

    for line in lines:
        words = line.split(" ") 

        if words[0] == "turn":
            command = 1 if words[1] == "on" else -1 

            p1 = tuple(map(int, words[2].split(",")))
            p2 = tuple(map(int, words[-1].split(",")))

            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] += command
            grid = np.maximum(grid, 0)


        else:
            p1 = tuple(map(int, words[1].split(",")))
            p2 = tuple(map(int, words[-1].split(","))) 

            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] += 2 

    return int(np.sum(grid))


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
