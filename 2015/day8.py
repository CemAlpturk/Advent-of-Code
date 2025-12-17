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


def code(s: str) -> int:
    s = s[1:-1]
    c = 0
    i = 0 
    while i < len(s):
        if s[i] == '\\':
            if s[i+1] == '"':
                i += 2 
            elif s[i+1] == 'x':
                i += 4
            elif s[i+1] == '\\':
                i += 2
        else:
            i += 1
        c += 1
        

    return c

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    tot = 0 
    for line in lines:
        l1 = len(line)  
        l2 = code(line)
        # print(line, l1, l2)
        tot += l1 - l2

    return tot


def code2(s: str) -> int:
    c = 0
    for si in s:
        if si == '"':
            c += 2
        elif si == '\\':
            c += 2 
        else:
            c += 1 

    return c + 2 
    


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    tot = 0 
    for line in lines:
        l1 = len(line)
        l2 = code2(line)
        tot += l2 - l1 

    return tot


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
