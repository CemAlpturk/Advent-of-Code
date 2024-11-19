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


def get_neighbors(i: int, j: int, n: int, m: int) -> list[tuple[int, int]]:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 1),
        (1, -1),
        (1, 0),
    ]
    neighbors = []

    for x, y in directions:
        r = x + i
        c = y + j

        if 0 <= r < n and 0 <= c < m:
            neighbors.append((r, c))

    return neighbors


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    n = len(lines)
    m = len(lines[0])
    grid = np.zeros((n, m), dtype=int)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = int(c)

    flashes = 0
    n_steps = 100
    for step in range(n_steps):
        flashed = np.zeros_like(grid, dtype=np.bool_)
        grid += 1
        cont = True
        while cont:
            cont = False
            for i in range(n):
                for j in range(m):
                    if grid[i, j] > 9 and not flashed[i, j]:
                        cont = True
                        flashed[i, j] = True
                        flashes += 1

                        for x, y in get_neighbors(i, j, n, m):
                            grid[x, y] += 1

        grid[flashed] = 0

    val = flashes
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    grid = np.zeros((n, m), dtype=int)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = int(c)

    n_steps = 10000
    flash_step = -1
    for step in range(1, n_steps + 1):
        flashed = np.zeros_like(grid, dtype=np.bool_)
        grid += 1
        cont = True
        while cont:
            cont = False
            for i in range(n):
                for j in range(m):
                    if grid[i, j] > 9 and not flashed[i, j]:
                        cont = True
                        flashed[i, j] = True

                        for x, y in get_neighbors(i, j, n, m):
                            grid[x, y] += 1

        if np.all(flashed):
            flash_step = step
            break
        grid[flashed] = 0

    val = flash_step
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
