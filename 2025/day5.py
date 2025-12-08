import os
import time


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


def process_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    reached_items = False 
    ranges = []
    items = []
    for line in lines:
        if line == "":
            reached_items = True 
            continue 

        if reached_items:
            items.append(int(line))
        else:
            ranges.append(tuple(map(int, line.split("-"))))

    return ranges, items


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    ranges, items = process_input(lines)

    count = 0 
    for i in items:
        for x, y in ranges:
            if x <= i <= y:
                count += 1 
                break 
    return count



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    ranges, _ = process_input(lines)

    events = []
    for x, y in ranges:
        events.append((x, 1))
        events.append((y+1, -1))

    events = sorted(events)

    active = 0
    prev_x = None
    covered = 0 

    for x, delta in events:
        if active > 0:
            covered += x - prev_x

        active += delta 
        prev_x = x 

    return covered


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
