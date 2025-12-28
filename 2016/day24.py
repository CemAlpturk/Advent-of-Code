import os
import time
from itertools import permutations 
from toolbox.data_structures import Graph 
from toolbox.algorithms.graphs import dijkstra 


def read_input(filename: str) -> list[str]:
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
        lines = f.readlines()

    return [line.strip("\n") for line in lines]


def construct_graph(lines: list[str]) -> tuple[Graph, dict[str, tuple[int, int]]]:
    n = len(lines)
    m = len(lines[0])
    goals = {}
    graph = Graph()
    for i in range(n):
        for j in range(m):
            if lines[i][j] == "#":
                continue 
            v = lines[i][j]
            if v.isnumeric():
                goals[v] = (i, j)

            if i > 0 and lines[i-1][j] != "#":
                graph.add_edge((i, j), (i-1, j))
            if i < n-1 and lines[i+1][j] != "#":
                graph.add_edge((i, j), (i+1, j))
            if j > 0 and lines[i][j-1] != "#":
                graph.add_edge((i, j), (i, j-1))
            if j < m-1 and lines[i][j+1] != "#":
                graph.add_edge((i, j), (i, j+1))

    return graph, goals



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph, goals = construct_graph(lines)
    # Preprocess shortests distances 
    dists = {} 
    for u in goals.values():
        dists[u] = dijkstra(graph, u)

    start = goals.pop("0")
    shortest_dist = float("inf")
    for perm in permutations(goals.keys()):
        d = 0 
        p0 = start 
        for p in perm:
            p1 = goals[p] 
            d += dists[p0][p1]
            if d > shortest_dist:
                break 
            p0 = p1 

        shortest_dist = min(shortest_dist, d)

    return int(shortest_dist)
        


def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph, goals = construct_graph(lines)
    # Preprocess shortests distances 
    dists = {} 
    for u in goals.values():
        dists[u] = dijkstra(graph, u)

    start = goals["0"]
    shortest_dist = float("inf")
    gls = goals.copy()
    gls.pop("0")
    for perm in permutations(gls.keys()):
        perm = perm + ("0", )
        d = 0 
        p0 = start 
        for p in perm:
            p1 = goals[p] 
            d += dists[p0][p1]
            if d > shortest_dist:
                break 
            p0 = p1 

        shortest_dist = min(shortest_dist, d)

    return int(shortest_dist)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
