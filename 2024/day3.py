import os


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
        # lines = f.readlines()
        line = f.read().strip()

    return line

    # return [line.strip("\n") for line in lines]


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    line = read_input(filename)
    total = 0
    for i in range(len(line)):
        chunk = line[i:]

        if not chunk.startswith("mul("):
            continue

        chunk = chunk[4:]

        try:
            subchunk = chunk.split(")", 1)[0]
            pair = subchunk.split(",")
            a = int(pair[0])
            b = int(pair[1])
            total += a * b

        except:
            continue

    return total


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    line = read_input(filename)

    total = 0
    do = True

    for i in range(len(line)):
        chunk = line[i:]

        if chunk.startswith("do()"):
            do = True
        elif chunk.startswith("don't()"):
            do = False

        if not chunk.startswith("mul("):
            continue

        chunk = chunk[4:]

        try:
            subchunk = chunk.split(")", 1)[0]
            pair = subchunk.split(",")
            a = int(pair[0])
            b = int(pair[1])
            if do:
                total += a * b
        except:
            continue

    return total


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
