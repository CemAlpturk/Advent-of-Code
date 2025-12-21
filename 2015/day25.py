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
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)

    r = 2978 
    c = 3083

    p = 20151125
    m = 252533
    d = 33554393

    i, j= 1, 1
    I = 1

    while i != r or j != c:
        p = (p * m) % d 

        if i > 1:
            i -= 1
            j += 1
        else:
            i = I + 1
            I += 1
            j = 1 

    return p




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
