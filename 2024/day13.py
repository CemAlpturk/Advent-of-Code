import os
import time
from math import gcd
import numpy as np


def read_input(filename: str) -> str:
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
        data = f.read()

    return data


def solve_system(A, B, G):
    Ax, Ay = A
    Bx, By = B
    Gx, Gy = G

    c1 = (Gy * Ax - Gx * Ay) / (Ax * By - Ay * Bx)
    c2 = (Gx - Bx * c1) / Ax
    return c2, c1


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    A_cost = 3
    B_cost = 1
    total = 0
    for block in lines.split("\n\n"):
        if not block:
            continue

        machine = block.split("\n")
        A = tuple(
            map(lambda x: int(x.split("+")[-1]), machine[0].split(": ")[1].split(", "))
        )
        B = tuple(
            map(lambda x: int(x.split("+")[-1]), machine[1].split(": ")[1].split(", "))
        )
        G = tuple(
            map(lambda x: int(x.split("=")[-1]), machine[2].split(": ")[1].split(", "))
        )

        c1, c2 = solve_system(A, B, G)
        if int(c1) == c1 and int(c2) == c2:
            # print(A, B, G, c1, c2)
            total += A_cost * int(c1) + B_cost * int(c2)

    return total


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    A_cost = 3
    B_cost = 1
    d = 10000000000000
    total = 0
    for block in lines.split("\n\n"):
        if not block:
            continue

        machine = block.split("\n")
        A = tuple(
            map(lambda x: int(x.split("+")[-1]), machine[0].split(": ")[1].split(", "))
        )
        B = tuple(
            map(lambda x: int(x.split("+")[-1]), machine[1].split(": ")[1].split(", "))
        )
        G = tuple(
            map(
                lambda x: d + int(x.split("=")[-1]),
                machine[2].split(": ")[1].split(", "),
            )
        )

        c1, c2 = solve_system(A, B, G)
        if int(c1) == c1 and int(c2) == c2:  #  and c1 <= 100 and c2 <= 100:
            # print(A, B, G, c1, c2)
            total += A_cost * int(c1) + B_cost * int(c2)

    return total


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
