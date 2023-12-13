def diff(values: list[int]):
    check = True
    for val in values:
        if val != 0:
            check = False
            break
    if check:
        return 0

    diffs = [values[i] - values[i - 1] for i in range(1, len(values))]

    next_val = diffs[-1] + diff(diffs)
    return next_val


def part1(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    values = [[int(val) for val in line.split(" ")] for line in lines]

    next_vals = [vals[-1] + diff(vals) for vals in values]
    print(sum(next_vals))


def part2(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    values = [[int(val) for val in line.split(" ")] for line in lines]

    # Invert values
    values = [[val for val in reversed(vals)] for vals in values]

    next_vals = [vals[-1] + diff(vals) for vals in values]
    print(sum(next_vals))


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
