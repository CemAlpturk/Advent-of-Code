import os
import time
from itertools import permutations


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
    nodes = set()
    sizes = {}
    used = {} 
    avail = {}

    for line in lines[2:]:
        words = [w for w in line.split(" ") if w]
        x, y = words[0].split("-")[-2:]
        x = int(x[1:])
        y = int(y[1:])
        node = (x, y) 
        nodes.add(node)

        size = int(words[1][:-1])
        sizes[node] = size 
        used[node] = int(words[2][:-1])
        avail[node] = int(words[3][:-1])
    
    count = 0
    for u, v in permutations(nodes, 2):
        if used[u] > 0 and u != v and used[u] <= avail[v]:
            count += 1 

    return count






def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    nodes = set()
    sizes = {}
    used0 = {} 
    avail0 = {}
    usage = {}
    n, m = 0, 0
    for line in lines[2:]:
        words = [w for w in line.split(" ") if w]
        x, y = words[0].split("-")[-2:]
        x = int(x[1:])
        y = int(y[1:])
        node = (x, y) 
        nodes.add(node)
        n = max(n, x)
        m = max(m, y)

        size = int(words[1][:-1])
        sizes[node] = size 
        used0[node] = int(words[2][:-1])
        avail0[node] = int(words[3][:-1])
        usage[node] = int(words[-1][:-1])
    
    # bfs 
    start = (n, 0)
    end = (0, 0)


    # plot 
    for i in range(n+1):
        s = ""
        for j in range(m+1):
            if (i, j) == end:
                s += "!"
            elif (i, j) == start:
                s += "G"
            elif usage[(i, j)] == 0:
                empty = (i, j)
                s += "e"
            else:
                c = 0
                k = 0
                c += i > 0 and used0[(i, j)] <= sizes[(i-1, j)]
                c += i < n and used0[(i, j)] <= sizes[(i+1, j)]
                c += j > 0 and used0[(i, j)] <= sizes[(i, j-1)]
                c += j < m and used0[(i, j)] <= sizes[(i, j+1)]

                k += i > 0 
                k += i < n 
                k += j > 0
                k += j < m 

                if c  < k:
                    s += "#"
                else:
                    s += "."
        print(s)

    print(start, end, empty)

    return 10 + 52 + 5 * 35 + 1  



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
