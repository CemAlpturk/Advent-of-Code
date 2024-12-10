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


def grid_to_graph(grid: np.ndarray) -> dict[tuple[int, int], list[tuple[int, int]]]:
    n, m = grid.shape
    graph = {}
    for i in range(n):
        for j in range(m):
            pos = (i, j)
            v = grid[*pos]
            graph[pos] = []

            if i > 0:
                graph[pos].append((i - 1, j))

            if i < n - 1:
                graph[pos].append((i + 1, j))

            if j > 0:
                graph[pos].append((i, j - 1))

            if j < m - 1:
                graph[pos].append((i, j + 1))

    return graph


def dfs(
    graph: dict[tuple[int, int], list[tuple[int, int]]],
    grid: np.ndarray,
    start: tuple[int, int],
) -> int:

    q = []
    visited = set()

    q.append(start)
    score = 0
    while q:
        u = q.pop(-1)
        if u in visited:
            continue

        visited.add(u)

        if grid[*u] == 9:
            score += 1
            continue

        for v in graph[u]:
            if grid[*v] - grid[*u] == 1:
                q.append(v)

    return score


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = np.array(
        [[int(v) for v in line.strip()] for line in lines.split("\n") if line]
    )
    graph = grid_to_graph(grid)

    trailheads = [(x.item(), y.item()) for x, y in zip(*np.where(grid == 0))]

    total_score = 0

    for start in trailheads:
        total_score += dfs(graph, grid, start)

    return total_score


def dfs_with_path(
    graph: dict[tuple[int, int], list[tuple[int, int]]],
    grid: np.ndarray,
    start: tuple[int, int],
) -> int:

    q = []
    # visited = set()
    paths = set()

    q.append((start, ()))

    while q:

        u, prev = q.pop(-1)

        # if u in visited:
        #     continue

        # visited.add(u)

        if grid[*u] == 9:
            paths.add((*prev, u))
            continue

        for v in graph[u]:
            if grid[*v] - grid[*u] == 1:
                q.append((v, (*prev, u)))

    return len(paths)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array(
        [[int(v) for v in line.strip()] for line in lines.split("\n") if line]
    )
    graph = grid_to_graph(grid)

    trailheads = [(x.item(), y.item()) for x, y in zip(*np.where(grid == 0))]

    total_score = 0

    for start in trailheads:
        total_score += dfs_with_path(graph, grid, start)

    return total_score


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
