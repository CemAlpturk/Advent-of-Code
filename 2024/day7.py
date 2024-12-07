import os
import time
from itertools import product


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


def eval(vals: list[int], res: int, ops: list[str]) -> bool:
    for comb in product(ops, repeat=len(vals) - 1):
        acc = vals[0]
        for v, op in zip(vals[1:], comb):
            if acc > res:
                break

            if op == "+":
                acc += v
            elif op == "*":
                acc *= v
            else:
                acc = int(str(acc) + str(v))

        if acc == res:
            return True

    return False


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = [line for line in read_input(filename).split("\n") if line]
    total = 0
    for line in lines:
        res_str, eq_str = line.split(": ")
        res = int(res_str)

        vals = list(map(int, eq_str.split(" ")))

        if eval(vals, res, ["+", "*"]):
            total += res

    return total


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = [line for line in read_input(filename).split("\n") if line]
    total = 0
    for line in lines:
        res_str, eq_str = line.split(": ")
        res = int(res_str)

        vals = list(map(int, eq_str.split(" ")))

        if eval(vals, res, ["+", "*", "||"]):
            total += res

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
