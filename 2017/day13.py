import os
import time
from collections import defaultdict
from itertools import count


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


def move_scanners(scanners: dict[int, tuple[int, int]], layers: dict[int, int]) -> dict[int, tuple[int, int]]:

    for k in layers.keys():
        s, d = scanners[k]
        r = layers[k]
        if s == 0 or s == r-1:
            d *= -1
        s += d
        assert 0 <= s < r, f"{s}, {r}"
        scanners[k] = (s, d)

    return scanners


def print_scanners(scanners: dict[int, tuple[int, int]], layers: dict[int, int]) -> None:
    for k in scanners.keys():
        print(k, scanners[k], layers[k])


def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)
    layers = {}
    for line in lines:
        k, v = map(int, line.split(": "))
        layers[k] = v
    scanners = {k:(0, -1) for k in layers.keys()}
    severity = 0 

    max_t = max(layers.keys()) + 1 
    
    pos = -1 
    for t in range(max_t):
        pos += 1 
        if pos in layers:
            s, _ = scanners[pos]
            if s == 0:
                severity += pos * layers[pos]

        scanners = move_scanners(scanners, layers)
        # print_scanners(scanners, layers)
        # print()

    return severity

def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    layers = {}
    for line in lines:
        k, v = map(int, line.split(": "))
        layers[k] = v

    def scanner(height, time):
        offset = time % ((height - 1) * 2)
        return 2 * (height - 1) - offset if offset > height - 1 else offset 

    return next(wait for wait in count() if not any(scanner(layers[pos], wait + pos) == 0 for pos in layers))
    


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
