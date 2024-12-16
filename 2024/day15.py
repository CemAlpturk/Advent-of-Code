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


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def move_obj(
    grid: np.ndarray, pos: tuple[int, int], dir: tuple[int, int]
) -> tuple[bool, np.ndarray, tuple[int, int]]:
    new_pos = add(pos, dir)
    if grid[*new_pos] == "#":
        return False, grid, pos

    if grid[*new_pos] == ".":
        grid[*new_pos] = grid[*pos]
        grid[*pos] = "."
        return True, grid, new_pos

    flag, grid, _ = move_obj(grid, new_pos, dir)
    if flag:
        grid[*new_pos] = grid[*pos]
        grid[*pos] = "."
        return True, grid, new_pos

    return False, grid, pos


def simulate(grid: np.ndarray, moves: list[str]) -> np.ndarray:
    pos = [(x.item(), y.item()) for x, y in zip(*np.where(grid == "@"))][0]

    DIRS = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }

    for move in moves:
        dir = DIRS[move]
        _, grid, pos = move_obj(grid, pos, dir)

    return grid


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid_str, moves_str = lines.split("\n\n")

    grid = np.array(
        [[v for v in line.strip()] for line in grid_str.split("\n") if line]
    )
    moves = [move for move in moves_str if move != "\n"]

    grid = simulate(grid, moves)

    boxes = [(x.item(), y.item()) for x, y in zip(*np.where(grid == "O"))]

    return sum(100 * x + y for x, y in boxes)


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
