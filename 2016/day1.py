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


def update_dir(dir: tuple[int, int], rot: str) -> tuple[int, int]:
    if dir == (0, 1) and rot == "R":
        return (1, 0)
    if dir == (0, 1) and rot == "L":
        return (-1, 0)
    if dir == (1, 0) and rot == "R":
        return (0, -1)
    if dir == (1, 0) and rot == "L":
        return (0, 1)
    if dir == (-1, 0) and rot == "R":
        return (0, 1)
    if dir == (-1, 0) and rot == "L":
        return (0, -1)
    if dir == (0, -1) and rot == "R":
        return (-1, 0)
    return (1, 0)


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    steps = lines[0].split(", ")

    pos = (0, 0)
    dir = (0, 1)

    for step in steps:
        rot = step[0]
        n = int(step[1:])

        dir = update_dir(dir, rot)
        pos = (pos[0] + n * dir[0], pos[1] + n * dir[1])

    return abs(pos[0]) + abs(pos[1])


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    steps = lines[0].split(", ")

    pos = (0, 0)
    dir = (0, 1)
    visited = {pos} 

    for step in steps:
        rot = step[0]
        n = int(step[1:])

        dir = update_dir(dir, rot)
        for _ in range(n):
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(pos)

    return None



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
