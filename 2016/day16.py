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


def dragon_curve(a: str) -> str:
    b = str(a)[::-1]
    b = b.replace("0", "a")
    b = b.replace("1", "0")
    b = b.replace("a", "1")

    return a + "0" + b 


def get_checksum(s: str) -> str:
    r = ""
    for i in range(0, len(s), 2):
        r += "1" if s[i] == s[i+1] else "0"
    if len(r) % 2 == 0:
        r = get_checksum(r)
    return r


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    state = lines[0] 
    n = 272

    while len(state) < n:
        state = dragon_curve(state)

    state = state[:n]
    checksum = get_checksum(state)
    return checksum




def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    state = lines[0] 
    n = 35651584

    while len(state) < n:
        state = dragon_curve(state)

    state = state[:n]
    checksum = get_checksum(state)
    return checksum



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
