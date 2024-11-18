import os
from itertools import permutations


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

    count = 0
    for line in lines:
        digits = line.split(" | ")[1].split(" ")
        for digit in digits:
            if len(digit) in (2, 3, 4, 7):
                count += 1

    val = count
    print(f"Part1: {val}")


def infer_wiring(digits: list[str]) -> dict[str, int]:
    nums = {}
    nums_inv = {}
    # Extract obvious ones
    for digit in digits:
        l = len(digit)
        if l == 7:
            nums[digit] = 8
            nums_inv[8] = digit
        elif l == 4:
            nums[digit] = 4
            nums_inv[4] = digit
        elif l == 3:
            nums[digit] = 7
            nums_inv[7] = digit
        elif l == 2:
            nums[digit] = 1
            nums_inv[1] = digit

    # Find 3
    for digit in digits:
        if digit in nums or len(digit) != 5:
            continue
        one = nums_inv[1]
        found = True
        for i in one:
            if i not in digit:
                found = False

        if found:
            nums[digit] = 3
            nums_inv[3] = digit

    return nums


def letter_permutations():
    letters = "abcdefg"
    for perm in permutations(letters):
        yield "".join(perm)


nums = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
nums_inv = {v: k for k, v in nums.items()}


def brute_force(digits: list[str]) -> dict[str, str]:

    bools = {}
    bools_inv = {}
    for k, v in nums.items():
        val = tuple(x in v for x in "abcdefg")
        bools[k] = val
        bools_inv[val] = k

    for config in letter_permutations():
        found = True
        for digit in digits:
            val = tuple(c in digit for c in config)
            if val not in bools_inv:
                found = False
                break

        if found:
            break

    mapping = {x: y for x, y in zip(config, "abcdefg")}
    return mapping


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    sum = 0
    for line in lines:
        digits = line.split(" | ")[0].split(" ")
        # print(nums)
        mapping = brute_force(digits)
        # print(mapping)
        vals = line.split(" | ")[1].split(" ")
        s = ""
        for val in vals:
            mapped_val = [mapping[i] for i in val]
            mapped_val.sort()
            mapped_val = "".join(mapped_val)
            # print(val, mapped_val)
            s += str(nums_inv[mapped_val])

        sum += int(s)
        # print(s)
        # break

    val = sum
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
