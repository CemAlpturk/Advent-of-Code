import os
import time
from random import shuffle


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

    transforms = {}
    for line in lines[:-2]:
        u, v = line.split(" => ") 
        if u not in transforms:
            transforms[u] = set()
        transforms[u].add(v)

    molecule = lines[-1]

    molecules = set()

    for u in transforms.keys():
        for i in range(0, len(molecule)-len(u)+1):
            if molecule[i:i+len(u)] == u:
                for v in transforms[u]:
                    val = molecule[:i] + v + molecule[i+len(u):]
                    # print(u, v, i, val)
                    molecules.add(val)

    # print(molecules)
    return len(molecules)


def transform(s: str, transforms: dict[str, set]) -> set:
    t = set()

    for u in transforms.keys():
        for i in range(0, len(s) - len(u) + 1):
            if s[i:i+len(u)] == u:
                for v in transforms[u]:
                    val = s[:i] + v + s[i+len(u):]
                    t.add(val)

    return t 


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    reps = []

    for line in lines[:-2]:
        u, v = line.split(" => ")
        reps.append((u, v))

    medicine = lines[-1] 

    target = medicine 
    d = 0
    while target != "e":
        tmp = target 
        for a, b in reps:
            if b not in target:
                continue 

            target = target.replace(b, a, 1)
            d += 1

        if tmp == target:
            target = medicine 
            d = 0
            shuffle(reps)

    return d



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
