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


def divisors(n: int): 
    large = []

    d = 1 
    while d * d <= n:
        if n % d == 0:
            yield d 
            if d != n // d:
                large.append(n // d)
        d += 1 

    for d in reversed(large):
        yield d


def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)
    val = 34000000
    i = 1
    while True:
        score = sum(divisors(i)) * 10
        if score > val:
            break 
        i += 1 
        
    return i

def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)
    val = 34000000
    i = 1 
    while True:
        score = sum(11*x for x in divisors(i) if i // x <= 50)
        if score > val:
            break 
        i += 1 

    return i


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
