import os
import time


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



def process_line(line: str) -> tuple[str, tuple]:
    instruction, args= line.split(" ", 1)
    args = tuple(args.split(", "))
    return instruction, args


def execute(instruction: str, args: tuple, reg: dict, pc: int) -> tuple[dict, int]:

    match instruction:
        case "hlf":
            # Half 
            register = args[0]
            reg[register] //= 2
            pc += 1
        case "tpl":
            # Triple
            register = args[0]
            reg[register] *= 3 
            pc += 1
        case "inc":
            # Increment 
            register = args[0]
            reg[register] += 1 
            pc += 1
        case "jmp":
            offset = args[0]
            if "+" in offset:
                offset = int(offset[1:])
            else:
                offset = -int(offset[1:])
            pc += offset 
        case "jie":
            # jump if even
            register = args[0]
            offset = args[1]
            if "+" in offset:
                offset = int(offset[1:])
            else:
                offset = -int(offset[1:])
            pc += offset if reg[register] % 2 == 0 else 1
        case "jio":
            # jump if one 
            register = args[0]
            offset = args[1]
            if "+" in offset:
                offset = int(offset[1:])
            else:
                offset = -int(offset[1:])
            pc += offset if reg[register] == 1 else 1

    return reg, pc


            


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    reg = {
        "a": 0,
        "b": 0,
    }
    pc = 0 
    n = len(lines)
    
    while 0 <= pc < n:
        instruction, args = process_line(lines[pc])
        reg, pc = execute(instruction, args, reg, pc)

    return reg["b"]
 


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    reg = {
        "a": 1,
        "b": 0,
    }
    pc = 0 
    n = len(lines)
    
    while 0 <= pc < n:
        instruction, args = process_line(lines[pc])
        reg, pc = execute(instruction, args, reg, pc)

    return reg["b"]



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
