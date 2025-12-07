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
    banks = [list(map(int, line)) for line in lines]

    tot = 0 
    for bank in banks:
        l = max(bank[:-1])
        l_i = bank.index(l)
        r = max(bank[l_i+1:])

        joltage = 10*l + r 

        tot += joltage

    return tot




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    banks = [list(map(int, line)) for line in lines]
    
    tot = 0 
    n = 12 
    for bank in banks:
        val = ""
        l_i = -1
        for k in reversed(range(n)):
            start = l_i + 1 
            stop = len(bank) - k 
            l = max(bank[start: stop])
            l_i = bank.index(l, start, stop)
            val += str(l)
        
        joltage = int(val)
        tot += joltage 

    return tot


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
