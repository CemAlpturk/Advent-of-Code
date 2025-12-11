import os
import time
from functools import cache
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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    # Build graph 
    graph = Graph() 
    for line in lines:
        u, vs = line.split(":")
        vs = [v for v in vs.strip().split(" ") if v]
        for v in vs:
            graph.add_edge(u, v, bidirectional=False)

    # Modified bfs 
    start = "you"
    end = "out"
    queue = [(start, start)]
    paths = set()

    while queue:
        u, path = queue.pop(0)

        if u == end:
            paths.add(path)
        
        if u in graph.adj_list:
            for v in graph.adj_list[u]:
                queue.append((v, path + "-" + v))

    return len(paths)



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    # Build graph 
    graph = Graph()
    for line in lines:
        u, vs = line.split(":")
        vs = [v for v in vs.strip().split(" ") if v]
        for v in vs:
            graph.add_edge(u, v, bidirectional=False)

    # Modified dfs 
    start = "svr"
    end = "out"
    # req = ["dac", "fft"]

    @cache 
    def visit(u: str, dest: str) -> int:
        if u == dest:
            return 1 
        
        return sum(visit(v, dest) for v in graph.adj_list.get(u, []))

    n1 = visit(start, "fft")
    n2 = visit("fft", "dac")
    n3 = visit("dac", end)

    return n1 * n2 * n3
    




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
