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

    return lines


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    depths = [int(val.strip("\n")) for val in lines]

    num_incr = 0

    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            num_incr += 1

    print(f"Part1: {num_incr}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    depths = [int(val.strip("\n")) for val in lines]

    sums = []
    for i in range(len(depths) - 2):
        sums.append(depths[i] + depths[i + 1] + depths[i + 2])

    counts = 0
    for i in range(len(sums) - 1):
        if sums[i] < sums[i + 1]:
            counts += 1

    print(f"Part2: {counts}")


if __name__ == "__main__":
    part1()
    part2()
