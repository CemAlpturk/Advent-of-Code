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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    ranges = list(tuple(map(int, x.split("-"))) for x in lines[0].split(","))
    
    s = 0
    for r1, r2 in ranges:
        for i in range(r1, r2+1):
            val = str(i)
            l = len(val)
            if val[:l//2] == val[l//2:]:
                s += i 

    return s


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    ranges = list(tuple(map(int, x.split("-"))) for x in lines[0].split(","))

    s = 0 
    for r1, r2 in ranges:
        for i in range(r1, r2+1):
            val = str(i) 
            l = len(val) 

            for j in range(1, l):
                k = l % j 
                if k == 0:
                    n = l // j 
                    c = val[:j]
                    if c * n == val:
                        s += i 
                        break

    return s


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
