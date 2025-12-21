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


BUTTONS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    p = [1, 1]
    code = []
    for line in lines:
        for v in line:
            if v == "U":
                p[0] -= 1 if p[0] > 0 else 0
            elif v == "D":
                p[0] += 1 if p[0] < 2 else 0
            elif v == "L":
                p[1] -= 1 if p[1] > 0 else 0
            else:
                p[1] += 1 if p[1] < 2 else 0

        code.append(str(BUTTONS[p[0]][p[1]]))

    return "".join(code)


NEW_BUTTONS = [
    ["_", "_", "1", "_", "_"],
    ["_", "2", "3", "4", "_"],
    ["5", "6", "7", "8", "9"],
    ["_", "A", "B", "C", "_"],
    ["_", "_", "D", "_", "_"],
]

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    p = [2, 0]
    code = [] 
    for line in lines:
        for v in line:
            if v == "U":
                if p[0] > 0 and NEW_BUTTONS[p[0] - 1][p[1]] != "_":
                    p[0] -= 1 
            elif v == "D":
                if p[0] < 4 and NEW_BUTTONS[p[0] + 1][p[1]] != "_":
                    p[0] += 1 
            elif v == "L":
                if p[1] > 0 and NEW_BUTTONS[p[0]][p[1] - 1] != "_":
                    p[1] -= 1 
            else:
                if p[1] < 4 and NEW_BUTTONS[p[0]][p[1] + 1] != "_":
                    p[1] += 1 
        
        code.append(NEW_BUTTONS[p[0]][p[1]])

    return "".join(code)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
