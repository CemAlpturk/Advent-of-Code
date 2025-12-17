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


def look_and_say(s: str) -> str:
    i = 0
    o = ""

    while i < len(s):
        # Look ahead
        j = i + 1 
        while j < len(s) and s[j] == s[i]:
            j += 1 

        c = j - i 
        o += str(c) + s[i]
        i = j 

    return o


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    seq = lines[0]
    for _ in range(40):
        seq = look_and_say(seq)

    return len(seq)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    seq = lines[0] 
    for _ in range(50):
        seq = look_and_say(seq)
    return len(seq)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
