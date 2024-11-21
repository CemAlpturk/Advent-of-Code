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


def fold_y(paper: np.ndarray, i: int) -> np.ndarray:

    p1 = paper[:i, :]
    p2 = paper[i + 1 :, :]

    return np.logical_or(p1, p2[::-1, :])


def fold_x(paper: np.ndarray, i: int) -> np.ndarray:

    p1 = paper[:, :i]
    p2 = paper[:, i + 1 :]

    return np.logical_or(p1[:, ::-1], p2)


def print_paper(paper: np.ndarray) -> None:
    for i in range(paper.shape[0]):
        s = ""
        for j in range(paper.shape[1]):
            s += "#" if paper[i, j] else "_"

        print(s)


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    dots = []
    instructions = []
    for i, line in enumerate(lines):
        if line == "":
            break
        x, y = line.split(",")
        dots.append((int(x), int(y)))

    for line in lines[i + 1 :]:
        axis, val = line[11:].split("=")
        instructions.append((axis, int(val)))

    # Find paper bounds
    max_x = max(p[0] for p in dots)
    max_y = max(p[1] for p in dots)

    paper = np.zeros((max_y + 1, max_x + 1), dtype=np.bool_)
    for x, y in dots:
        paper[y, x] = True

    for i, (axis, n) in enumerate(instructions):
        if axis == "x":
            paper = fold_x(paper, n)
        else:
            paper = fold_y(paper, n)

        # print(f"{i+1}: {paper.sum()}")
        break

    val = paper.sum()
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    dots = []
    instructions = []
    for i, line in enumerate(lines):
        if line == "":
            break
        x, y = line.split(",")
        dots.append((int(x), int(y)))

    for line in lines[i + 1 :]:
        axis, val = line[11:].split("=")
        instructions.append((axis, int(val)))

    # Find paper bounds
    max_x = max(p[0] for p in dots)
    max_y = max(p[1] for p in dots)

    paper = np.zeros((max_y + 1, max_x + 1), dtype=np.bool_)
    for x, y in dots:
        paper[y, x] = True

    for i, (axis, n) in enumerate(instructions):
        if axis == "x":
            paper = fold_x(paper, n)
        else:
            paper = fold_y(paper, n)

    print_paper(paper[:, ::-1])

    val = 0
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
