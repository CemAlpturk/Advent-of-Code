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


def toggle(line: str) -> str:
    words = line.split(" ")
    n_args = len(words) - 1 

    if n_args == 1:
        words[0] = "dec" if words[0] == "inc" else "inc"
        return " ".join(words)
    elif n_args == 2:
        words[0] = "cpy" if words[0] == "jnz" else "jnz"
        return " ".join(words)
    return line 


def is_int(x: str) -> bool:
    try:
        int(x)
        return True 
    except ValueError:
        return False
        
    
def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    registers = {}
    pc = 0

    registers["a"] = 7

    while 0 <= pc < len(lines):
        line = lines[pc]
        words = line.split(" ")

        match words[0]:
            case "cpy":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                y = words[-1]
                if not y.isnumeric():
                    registers[y] = x 
            case "inc":
                registers[words[1]] += 1
            case "dec":
                registers[words[1]] -= 1 
            case "jnz":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                y = int(words[2]) if is_int(words[2]) else registers[words[2]]
                if x != 0:
                    pc += y - 1
            case "tgl":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                idx = pc + x
                if 0 <= idx < len(lines):
                    lines[idx] = toggle(lines[idx])
        
        # print(line, registers, lines)
        pc += 1
    return registers["a"]


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    registers = {}
    pc = 0

    registers["a"] = 12

    lines[4] = "mul b d a"
    lines[5] = "cpy 0 d"
    lines[6] = "cpy 0 c"
    lines[7] = "NOP"
    lines[8] = "NOP"
    lines[9] = "NOP"

    while 0 <= pc < len(lines):
        line = lines[pc]
        words = line.split(" ")
        

        match words[0]:
            case "cpy":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                y = words[-1]
                if not y.isnumeric():
                    registers[y] = x 
            case "inc":
                registers[words[1]] += 1
            case "dec":
                registers[words[1]] -= 1 
            case "jnz":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                y = int(words[2]) if is_int(words[2]) else registers[words[2]]
                if x != 0:
                    pc += y - 1
            case "tgl":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                idx = pc + x
                if 0 <= idx < len(lines):
                    lines[idx] = toggle(lines[idx])
            case "mul":
                x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                y = int(words[2]) if is_int(words[2]) else registers[words[2]]
                z = words[3]
                registers[z] = x * y
            case "NOP":
                pass

        
        # print(line, registers, lines)
        pc += 1
        # print(pc, registers)
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
