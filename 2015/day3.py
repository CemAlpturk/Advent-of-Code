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
    commands = lines[0]

    x, y = 0, 0
    houses = {(x, y)}

    for c in commands:
        if c == "^":
            y += 1 
        elif c == "v":
            y -= 1
        elif c == ">":
            x += 1
        else:
            x -= 1

        houses.add((x, y))

    return len(houses)
            


def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    c1 = lines[0][::2]
    c2 = lines[0][1::2]

    x1, y1 = 0, 0
    x2, y2 = 0, 0

    houses = {(x1, y1)}

    for c in c1:
        if c == "^":
            y1 += 1 
        elif c == "v":
            y1 -= 1 
        elif c == ">":
            x1 += 1 
        else:
            x1 -= 1

        houses.add((x1, y1))

    for c in c2:
        if c == "^":
            y2 += 1
        elif c == "v":
            y2 -= 1
        elif c == ">":
            x2 += 1
        else:
            x2 -= 1 

        houses.add((x2, y2))

    return len(houses)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
