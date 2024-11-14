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

    gridx = 0
    gridy = 0
    for line in lines:
        x1, y1 = line.split(" -> ")[0].split(",")
        x2, y2 = line.split(" -> ")[1].split(",")

        x1, x2 = int(x1), int(x2)
        y1, y2 = int(y1), int(y2)

        if x1 > x2:
            x1, x2 = x2, x1

        if y1 > y2:
            y1, y2 = y2, y1

        gridx = max(gridx, x2)
        gridy = max(gridy, y2)

    grid = np.zeros((gridx + 1, gridy + 1), dtype=int)
    for line in lines:
        x1, y1 = line.split(" -> ")[0].split(",")
        x2, y2 = line.split(" -> ")[1].split(",")

        x1, x2 = int(x1), int(x2)
        y1, y2 = int(y1), int(y2)

        if x1 > x2:
            x1, x2 = x2, x1

        if y1 > y2:
            y1, y2 = y2, y1

        horizontal = x1 == x2
        vertical = y1 == y2

        if horizontal:
            for y in range(y1, y2 + 1):
                grid[x1, y] += 1

        elif vertical:
            for x in range(x1, x2 + 1):
                grid[x, y1] += 1

    count = (grid > 1).sum()

    print(f"Part1: {count}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    gridx = 0
    gridy = 0
    for line in lines:
        x1, y1 = line.split(" -> ")[0].split(",")
        x2, y2 = line.split(" -> ")[1].split(",")

        x1, x2 = int(x1), int(x2)
        y1, y2 = int(y1), int(y2)

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        gridx = max(gridx, x2)
        gridy = max(gridy, y2)

    grid = np.zeros((gridx + 1, gridy + 1), dtype=int)
    for line in lines:
        x1, y1 = line.split(" -> ")[0].split(",")
        x2, y2 = line.split(" -> ")[1].split(",")

        x1, x2 = int(x1), int(x2)
        y1, y2 = int(y1), int(y2)

        xs = list(range(x1, x2 + 1)) if x2 >= x1 else list(reversed(range(x2, x1 + 1)))
        ys = list(range(y1, y2 + 1)) if y2 >= y1 else list(reversed(range(y2, y1 + 1)))

        if len(xs) == 1 and len(ys) > 1:
            xs = xs * len(ys)
        elif len(ys) == 1 and len(xs) > 1:
            ys = ys * len(xs)

        for x, y in zip(xs, ys):
            grid[x, y] += 1

    count = (grid > 1).sum()

    print(f"Part2: {count}")


if __name__ == "__main__":
    part1()
    part2()
