import os
import time
import random
from toolbox.data_structures import Graph 
from toolbox.algorithms.graphs import bfs 


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


def construct_graph(lines: list[str]) -> Graph:
    graph = Graph() 

    for line in lines:
        u, vs = line.split(" <-> ")
        for v in vs.split(", "):
            graph.add_edge(u, v)

    return graph

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph = construct_graph(lines)

    nodes = bfs(graph, "0")
    return len(nodes)


def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph = construct_graph(lines)
    nodes = set(graph.nodes())
    i = 0
    while nodes:
        u = random.choice(list(nodes))
        us = bfs(graph, u)

        for u in us:
            nodes.remove(u)
        i += 1 

    return i


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
