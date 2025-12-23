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
    n_discs = len(lines)
    disc_sizes = []
    disc_pos = []
    for line in lines:
        words = line.split(" ")
        disc_sizes.append(int(words[3]))
        disc_pos.append(int(words[-1][:-1]))

    t = 0 
    while True:
        passed = True 
        for i in range(n_discs):
            if (disc_pos[i] + (t+i+1)) % disc_sizes[i] != 0:
                t += 1 
                passed = False 
                break 
        if passed:
            break 
    return t

def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n_discs = len(lines) + 1
    disc_sizes = []
    disc_pos = []
    for line in lines:
        words = line.split(" ")
        disc_sizes.append(int(words[3]))
        disc_pos.append(int(words[-1][:-1]))

    disc_sizes.append(11)
    disc_pos.append(0)

    t = 0 
    while True:
        passed = True 
        for i in range(n_discs):
            if (disc_pos[i] + (t+i+1)) % disc_sizes[i] != 0:
                t += 1 
                passed = False 
                break 
        if passed:
            break 
    return t



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
