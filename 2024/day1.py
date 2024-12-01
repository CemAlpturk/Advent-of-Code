import os
from collections import defaultdict


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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    nums1, nums2 = [], []

    for line in lines:
        n1, n2 = line.split("   ")
        nums1.append(int(n1))
        nums2.append(int(n2))

    nums1.sort()
    nums2.sort()

    diffs = [abs(n2 - n1) for n1, n2 in zip(nums1, nums2)]

    return sum(diffs)


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    nums1 = []
    nums2 = defaultdict(lambda: 0)

    for line in lines:
        n1, n2 = line.split("   ")
        nums1.append(int(n1))
        nums2[int(n2)] += 1

    score = 0
    for n in nums1:
        score += n * nums2[n]

    return score


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
