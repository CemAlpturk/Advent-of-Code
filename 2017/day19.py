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
    grid = []
    for line in lines:
        grid.append(list(line))


    n = len(grid)
    m = len(grid[0])
    start = (0, grid[0].index("|"))
    dir = (1, 0)

    path = ""

    pos = start 
    while True:
        x, y = pos
        if not(0 <= x < n and 0 <= y < m):
            break
        dx, dy = dir
        v = grid[x][y]
        if v == " ":
            break
        path += v

        if v == "+":
            if dx == 0:
                if x > 0 and grid[x-1][y] != " ":
                    dx = -1
                    dy = 0
                else:
                    dx = 1 
                    dy = 0
            else:
                if y > 0 and grid[x][y-1] != " ":
                    dy = -1 
                    dx = 0
                else:
                    dy = 1  
                    dx = 0
        pos = (x + dx, y + dy)
        dir = (dx, dy)
    
    path = path.replace("|", "").replace("+", "").replace("-", "")

    return path





def part2():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = []
    for line in lines:
        grid.append(list(line))


    n = len(grid)
    m = len(grid[0])
    start = (0, grid[0].index("|"))
    dir = (1, 0)

    steps = 0
    pos = start 
    while True:
        x, y = pos
        if not(0 <= x < n and 0 <= y < m):
            break
        dx, dy = dir
        v = grid[x][y]
        if v == " ":
            break

        if v == "+":
            if dx == 0:
                if x > 0 and grid[x-1][y] != " ":
                    dx = -1
                    dy = 0
                else:
                    dx = 1 
                    dy = 0
            else:
                if y > 0 and grid[x][y-1] != " ":
                    dy = -1 
                    dx = 0
                else:
                    dy = 1  
                    dx = 0
        pos = (x + dx, y + dy)
        dir = (dx, dy)
        steps += 1 
    

    return steps



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
