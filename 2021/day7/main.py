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

    nums = [int(val) for val in lines[0].split(",")]
    nums.sort()
    m = nums[len(nums) // 2]
    dists = [abs(m - n) for n in nums]

    val = sum(dists)
    print(f"Part1: {val}")


def calculate_dists(nums: list[int], pos: int) -> int:
    sum = 0
    for num in nums:
        d = abs(pos - num)
        sum += d * (d + 1) / 2

    return int(sum)


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    nums = [int(val) for val in lines[0].split(",")]
    minnum = min(nums)
    maxnum = max(nums)

    min_fuel = float("inf")
    for x in range(minnum, maxnum + 1):
        min_fuel = min(min_fuel, calculate_dists(nums, x))

    val = min_fuel
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
