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


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    fish_times = [int(val) for val in lines[0].split(",")]

    n_days = 80
    for step in range(n_days):
        new_fish = []
        for i in range(len(fish_times)):
            if fish_times[i] == 0:
                fish_times[i] = 6
                new_fish.append(8)
            else:
                fish_times[i] -= 1

        fish_times.extend(new_fish)

    val = len(fish_times)
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    fish_times = [int(val) for val in lines[0].split(",")]

    times = [0] * 9
    for fish in fish_times:
        times[fish] += 1

    n_days = 256
    for step in range(1, n_days + 1):
        n = times[0]
        times = times[1:] + [n]
        times[6] += n

    val = sum(times)
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
