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

def is_int(x: str) -> bool:
    try:
        int(x)
        return True 
    except ValueError:
        return False


def is_clock(x: list[int]) -> bool:
    return (
        all(xi in (0, 1) for xi in x) and 
        all(a != b for a, b in zip(x, x[1:]))
    )

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    val = 0
    while True:

        registers = {}
        pc = 0
        registers["a"] = val 
        out: list[int] = []
        visited = set()
    
        while 0 <= pc < len(lines):
            state = (pc, tuple(registers.items()))
            if state in visited:
                break
            visited.add(state)

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
                case "out": 
                    x = int(words[1]) if is_int(words[1]) else registers[words[1]]
                    out.append(x)
            # print(line, registers, lines)
            pc += 1

        if is_clock(out):
            return val
        val += 1 


    


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
