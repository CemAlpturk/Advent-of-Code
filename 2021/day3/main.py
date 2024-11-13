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

    n = len(lines[0]) - 1
    zeros = [0] * n
    ones = [0] * n

    for line in lines:
        line = line.strip("\n")
        for i, c in enumerate(line):
            if c == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    gamma_rates = [0 if zeros[i] > ones[i] else 1 for i in range(n)]
    epsilon_rates = [1 if zeros[i] > ones[i] else 0 for i in range(n)]

    gamma_rate = 0
    epsilon_rate = 0

    for bit in gamma_rates:
        gamma_rate = (gamma_rate << 1) | bit

    for bit in epsilon_rates:
        epsilon_rate = (epsilon_rate << 1) | bit

    val = gamma_rate * epsilon_rate
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    # Oxygen generator
    choices = [line.strip("\n") for line in lines]
    n = len(choices[0])
    for idx in range(n):
        zeros = 0
        ones = 0
        for line in choices:
            if line[idx] == "0":
                zeros += 1
            else:
                ones += 1

        c = "0" if zeros > ones else "1"

        choices = [line for line in choices if line[idx] == c]

    assert len(choices) == 1
    oxy_bits = choices[0]
    ox = 0
    for bit in oxy_bits:
        ox = (ox << 1) | int(bit)

    # C02 scrubber
    choices = [line.strip("\n") for line in lines]
    for idx in range(n):
        zeros = 0
        ones = 0
        for line in choices:
            if line[idx] == "0":
                zeros += 1
            else:
                ones += 1

        c = "1" if zeros > ones else "0"
        choices = [line for line in choices if line[idx] == c]
        if len(choices) == 1:
            break

    assert len(choices) == 1
    co2_bits = choices[0]
    co = 0
    for bit in co2_bits:
        co = (co << 1) | int(bit)

    val = ox * co
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
