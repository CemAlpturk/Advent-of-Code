import os
import time
from itertools import permutations
from tqdm import tqdm
from functools import lru_cache
from collections import defaultdict


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
        data = f.read()

    return data


@lru_cache
def gen_num(x: int) -> int:
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    nums = [int(line.strip()) for line in lines.split("\n") if line]

    total_steps = 2000
    sum = 0
    for num in nums:
        v = num
        for _ in range(total_steps):
            num = gen_num(num)

        sum += num

        # print(f"{v}: {num}")

    return sum


def simulate(
    nums: list[int],
    steps: int,
) -> tuple[list[int], list[list[tuple[int, int]]]]:
    final_numbers = []
    deltas = []
    for num in tqdm(nums):
        prices = [num % 10]
        for _ in range(steps):
            num = gen_num(num)
            prices.append(num % 10)
            changes = [
                (second - first, second) for first, second in zip(prices, prices[1:])
            ]
            final_numbers.append(num)
            deltas.append(changes)
    return final_numbers, deltas


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    nums = [int(line.strip()) for line in lines.split("\n") if line]

    total_steps = 2000
    final_numbers, deltas = simulate(nums, total_steps)

    bananas = defaultdict(int)
    for changes in tqdm(deltas):
        seen = set()
        for i in range(len(changes) - 3):
            sequence = tuple(change[0] for change in changes[i : i + 4])
            if sequence not in seen:
                bananas[sequence] += changes[i + 3][1]
                seen.add(sequence)
    return max(bananas.values())


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
