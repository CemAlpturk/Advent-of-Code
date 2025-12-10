import os
import time
import math
from collections import defaultdict, Counter
from itertools import combinations
from functools import reduce
from toolbox.data_structures import UnionFind, PriorityQueue


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


def dist(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1 
    x2, y2, z2 = p2 
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    coords = [tuple(map(int, line.split(","))) for line in lines]
    
    edges = combinations(coords, 2)
    queue = PriorityQueue(edges, lambda x: dist(x[0], x[1]))  # type: ignore

    circuits = UnionFind()

    steps = 1000 

    for _ in range(steps):
        # Pop the smallest edge 
        p1, p2 = queue.pop() 
        circuits.union(p1, p2)

    
    counts = defaultdict(int)
    for p in coords:
        root = circuits.find(p)
        counts[root] += 1 
    
    vals = list(sorted(counts.values(), reverse=True))
    return vals[0] * vals[1] * vals[2]

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    coords = [tuple(map(int, line.split(","))) for line in lines] 

    edges = combinations(coords, 2)
    queue = PriorityQueue(edges, lambda x: dist(x[0], x[1]))  # type: ignore 

    circuits = UnionFind() 

    while True:
        # Pop the smallest edge 
        p1, p2 = queue.pop() 

        # Join circuits 
        circuits.union(p1, p2)

        # Check number of circuits 
        counts = defaultdict(int)
        for p in coords:
            root = circuits.find(p)
            counts[root] += 1 

        if len(counts) == 1:
            return p1[0] * p2[0] 


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
