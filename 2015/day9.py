import os
import time
from itertools import permutations

from toolbox.data_structures import Graph 


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


def best_path(graph: Graph):
    best = float("inf")
    best_path = None 

    cities = graph.nodes()
    for perm in permutations(cities):
        total = sum(graph.weights[(a, b)] for a, b in zip(perm, perm[1:]))
        if total < best:
            best = total 
            best_path = perm 

    return best


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    graph = Graph() 
    for line in lines:
        u = line.split(" ")[0]
        v = line.split(" ")[2]
        w = int(line.split(" ")[-1])

        graph.add_edge(u, v, w=w)

    return best_path(graph)




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    graph = Graph() 
    for line in lines:
        u = line.split(" ")[0]
        v = line.split(" ")[2]
        w = int(line.split(" ")[-1])

        graph.add_edge(u, v, w=-w)

    return -best_path(graph)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
