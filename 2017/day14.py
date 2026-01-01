import os
import time
from typing import Callable
from functools import reduce
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


def circular_apply(
    xs: list[int],
    start: int,
    length: int,
    fn: Callable[[list[int]], list[int]],
) -> None:

    n = len(xs)
    if n == 0 or length == 0:
        return 

    idxs = [(start + i) % n for i in range(length)]
    chunk = [xs[i] for i in idxs]
    new_chunk = fn(chunk)
    if len(new_chunk) != len(chunk):
        raise ValueError 

    for i, v in zip(idxs, new_chunk):
        xs[i] = v 

def knot_hash(s: str) -> str:
    lengths = [ord(c) for c in s]
    lengths += [17, 31, 73, 47, 23]

    n = 256 
    k = 64 
    xs = list(range(n))
    current_pos = 0
    skip_size = 0 

    def fn(vals: list[int]) -> list[int]:
        return vals[::-1]

    for _ in range(k):
        for l in lengths:
            circular_apply(xs, current_pos, l ,fn)
            current_pos += l + skip_size 
            current_pos %= n 
            skip_size += 1 

    hsh = ""
    for i in range(16):
        start = i * 16  
        stop = start + 16 

        val = reduce(lambda x, y: x ^ y, xs[start:stop], 0)
        h = hex(val).replace("0x", "")
        if len(h) == 1:
            h = "0" + h 
        hsh += h

    return hsh

def hex_to_bits(s: str) -> str:
    v = int(s, 16)
    return format(v, "04b")

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    key = lines[0] 

    n = 128
    tot = 0 
    for i in range(n):
        row_str = key + f"-{i}"
        h = knot_hash(row_str)
        bits = "".join(hex_to_bits(hi) for hi in h)
        tot += sum(b == "1" for b in bits)

    return tot


def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    key = lines[0] 

    n = 128 
    grid = []
    for i in range(n):
        row_str = key + f"-{i}"
        h = knot_hash(row_str)
        bits = "".join(hex_to_bits(hi) for hi in h)
        grid.append([b == "1" for b in bits])


    n = len(grid)
    m = len(grid[0])
    graph = Graph() 
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                graph.add_edge((i, j), (i, j))
                if i > 0 and grid[i-1][j]:
                    graph.add_edge((i, j), (i-1, j))
                if i < n-1 and grid[i+1][j]:
                    graph.add_edge((i, j), (i+1, j))
                if j > 0 and grid[i][j-1]:
                    graph.add_edge((i, j), (i, j-1))
                if j < m-1 and grid[i][j+1]:
                    graph.add_edge((i, j), (i, j+1))

    visited = set()
    count = 0 
    for node in graph.nodes():
        if node not in visited:
            visited.update(bfs(graph, node))
            count += 1 

    return count





if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
