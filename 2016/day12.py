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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    
    registers = {"a": 0, "b": 0, "c": 0}
    pc = 0
    while pc < len(lines):
        line = lines[pc]
        words = line.split(" ")

        match words[0]:
            case "cpy":
                x = int(words[1]) if words[1].isnumeric() else registers[words[1]]
                y = words[-1]
                registers[y] = x 
            case "inc":
                registers[words[1]] += 1 
            case "dec":
                registers[words[1]] -= 1 
            case "jnz":
                x = int(words[1]) if words[1].isnumeric() else registers[words[1]]
                y = int(words[2])
                if x != 0:
                    pc += y - 1
        pc += 1 

    return registers["a"]


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    registers = defaultdict(int)
    registers["c"] = 1
    pc = 0
    while pc < len(lines):
        line = lines[pc]
        words = line.split(" ")

        match words[0]:
            case "cpy":
                x = int(words[1]) if words[1].isnumeric() else registers[words[1]]
                y = words[-1]
                registers[y] = x 
            case "inc":
                registers[words[1]] += 1 
            case "dec":
                registers[words[1]] -= 1 
            case "jnz":
                x = int(words[1]) if words[1].isnumeric() else registers[words[1]]
                y = int(words[2])
                if x != 0:
                    pc += y - 1
        pc += 1 

    return registers["a"]



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
