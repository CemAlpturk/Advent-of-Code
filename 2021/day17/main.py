import os


def read_input(filename: str) -> list[str]:

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip("\n") for line in lines]


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    line = read_input(filename)[0][13:]
    xs, ys = line.split(",")
    xmin, xmax = tuple(map(int, xs.split("=")[1].split("..")))
    ymin, ymax = tuple(map(int, ys.split("=")[1].split("..")))
    # print(xmin, xmax)
    # print(ymin, ymax)
    y0_max = -ymin - 1
    x0 = 0
    while (x0 * (x0 + 1)) / 2 < xmin:
        x0 += 1

    x0_min = x0
    x0_max = xmax

    y0 = y0_max

    while y0 > 0:

        for x0 in range(x0_min, x0_max + 1):
            # Simulate traj
            x, y = 0, 0
            vx = x0
            vy = y0
            while y >= ymin:
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1

                if xmin <= x <= xmax and ymin <= y <= ymax:
                    return y0 * (y0 + 1) / 2
    return -1


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    line = read_input(filename)[0][13:]
    xs, ys = line.split(",")
    xmin, xmax = tuple(map(int, xs.split("=")[1].split("..")))
    ymin, ymax = tuple(map(int, ys.split("=")[1].split("..")))
    # print(xmin, xmax)
    # print(ymin, ymax)
    y0_max = -ymin - 1
    x0 = 0
    while (x0 * (x0 + 1)) / 2 < xmin:
        x0 += 1

    x0_min = x0
    x0_max = xmax

    y0 = y0_max
    count = 0
    while y0 >= ymin:

        for x0 in range(x0_min, x0_max + 1):
            # Simulate traj
            x, y = 0, 0
            vx = x0
            vy = y0
            while y >= ymin:
                x += vx
                y += vy
                vx = max(0, vx - 1)
                vy -= 1

                if xmin <= x <= xmax and ymin <= y <= ymax:
                    count += 1
                    break

        y0 -= 1
    return count


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
