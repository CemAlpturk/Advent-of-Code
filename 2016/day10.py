import os
import time
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

    vals: dict[str, tuple] = {}
    connections: dict[str, tuple] = {}

    for line in lines:
        words = line.split(" ")
        if words[0] == "value":
            v = int(words[1])
            u = "b" + words[-1]
            if u not in vals:
                vals[u] = ()
            vals[u] = vals[u] + (v,)
        else:
            u = "b" + words[1]
            v = words[5][0] +words[6] 
            w = words[-2][0] + words[-1]
            connections[u] = (v, w)


    # Execute graph 

    ta, tb = 61, 17

    queue = [k for k, v in vals.items() if len(v) == 2]
    while queue:
        u = queue.pop(0)
        if u not in connections:
            continue 
        a, b = vals[u]
        x, y = connections[u]

        if min(a, b) == min(ta, tb) and max(a, b) == max(ta, tb):
            return u[1:]

        if x not in vals:
            vals[x] = ()
        if y not in vals:
            vals[y] = ()

        vals[x] = vals[x] + (min(a, b),)
        vals[y] = vals[y] + (max(a, b),)
        if len(vals[x]) == 2:
            queue.append(x)
        if len(vals[y]) == 2:
            queue.append(y)

    print(vals)

    


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    vals: dict[str, tuple] = {}
    connections: dict[str, tuple] = {}

    for line in lines:
        words = line.split(" ")
        if words[0] == "value":
            v = int(words[1])
            u = "b" + words[-1]
            if u not in vals:
                vals[u] = ()
            vals[u] = vals[u] + (v,)
        else:
            u = "b" + words[1]
            v = words[5][0] +words[6] 
            w = words[-2][0] + words[-1]
            connections[u] = (v, w)


    # Execute graph 
    queue = [k for k, v in vals.items() if len(v) == 2]
    while queue:
        u = queue.pop(0)
        if u not in connections:
            continue 
        a, b = vals[u]
        x, y = connections[u]

        if x not in vals:
            vals[x] = ()
        if y not in vals:
            vals[y] = ()

        vals[x] = vals[x] + (min(a, b),)
        vals[y] = vals[y] + (max(a, b),)
        if len(vals[x]) == 2:
            queue.append(x)
        if len(vals[y]) == 2:
            queue.append(y)


    return vals["o0"][0] * vals["o1"][0] * vals["o2"][0]


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
