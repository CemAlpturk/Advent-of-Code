import os
import time
import numpy as np
from collections import defaultdict

from toolbox.data_structures import Graph, PriorityQueue
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


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    n, m = grid.shape

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    graph = Graph()
    for i in range(n):
        for j in range(m):
            if grid[i, j] == "#":
                continue
            for k, d in enumerate(dirs):
                pos = (i, j)
                u = (pos, d)
                new_pos = add(pos, d)

                if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                    if grid[*new_pos] != "#":
                        v = (new_pos, d)
                        graph.add_edge(u, v, 1, bidirectional=False)

                v = (pos, dirs[(k - 1) % 4])
                graph.add_edge(u, v, 1000, bidirectional=False)
                v = (pos, dirs[(k + 1) % 4])
                graph.add_edge(u, v, 1000, bidirectional=False)

    start = tuple(map(lambda x: x.item(), list(zip(*np.where(grid == "S")))[0]))
    end = tuple(map(lambda x: x.item(), list(zip(*np.where(grid == "E")))[0]))

    distances = dijkstra(graph, (start, (0, 1)))

    return int(min(distances[(end, d)] for d in dirs))


def dijkstra_multi_path(
    graph: Graph,
    start: tuple[tuple[int, int], tuple[int, int]],
    end: tuple[int, int],
) -> tuple[list, float]:
    pq = PriorityQueue([(0.0, start, [start])], lambda x: x[0])
    shortest_paths = []
    shortest_dist = float("inf")
    visited = defaultdict(lambda: float("inf"))

    while len(pq) > 0:
        d, u, p = pq.pop()

        if d > shortest_dist:
            continue

        if u[0] == end:
            if d < shortest_dist:
                shortest_paths = [p]
                shortest_dist = d
            elif d == shortest_dist:
                shortest_paths.append(p)
            continue

        for v in graph.adj_list.get(u, []):
            w = graph.weights[(u, v)]
            new_d = d + w
            if new_d <= visited[v]:
                visited[v] = new_d
                pq.push((new_d, v, p + [v]))

    return shortest_paths, shortest_dist


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    n, m = grid.shape

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    graph = Graph()
    for i in range(n):
        for j in range(m):
            if grid[i, j] == "#":
                continue
            for k, d in enumerate(dirs):
                pos = (i, j)
                u = (pos, d)
                new_pos = add(pos, d)

                if 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
                    if grid[*new_pos] != "#":
                        v = (new_pos, d)
                        graph.add_edge(u, v, 1, bidirectional=False)

                v = (pos, dirs[(k - 1) % 4])
                graph.add_edge(u, v, 1000, bidirectional=False)
                v = (pos, dirs[(k + 1) % 4])
                graph.add_edge(u, v, 1000, bidirectional=False)

    start = tuple(map(lambda x: x.item(), list(zip(*np.where(grid == "S")))[0]))
    end = tuple(map(lambda x: x.item(), list(zip(*np.where(grid == "E")))[0]))

    paths, dists = dijkstra_multi_path(graph, (start, (0, 1)), end)

    nodes = set()
    for p in paths:
        for u, _ in p:
            nodes.add(u)

    return len(nodes)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
