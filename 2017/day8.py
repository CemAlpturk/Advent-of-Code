import os
import time
from collections import defaultdict 


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


def cond(x: int, op: str, y: int) -> bool:
    match op:
        case ">":
            return x > y 
        case "<":
            return x < y 
        case ">=":
            return x >= y
        case "<=":
            return x <= y
        case "==":
            return x == y
        case "!=":
            return x != y

        case _:
            raise ValueError(op)


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    registers = defaultdict(int)

    for line in lines:
        words = line.split(" ")
        r = words[0] 
        command = words[1] 
        v = int(words[2])
        if command == "dec":
            v = -v 

        x = registers[words[4]]
        op = words[5]
        y = int(words[6])

        if cond(x, op, y):
            registers[r] += v 

    return sorted(registers.items(), key=lambda x: (x[1], x[0]), reverse=True)[0]
            




def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    registers = defaultdict(int)
    maxval = -float("inf")
    for line in lines:
        words = line.split(" ")
        r = words[0] 
        command = words[1] 
        v = int(words[2])
        if command == "dec":
            v = -v 

        x = registers[words[4]]
        op = words[5]
        y = int(words[6])

        if cond(x, op, y):
            registers[r] += v 

        maxval = max(maxval, max(registers.values()))

    return maxval


     

if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
