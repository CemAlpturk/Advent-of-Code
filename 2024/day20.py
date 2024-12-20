import os
import time
from collections import defaultdict
import numpy as np
from tqdm import tqdm

from toolbox.data_structures import Graph
from toolbox.algorithms.graphs import dijkstra


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


def grid_to_graph(grid: np.ndarray) -> Graph:
    graph = Graph()
    n, m = grid.shape

    for i in range(n):
        for j in range(m):
            if grid[i, j] == "#":
                continue

            pos = (i, j)
            # graph[pos] = []

            if i > 0 and grid[i - 1, j] != "#":
                graph.add_edge(pos, (i - 1, j), bidirectional=False)
            if i < n - 1 and grid[i + 1, j] != "#":
                graph.add_edge(pos, (i + 1, j), bidirectional=False)
            if j > 0 and grid[i, j - 1] != "#":
                graph.add_edge(pos, (i, j - 1), bidirectional=False)
            if j < m - 1 and grid[i, j + 1] != "#":
                graph.add_edge(pos, (i, j + 1), bidirectional=False)

    return graph


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    n, m = grid.shape
    start = list((x.item(), y.item()) for x, y in zip(*np.where(grid == "S")))[0]
    end = list((x.item(), y.item()) for x, y in zip(*np.where(grid == "E")))[0]

    counts = defaultdict(int)
    graph = grid_to_graph(grid)

    real_dists = dijkstra(graph, start)
    max_path = real_dists[end]

    _walls = list(
        map(lambda x: (x[0].item(), x[1].item()), zip(*np.where(grid == "#")))
    )
    walls = []
    for x, y in _walls:
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            continue

        c = 0
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            pos = add((x, y), d)
            if grid[*pos] != "#":
                c += 1

        if c > 0:
            walls.append((x, y))

    for x, y in tqdm(walls):
        # Remove the wall and insert as new node
        if grid[x - 1, y] != "#":
            graph.add_edge((x, y), (x - 1, y))
        if grid[x + 1, y] != "#":
            graph.add_edge((x, y), (x + 1, y))
        if grid[x, y - 1] != "#":
            graph.add_edge((x, y), (x, y - 1))
        if grid[x, y + 1] != "#":
            graph.add_edge((x, y), (x, y + 1))

        dists = dijkstra(graph, start)
        d = max_path - dists[end]
        counts[int(d)] += 1

        # Add the wall again
        graph.remove_node((x, y))

    return sum(v for k, v in counts.items() if k >= 100)


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
