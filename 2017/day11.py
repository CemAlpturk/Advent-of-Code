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



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    commands = lines[0].split(",")

    start = (0, 0, 0)
    u = start 
    for step in commands:
        x, y, z = u 

        match step:
            case "n":
                v = (x, y+1, z-1)
            case "ne":
                v = (x+1, y, z-1)
            case "se":
                v = (x+1, y-1, z)
            case "s":
                v = (x, y-1, z+1)
            case "sw":
                v = (x-1, y, z+1)
            case "nw":
                v = (x-1, y+1, z)
            case _:
                raise ValueError(step)

        u = v 

    end = u 

    return max(abs(start[0] - end[0]), abs(start[1] - end[1]), abs(start[2] - end[2]))


def dist(x: tuple[int, int, int], y: tuple[int, int, int]) -> int:
    return max(map(lambda a: abs(a[0]-a[1]), zip(x, y)))


def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    commands = lines[0].split(",")

    start = (0, 0, 0)
    u = start
    max_dist = 0
    for step in commands:
        x, y, z = u 

        match step:
            case "n":
                v = (x, y+1, z-1)
            case "ne":
                v = (x+1, y, z-1)
            case "se":
                v = (x+1, y-1, z)
            case "s":
                v = (x, y-1, z+1)
            case "sw":
                v = (x-1, y, z+1)
            case "nw":
                v = (x-1, y+1, z)
            case _:
                raise ValueError(step)
        
        max_dist = max(max_dist, dist(start, v))
        u = v 
    return max_dist





if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
