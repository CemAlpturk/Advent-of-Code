import os
import numpy as np


def read_input(filename: str) -> list[str]:

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip("\n") for line in lines]


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    # Parse matrix
    n = len(lines)
    m = len(lines[0])
    heights = np.zeros((n, m), dtype=int)
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            heights[i, j] = int(v)
    heights = np.pad(heights, (1, 1), "constant", constant_values=(10, 10))

    risk = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            up = heights[i - 1, j]
            down = heights[i + 1, j]
            left = heights[i, j - 1]
            right = heights[i, j + 1]

            val = heights[i, j]

            if val < min(up, down, left, right):
                risk += val + 1

    val = risk
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    # Parse matrix
    n = len(lines)
    m = len(lines[0])
    heights = np.zeros((n, m), dtype=int)
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            heights[i, j] = int(v)
    heights = np.pad(heights, (1, 1), "constant", constant_values=(10, 10))

    basins = np.zeros_like(heights)
    # basins[heights >= 9] = -1

    visited = set()
    cluster_num = 0

    def dfs(x, y):
        if (x, y) in visited or heights[x, y] >= 9:
            return

        basins[x, y] = cluster_num
        visited.add((x, y))

        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) in visited or heights[i, j] >= 9:
                continue
            cluster_num += 1
            dfs(i, j)

    n_basins = np.max(basins)

    basin_sizes = [np.sum(basins == i) for i in range(1, n_basins + 1)]
    basin_sizes.sort()

    val = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
