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

    s = read_input(filename)[0]
    n = len(s)

    garbage = False 
    ignore = False 
    score = 0 
    score_depth = 0
    garbage_chars = 0

    for char in s:
        if not garbage:
            if char == "}":
                score += score_depth 
            score_depth += (char == "{") - (char == "}")
            garbage = char == "<"
        elif not ignore:
            garbage = char != ">"
            ignore = char == "!"
            garbage_chars += char != ">" and char != "!"
        else:
            ignore = False 

    return score, garbage_chars

    



def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
