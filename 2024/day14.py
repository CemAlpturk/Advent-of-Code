import os
import time
import math
import numpy as np
from PIL import Image


def read_input(filename: str) -> str:
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
        data = f.read()

    return data


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    robots = []
    for line in lines.split("\n"):
        if not line:
            continue

        p_str, v_str = line.split(" ")
        p = tuple(map(int, p_str[2:].split(",")))
        v = tuple(map(int, v_str[2:].split(",")))
        robots.append((p, v))

    nx = 101
    ny = 103
    step = 100
    q1, q2, q3, q4 = 0, 0, 0, 0

    for (px, py), (vx, vy) in robots:
        x = (px + step * vx) % nx
        y = (py + step * vy) % ny

        if x == nx // 2 or y == ny // 2:
            continue

        if (x < nx / 2) and (y < ny / 2):
            q1 += 1
        elif (x < nx / 2) and (y > ny / 2):
            q2 += 1
        elif (x > nx / 2) and (y < ny / 2):
            q3 += 1
        elif (x > nx / 2) and (y > ny / 2):
            q4 += 1

    # print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    img_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data/day14/imgs")
    )
    os.makedirs(img_path, exist_ok=True)

    robots = []
    for line in lines.split("\n"):
        if not line:
            continue

        p_str, v_str = line.split(" ")
        p = tuple(map(int, p_str[2:].split(",")))
        v = tuple(map(int, v_str[2:].split(",")))
        robots.append((p, v))

    nx = 101
    ny = 103
    # grid = [["."] * ny for _ in range(nx)]
    seen = set()
    step = 0
    while True:
        # print(step)
        grid = [["."] * nx for _ in range(ny)]
        for (px, py), (vx, vy) in robots:
            x = (px + step * vx) % nx
            y = (py + step * vy) % ny

            grid[y][x] = "#"

        # print("#######")
        # print(step)
        np_grid = np.array(grid) == "#"
        im = Image.fromarray(np_grid)
        im.save(img_path + f"/step_{step}.jpg")

        state = "\n".join(["".join(row) for row in grid])
        # print(state)
        # print("#######")
        if state in seen:
            print(step)
            break
        seen.add(state)
        step += 1
        # input()

    print(state)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
