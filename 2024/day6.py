import os
import time
import numpy as np
from tqdm import tqdm


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
    visited = np.zeros_like(grid, dtype=bool)
    start_pos = tuple(map(lambda x: x.item(), np.where(grid == "^")))
    # visited[*start_pos] = True
    dir_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }

    move_dir = (-1, 0)

    n, m = grid.shape
    pos = start_pos

    while True:
        visited[*pos] = True

        # Update movement
        next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])

        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            # Out of bounds
            break

        if grid[*next_pos] == "#":
            # Rotate
            move_dir = dir_map[move_dir]

        else:
            pos = next_pos

    return np.sum(visited)


def is_loop(
    grid: np.ndarray,
    start: tuple[int, int],
    dir: tuple[int, int],
    dir_map: dict,
) -> bool:
    visited = set()
    # visited.add((start, dir))

    n, m = grid.shape
    pos = start

    while True:
        if (pos, dir) in visited:
            return True

        visited.add((pos, dir))

        next_pos = (pos[0] + dir[0], pos[1] + dir[1])

        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            return False

        if grid[*next_pos] == "#":
            dir = dir_map[dir]
        else:
            pos = next_pos


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    start_pos = tuple(map(lambda x: x.item(), np.where(grid == "^")))
    dir_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
    }

    move_dir = (-1, 0)

    candidates = [(x.item(), y.item()) for x, y in zip(*np.where(grid == "."))]

    count = 0

    for candidate in tqdm(candidates):
        modified_grid = grid.copy()
        modified_grid[*candidate] = "#"

        count += int(is_loop(modified_grid, start_pos, move_dir, dir_map))

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
