import os
import time

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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    # Construct into graph
    n = len(lines)
    m = len(lines[0])
    start = (0, 0)
    splitters = set()
    graph = Graph() 
    for i in range(n):
        for j in range(m):
            v = lines[i][j] 
            
            if v == "S":
                start = (i, j)

            if v == "^":
                splitters.add((i, j))

            if i < n - 1:
                if v in "S.":
                    graph.add_edge((i, j), (i+1, j), bidirectional=False)
                else:
                    graph.add_edge((i, j), (i, j-1), bidirectional=False)
                    graph.add_edge((i, j), (i, j+1), bidirectional=False)


    nodes = bfs(graph, start)

    return len({node for node in nodes if node in splitters})
    

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = len(lines)
    m = len(lines[0])
    start = (-1, -1)
    for i in range(n):
        for j in range(m):
            v = lines[i][j]
            if v == "S":
                start = (i, j)
                break 

    counts = [0] * m 
    counts[start[1]] = 1 

    for i in range(n):
        for j in range(m):
            v = lines[i][j] 
            if v == "^":
                counts[j-1] += counts[j] 
                counts[j+1] += counts[j]
                counts[j] = 0 

    return sum(counts)

if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
