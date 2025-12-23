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


def check_ip(ip, ranges):
    for a, b in ranges:
        if a <= ip <= b:
            return False, (a,b)

    return True , None



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    ranges = [tuple(map(int, line.split("-"))) for line in lines]

    ranges = sorted(ranges)

    
    i = 0
    while True:
        # print(i)
        if check_ip(i, ranges)[0]:
            break 
        i += 1

    return i



def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    ranges = [tuple(map(int, line.split("-"))) for line in lines]

    ranges = sorted(ranges)

    i = 0 
    c = 0
    while i <= 4294967295:
        ok, rng = check_ip(i, ranges)
        if ok:
            c += 1 
            i += 1 
        else:
            i = rng[1] + 1

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
