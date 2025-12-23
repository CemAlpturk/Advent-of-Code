import os
import time
from hashlib import md5 


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


def doors(passcode: str) -> tuple[bool, bool, bool, bool]:
    h = md5(passcode.encode()).hexdigest()[:4]

    return tuple(x in "bcdef" for x in h)


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    passcode = lines[0] 

    pos = (0, 0)
    goal = (3, 3)

    queue = [(pos, "")]

    while queue:
        u, path = queue.pop(0)
        if u == goal:
            return path
        i, j = u
        code = passcode + path 
        unlocked = doors(code)

        if i > 0 and unlocked[0]:
            queue.append(((i-1, j), path + "U"))
        if i < 3 and unlocked[1]:
            queue.append(((i+1, j), path + "D"))
        if j > 0 and unlocked[2]:
            queue.append(((i, j-1), path + "L"))
        if j < 3 and unlocked[3]:
            queue.append(((i, j+1), path + "R"))




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    passcode = lines[0] 

    pos = (0, 0)
    goal = (3, 3)

    queue = [(pos, "")]
    lens = set()

    while queue:
        u, path = queue.pop(0)
        if u == goal:
            lens.add(len(path))
            continue 
        i, j = u
        code = passcode + path 
        unlocked = doors(code)

        if i > 0 and unlocked[0]:
            queue.append(((i-1, j), path + "U"))
        if i < 3 and unlocked[1]:
            queue.append(((i+1, j), path + "D"))
        if j > 0 and unlocked[2]:
            queue.append(((i, j-1), path + "L"))
        if j < 3 and unlocked[3]:
            queue.append(((i, j+1), path + "R"))

    return max(lens)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
