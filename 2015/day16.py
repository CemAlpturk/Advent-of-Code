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

    tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    aunts = []
    for line in lines:
        fields = line.split(": ", 1)[1]
        d = {}
        for item in fields.split(", "):
            k, v = item.split(": ")
            d[k] = int(v) if v.isnumeric() else v
        aunts.append(d)

    candidates = set()
    for i in range(len(aunts)):
        possible = True
        for k, v in aunts[i].items():
            if k in tape and v != tape[k]:
                possible = False 
                break
        if possible:
            candidates.add(i+1)

    return list(candidates)[0]




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    tape = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    aunts = []
    for line in lines:
        fields = line.split(": ", 1)[1]
        d = {}
        for item in fields.split(", "):
            k, v = item.split(": ")
            d[k] = int(v) if v.isnumeric() else v
        aunts.append(d)

    candidates = set()
    for i in range(len(aunts)):
        possible = True

        for k, v in aunts[i].items():
            if k in tape:
                if k in ["cats", "trees"]:
                    if v <= tape[k]:
                        possible = False 
                         
                elif k in ["pomeranians", "goldfish"]:
                    if v >= tape[k]:
                        possible = False 
                        
                elif v != tape[k]:
                    possible = False 
                    

        if possible:
            candidates.add(i+1)

    # print(candidates)
    return list(candidates)[0]



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
