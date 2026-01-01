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
    moves = lines[0].split(",")

    n = 16 
    progs = list(range(n))

    for move in moves:
        if move[0] == "s":
            i = int(move[1:])
            progs = progs[-i:] + progs[:-i]
        elif move[0] == "x":
            i, j = map(int, move[1:].split("/"))
            progs[i], progs[j] = progs[j], progs[i] 

        elif move[0] == "p":
            ki, kj = move[1:].split("/")
            ki = ord(ki) - ord("a")
            kj = ord(kj) - ord("a")
            i = progs.index(ki)
            j = progs.index(kj)
            progs[i], progs[j] = progs[j], progs[i]
        else:
            raise ValueError

    return "".join(chr(ord("a") + p) for p in progs)


def to_str(ps: list[int]) -> str:
    return "".join(chr(ord("a") + p) for p in ps)


def dance(progs: list[int], moves: list[str]) -> list[int]:
    for move in moves:
        if move[0] == "s":
            i = int(move[1:])
            progs = progs[-i:] + progs[:-i]
        elif move[0] == "x":
            i, j = map(int, move[1:].split("/"))
            progs[i], progs[j] = progs[j], progs[i] 

        elif move[0] == "p":
            ki, kj = move[1:].split("/")
            ki = ord(ki) - ord("a")
            kj = ord(kj) - ord("a")
            i = progs.index(ki)
            j = progs.index(kj)
            progs[i], progs[j] = progs[j], progs[i]
        else:
            raise ValueError

    return progs


def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    moves = lines[0].split(",")

    n = 16 
    progs = list(range(n))

    k = 1000000000
    seen = set()
    i = 0 

    while to_str(progs) not in seen:
        seen.add(to_str(progs))
        progs = dance(progs, moves)
        i += 1 

    t = k % i 

    for _ in range(t):
        progs = dance(progs, moves)


    return "".join(chr(ord("a") + p) for p in progs)



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
