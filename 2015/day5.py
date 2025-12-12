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


def is_good(s: str) -> bool:
    vowels = "aeiou"
    no = {"ab", "cd", "pq", "xy"}

    c_v = 0
    c_d = 0
    for i in range(len(s)-1):
        # Vowel check 
        if s[i] in vowels:
            c_v += 1 

        if s[i] == s[i+1]:
            c_d += 1 

        if s[i:i+2] in no:
            return False

    c_v += s[-1] in vowels

    if c_v < 3:
        return False 

    if c_d == 0:
        return False 

    return True


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename) 
    return sum(map(is_good, lines))


def is_nice(s: str) -> bool:
    
    p1 = False 

    for i in range(len(s) - 1):
        s1 = s[i:i+2]
        if s1 in s[i+2:]:
            p1 = True 
            break

    p2 = False
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            p2 = True 
            break 

    return p1 and p2  



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    return sum(map(is_nice, lines))


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
