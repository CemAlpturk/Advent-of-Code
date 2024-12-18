import os
import time

from tqdm import trange

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


def make_graph(coords: list[tuple[int, int]], n: int, m: int) -> Graph:
    graph = Graph()

    for i in range(n):
        for j in range(m):
            pos = (i, j)

            if pos in coords:
                continue

            if i > 0 and (i - 1, j) not in coords:
                graph.add_edge(pos, (i - 1, j))
            if i < n - 1 and (i + 1, j) not in coords:
                graph.add_edge(pos, (i + 1, j))
            if j > 0 and (i, j - 1) not in coords:
                graph.add_edge(pos, (i, j - 1))
            if j < m - 1 and (i, j + 1) not in coords:
                graph.add_edge(pos, (i, j + 1))

    return graph


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    byte_coords = [
        tuple(map(int, line.strip().split(","))) for line in lines.split("\n") if line
    ]
    n = 71
    graph = make_graph(byte_coords[:1024], n, n)  # type: ignore

    start = (0, 0)
    end = (n - 1, n - 1)

    dists = dijkstra(graph, start)
    return int(dists[end])


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    byte_coords = [
        tuple(map(int, line.strip().split(","))) for line in lines.split("\n") if line
    ]
    n = 71

    start = (0, 0)
    end = (n - 1, n - 1)

    for i in trange(len(byte_coords)):
        graph = make_graph(byte_coords[: i + 1], n, n)  # type: ignore

        dists = dijkstra(graph, start)
        if dists[end] == float("inf"):
            return ",".join(map(str, byte_coords[i]))


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
