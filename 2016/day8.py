import os
import time
import numpy as np 


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

def rotate(x: np.ndarray, k: int) -> np.ndarray:
    y = np.zeros_like(x)
    n = len(x)
    for i in range(len(x)):
        idx = (i + k) % n 
        y[idx] = x[i] 
    return y 


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n, m = 6, 50
    # n, m = 3, 7
    screen = np.zeros((n, m), dtype=bool)

    for line in lines:
        words = line.split(" ")
        if words[0] == "rect":
            y, x = map(int, words[1].split("x"))
            screen[:x, :y] = True 

        elif words[0] == "rotate":
            if words[1] == "column":
                col_num = int(words[2].split("=")[-1])
                y = int(words[-1]) % n 
                screen[:, col_num] = rotate(screen[:, col_num], y)
            elif words[1] == "row":
                row_num = int(words[2].split("=")[-1])
                x = int(words[-1]) % m
                screen[row_num] = rotate(screen[row_num], x)

    return np.sum(screen)


def print_screen(screen: np.ndarray):
    n, m = screen.shape 
    for i in range(n):
        r = ""
        for j in range(m):
            if screen[i, j]:
                r += "#"
            else:
                r += " "
        print(r)




def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    n, m = 6, 50
    # n, m = 3, 7
    screen = np.zeros((n, m), dtype=bool)

    for line in lines:
        words = line.split(" ")
        if words[0] == "rect":
            y, x = map(int, words[1].split("x"))
            screen[:x, :y] = True 

        elif words[0] == "rotate":
            if words[1] == "column":
                col_num = int(words[2].split("=")[-1])
                y = int(words[-1]) % n 
                screen[:, col_num] = rotate(screen[:, col_num], y)
            elif words[1] == "row":
                row_num = int(words[2].split("=")[-1])
                x = int(words[-1]) % m
                screen[row_num] = rotate(screen[row_num], x)

    print_screen(screen)




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
