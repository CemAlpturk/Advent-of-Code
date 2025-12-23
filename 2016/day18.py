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


def new_row(row: list[bool]) -> list[bool]:
    crow = [False] + row + [False]
    nrow = []
    for i in range(1, len(crow)-1):
        left = crow[i-1]
        center = crow[i]
        right = crow[i+1]

        if (
            (left and center and (not right)) or 
            (center and right and (not left)) or
            (left and (not center and not right)) or
            (right and (not center and not left))
        ):
            nrow.append(True)
        else:
            nrow.append(False)

    return nrow 


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    row = list(x == "^" for x in lines[0])
    c = len(row) - sum(row)
    for _ in range(39):
        row = new_row(row)
        c += len(row) - sum(row)

    return c
    


def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    row = list(x == "^" for x in lines[0])
    c = len(row) - sum(row)
    for _ in range(400000-1):
        row = new_row(row)
        c += len(row) - sum(row)

    return c


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
