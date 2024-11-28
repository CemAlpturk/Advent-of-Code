import os
import numpy as np
from tqdm import tqdm


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


def to_graph(grid: np.ndarray) -> dict[tuple[int, int], list[tuple[int, int]]]:
    graph = {}
    n, m = grid.shape
    for i in range(n):
        for j in range(m):
            pos = (i, j)
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


def dijkstra(
    graph: dict, costs: np.ndarray, start: tuple[int, int], end: tuple[int, int]
) -> dict:

    dist = {}
    prev = {}
    q = []
    for v in graph.keys():
        dist[v] = float("inf")
        prev[v] = None
        q.append(v)

    dist[start] = 0
    with tqdm(total=len(q)) as pbar:
        while q:
            u = None
            min_d = float("inf")
            idx = None
            for i, v in enumerate(q):
                d = dist[v]
                if d < min_d:
                    min_d = d
                    u = v
                    idx = i

            if u is None:
                break

            if u == end:
                break

            q.pop(idx)

            for v in graph[u]:
                if v in q:
                    alt = dist[u] + costs[v[0], v[1]]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

            pbar.update(1)

    return dist


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    n = len(lines)
    m = len(lines[0])
    grid = np.zeros((n, m), dtype=int)

    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            grid[i, j] = v

    graph = to_graph(grid)

    start = (0, 0)
    end = (n - 1, m - 1)

    dist = dijkstra(graph, grid, start, end)

    return dist[end]


def increment_grid(grid: np.ndarray, n: int) -> np.ndarray:
    for _ in range(n):
        grid = grid + 1
        grid[grid == 10] = 1

    return grid.copy()


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    n = len(lines)
    m = len(lines[0])
    _grid = np.zeros((n, m), dtype=int)

    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            _grid[i, j] = v

    grid = np.zeros((5 * n, 5 * m), dtype=int)

    for i in range(5):
        for j in range(5):
            grid[i * n : (i + 1) * n, j * m : (j + 1) * m] = increment_grid(
                _grid, i + j
            )

    graph = to_graph(grid)

    start = (0, 0)
    end = (5 * n - 1, 5 * m - 1)

    dist = dijkstra(graph, grid, start, end)

    return dist[end]


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
