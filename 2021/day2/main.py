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

    depth = 0
    pos = 0

    for line in lines:
        line = line.strip("\n")
        command, num = line.split(" ")

        if command == "forward":
            pos += int(num)
        elif command == "down":
            depth += int(num)
        elif command == "up":
            depth -= int(num)

    val = depth * pos
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    depth = 0
    pos = 0
    aim = 0

    for line in lines:
        line = line.strip("\n")
        command, num = line.split(" ")
        num = int(num)

        if command == "forward":
            pos += num
            depth += aim * num
        elif command == "down":
            aim += num
        elif command == "up":
            aim -= num

    val = depth * pos
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
