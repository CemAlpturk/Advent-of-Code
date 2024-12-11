import os
import time
from collections import defaultdict
from functools import lru_cache


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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    stones = list(map(int, lines.strip().split(" ")))
    
    n = 25

    for _ in range(n):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                l = len(str(stone))
                s1 = str(stone)[:l//2]
                s2 = str(stone)[l//2:]
                new_stones.append(int(s1))
                new_stones.append(int(s2))
            else:
                new_stones.append(stone*2024)

        stones = new_stones 

    return len(stones)


@lru_cache
def update_stone(stone: int) -> tuple[int] | tuple[int, int]:
    if stone == 0:
        return 1,
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l = len(s)
        s1 = s[:l//2]
        s2 = s[l//2:]
        return int(s1), int(s2) 
    else:
        return stone * 2024,



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    vals = list(map(int, lines.strip().split(" ")))
    stones = defaultdict(int)
    for val in vals:
        stones[val] += 1
    
    n = 75

    for _ in range(n):
        new_stones = defaultdict(int)
        for stone, c in stones.items():
            vals = update_stone(stone)
            for val in vals:
                new_stones[val] += c 

        stones = new_stones 

    return sum(stones.values())




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
