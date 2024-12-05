import os
import time
import numpy as np


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
    count = 0
    n, m = grid.shape
    word = "XMAS"
    nw = len(word)
    for i in range(n):
        for j in range(m):
            row = "".join(grid[i, j : j + nw])
            col = "".join(grid[i : i + nw, j])

            if row == word or row[::-1] == word:
                count += 1

            if col == word or col[::-1] == word:
                count += 1

            if i <= n - nw and j <= m - nw:
                diag = (
                    grid[i, j]
                    + grid[i + 1, j + 1]
                    + grid[i + 2, j + 2]
                    + grid[i + 3, j + 3]
                )
                if diag == word or diag[::-1] == word:
                    count += 1

            if i <= n - nw and j >= nw - 1:
                diag = (
                    grid[i, j]
                    + grid[i + 1, j - 1]
                    + grid[i + 2, j - 2]
                    + grid[i + 3, j - 3]
                )
                if diag == word or diag[::-1] == word:
                    count += 1

    return count


def check_block(block: np.ndarray, word: str) -> int:
    n, m = block.shape
    assert n == m
    assert n == len(word)

    diag1 = ""
    diag2 = ""

    for i in range(n):
        diag1 += block[i, i]
        diag2 += block[i, -i - 1]

    count = 0
    if (diag1 == word or diag1[::-1] == word) and (
        diag2 == word or diag2[::-1] == word
    ):
        count += 1

    return count


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    count = 0
    n, m = grid.shape
    word = "MAS"
    nw = len(word)

    for i in range(n - nw + 1):
        for j in range(m - nw + 1):
            block = grid[i : i + nw, j : j + nw]
            count += check_block(block, word)

    return count


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
