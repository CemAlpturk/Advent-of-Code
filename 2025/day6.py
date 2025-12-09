import os
import time
from functools import reduce


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


def process_input(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    vals = [] 
    ops = [] 

    n = len(lines)
    
    for line in lines[:-1]:
        v = list(map(int, (x for x in line.split(" ") if x)))
        vals.append(v)

    ops = [x for x in lines[-1].split(" ") if x]

    return vals, ops 


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vals, ops = process_input(lines)
    
    tot = 0 
    m = len(ops)

    for j in range(m):
        op = ops[j]
        vs = [v[j] for v in vals]
        
        if op == "+":
            tot += reduce(lambda x, y: x + y, vs, 0)
        else:
            tot += reduce(lambda x, y: x * y, vs, 1)

    return tot

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    vals = lines[:-1]
    n = len(vals)
    m = len(vals[0])
    # Invert 
    new_vals = []
    r = []
    for j in reversed(range(m)):
        s = "".join(vals[i][j] for i in range(n)).strip(" ")
        if s:
            r.append(int(s))
        else:
            new_vals.append(r)
            r = [] 
    new_vals.append(r)


    ops = [x for x in lines[-1].split(" ") if x][::-1]

    vals = new_vals
    # i = 0
    # l = len(new_vals) // len(ops)
    # while i < len(new_vals):
    #     vals.append(new_vals[i:i+l])
    #     i += l


    tot = 0
    m = len(ops)
    for j in range(m):
        op = ops[j]
        vs = vals[j]
        
        if op == "+":
            k = reduce(lambda x, y: x + y, vs, 0)
        else:
            k = reduce(lambda x, y: x * y, vs, 1)

        tot += k
        # print(vs, op, k)

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
