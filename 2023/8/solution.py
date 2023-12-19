from itertools import cycle
import math


def part1(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    rule = lines[0].strip()
    # print(rule)

    _map = {}
    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue
        k, v = line.split(" = ")
        k = k.strip()
        v1 = v.split(",")[0][1:]
        v2 = v.split(", ")[1][:-1]

        _map[k] = (v1, v2)

    start = "AAA"
    end = "ZZZ"
    curr = start
    n = 0
    # print(curr)
    while curr != end:
        if curr in _map:
            v1, v2 = _map[curr]
            # print(rule[n % len(rule)])
            if rule[n % len(rule)] == "L":
                curr = v1
            else:
                curr = v2
            n += 1
            # print(curr)
        else:
            break

    print(n)


def part2(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    rule = lines[0].strip()
    directions = [0 if d == "L" else 1 for d in rule]
    _map = {}
    start_nodes = []
    end_nodes = []
    for line in lines[1:]:
        line = line.strip()
        if line == "":
            continue
        k, v = line.split(" = ")
        k = k.strip()
        v1 = v.split(",")[0][1:]
        v2 = v.split(", ")[1][:-1]

        _map[k] = (v1, v2)

        if k[-1] == "A":
            start_nodes.append(k)
        elif k[-1] == "Z":
            end_nodes.append(k)

    cycles = []
    for node in start_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = _map[node][d]
            if node[-1] == "Z":
                cycles.append(steps)
                break

    print(math.lcm(*cycles))


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
