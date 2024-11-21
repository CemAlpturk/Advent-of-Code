import os
import string
from collections import Counter


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
    polymer = lines[0]

    rules = {}
    for line in lines[2:]:
        pair, r = line.split(" -> ")
        rules[pair] = r

    n_steps = 10
    for step in range(1, n_steps + 1):
        s = polymer[0]
        for i, j in zip(polymer[:-1], polymer[1:]):
            pair = i + j
            r = rules.get(pair, "")
            s += r + j
        polymer = s

    counts = {}
    for i in polymer:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    maxval = max(counts.values())
    minval = min(counts.values())

    val = maxval - minval
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    polymer = lines[0]

    rules = [rule.split(" ") for rule in lines[2:]]
    rules = {a: (a[0] + c, c + a[1]) for a, _, c in rules}
    pairs = ["".join(p) for p in zip(polymer, polymer[1:])]

    steps = 40
    ctr = Counter(pairs)
    for i in range(steps):
        newCtr = {key: 0 for key in rules.keys()}
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value

        ctr = newCtr

    letterTotals = {letter: 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letterTotals[key[0]] += value

    letterTotals[polymer[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    val = lmax - lmin

    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
