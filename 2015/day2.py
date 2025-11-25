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
    dims =  list(tuple(map(int, line.split("x"))) for line in lines)

    tot = 0
    for x, y, z in dims:
        a1 = x * y
        a2 = x * z 
        a3 = z * y 
        slack = min(a1, a2, a3)
        tot += 2*a1 + 2*a2 + 2*a3 + slack 

    return tot
    


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    dims = list(tuple(map(int, line.split("x"))) for line in lines)

    tot = 0 
    for x, y, z in dims:
        p1 = 2 * (x + y)
        p2 = 2 * (x + z)
        p3 = 2 * (y + z)
        v = x * y * z 
        tot += min(p1, p2, p3) + v 

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
