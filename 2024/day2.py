import os


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


def check_levels(levels: list[int]) -> bool:
    incr = levels[0] <= levels[1]
    for i in range(len(levels) - 1):
        x = levels[i]
        y = levels[i + 1]

        d = abs(x - y)
        if d < 1 or d > 3:
            return False

        if incr and x >= y:
            return False

        if not incr and x <= y:
            return False

    return True


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    count = 0

    for line in lines:
        report = list(map(int, line.split(" ")))

        if check_levels(report):
            count += 1

    return count


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    count = 0

    for line in lines:
        report = list(map(int, line.split(" ")))

        check = check_levels(report)

        if check:
            count += 1
        else:

            for i in range(len(report)):
                r = list(report)
                r.pop(i)
                c = check_levels(r)
                if c:
                    count += 1
                    break

    return count


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
