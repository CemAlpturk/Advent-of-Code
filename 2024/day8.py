import os
import time
import numpy as np
from itertools import combinations


def read_input(filename: str) -> str:
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
        data = f.read()

    return data


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    n, m = grid.shape
    antennas = [(x.item(), y.item()) for x, y in zip(*np.where(grid != "."))]

    antinodes = set()

    for a1, a2 in combinations(antennas, 2):
        if grid[*a1] != grid[*a2]:
            continue

        dx = a2[0] - a1[0]
        dy = a2[1] - a1[1]

        ant1 = (a2[0] + dx, a2[1] + dy)
        ant2 = (a1[0] - dx, a1[1] - dy)
        for x, y in (ant1, ant2):
            if 0 <= x < n and 0 <= y < m:
                antinodes.add((x, y))

    return len(antinodes)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    n, m = grid.shape
    antennas = [(x.item(), y.item()) for x, y in zip(*np.where(grid != "."))]

    antinodes = set()

    for a1, a2 in combinations(antennas, 2):
        if grid[*a1] != grid[*a2]:
            continue

        dx = a2[0] - a1[0]
        dy = a2[1] - a1[1]

        k = 0
        while True:
            _dx = k * dx
            _dy = k * dy
            ant1 = (a2[0] + _dx, a2[1] + _dy)
            ant2 = (a1[0] - _dx, a1[1] - _dy)
            c = 0
            for x, y in (ant1, ant2):
                if 0 <= x < n and 0 <= y < m:
                    antinodes.add((x, y))
                else:
                    c += 1
            k += 1

            if c == 2:
                break

    return len(antinodes)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
