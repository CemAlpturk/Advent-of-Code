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
    n = len(lines)
    m = len(lines[0])

    count = 0 
    for i in range(n):
        for j in range(m):
            if lines[i][j] == ".":
                continue 

            c = 0
            
            c += i > 0 and lines[i-1][j] == "@"
            c += i < n-1 and lines[i+1][j] == "@" 
            c += j > 0 and lines[i][j-1] == "@"
            c += j < m-1 and lines[i][j+1] == "@"
            
            c += (i > 0 and j > 0) and lines[i-1][j-1] == "@" 
            c += (i > 0 and j < m-1) and lines[i-1][j+1] == "@" 
            c += (i < n-1 and j > 0) and lines[i+1][j-1] == "@"
            c += (i < n-1 and j < m-1) and lines[i+1][j+1] == "@" 

            count += c < 4 

    return count


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    lines = [[x for x in line] for line in lines]
    n = len(lines)
    m = len(lines[0])
    count = 0 
    while True:
        rolls = set()
        for i in range(n):
            for j in range(m):
                if lines[i][j] == ".":
                    continue 

                c = 0
            
                c += i > 0 and lines[i-1][j] == "@"
                c += i < n-1 and lines[i+1][j] == "@" 
                c += j > 0 and lines[i][j-1] == "@"
                c += j < m-1 and lines[i][j+1] == "@"
            
                c += (i > 0 and j > 0) and lines[i-1][j-1] == "@" 
                c += (i > 0 and j < m-1) and lines[i-1][j+1] == "@" 
                c += (i < n-1 and j > 0) and lines[i+1][j-1] == "@"
                c += (i < n-1 and j < m-1) and lines[i+1][j+1] == "@" 

                if c < 4:
                    count += 1 
                    rolls.add((i, j))

        # Remove selected rolls 
        if len(rolls) == 0:
            break 

        for (x, y) in rolls:
            lines[x][y] = "." 

    return count

if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
