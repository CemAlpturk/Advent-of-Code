import os
import time
from itertools import combinations 
from functools import reduce 
from operator import mul


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
    packages = list(map(int, lines))
    
    target = sum(packages) // 3 

    for i in range(len(packages)):
        qes = [reduce(mul, c) for c in combinations(packages, i) if sum(c) == target]
        
        if qes:
            return min(qes)




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    packages = list(map(int, lines))
    
    target = sum(packages) // 4 

    for i in range(len(packages)):
        qes = [reduce(mul, c) for c in combinations(packages, i) if sum(c) == target]
        
        if qes:
            return min(qes)



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
