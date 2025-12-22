import os
import time
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


def is_wall(x: int, y: int, num: int) -> bool:
    val = num + x*x + 3*x + 2*x*y + y + y*y
    b = bin(val)
    return sum(bi == "1" for bi in b[2:]) % 2 == 1


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    num = int(lines[0])
    start = (1, 1)
    target = (31, 39)

    # Explore and build graph 
    graph = Graph() 
    queue = [start]
    visited = set()
    while queue:
        u = queue.pop(0)
        if u in visited:
            continue 
        visited.add(u)

        if u == target:
            break 

        i, j = u 
        if i > 0 and not is_wall(i-1, j, num):
            queue.append((i-1, j))
            graph.add_edge(u, (i-1, j))
        if not is_wall(i+1, j, num):
            queue.append((i+1, j))
            graph.add_edge(u, (i+1, j))
        if j > 0 and not is_wall(i, j-1, num):
            queue.append((i, j-1))
            graph.add_edge(u, (i, j-1))
        if not is_wall(i, j+1, num):
            queue.append((i, j+1))
            graph.add_edge(u, (i, j+1))

    dists = dijkstra(graph, start, target)
    return int(dists[target])





def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    num = int(lines[0])
    start = (1, 1)
    n = 50

    # Explore and build graph 
    queue = [(start, 0)]
    visited = set()
    while queue:
        u, d = queue.pop(0)
        if d > n:
            continue
        if u in visited:
            continue 
        visited.add(u)
        

        i, j = u 
        if i > 0 and not is_wall(i-1, j, num):
            queue.append(((i-1, j), d+1))
        if not is_wall(i+1, j, num):
            queue.append(((i+1, j), d+1))
        if j > 0 and not is_wall(i, j-1, num):
            queue.append(((i, j-1), d+1))
        if not is_wall(i, j+1, num):
            queue.append(((i, j+1), d+1))

    return len(visited)




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
