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


Cell = tuple[int, int]
Shape = set[Cell]

def parse_input(lines: list[str]) -> tuple[list[Shape], list[tuple[int, int]], list[tuple[int, ...]]]:
    shapes: list[Shape] = []
    trees: list[tuple[int, int]] = []
    gifts: list[tuple[int, ...]] = []

    l = 0 
    shape: Shape = set()
    while True:
        if lines[l][0].isnumeric() and lines[l][-1] != ":":
            break

        if lines[l][-1] == ":":
            shape = set()

        # Get number of lines 
        s = lines.index("", l)

        for i, line in enumerate(lines[l+1:s]):
            for j, v in enumerate(line):
                if v == "#":
                    shape.add((i, j))
        shapes.append(shape)
        l = s + 1

    for line in lines[l:]:
        grid = tuple(map(int, line.split(":")[0].split("x")))
        trees.append(grid)  # type: ignore
        gift = tuple(map(int, [x for x in line.split(":")[1].split(" ") if x]))
        gifts.append(gift)

    return shapes, trees, gifts



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    shapes, trees, giftss = parse_input(lines)

    count = 0 
    for tree, gifts in zip(trees, giftss):
        grid_area = tree[0] * tree[1]
        gifts_area = 0 
        for i, gift in enumerate(gifts):
            gifts_area += gift * len(shapes[i])

        if gifts_area <= grid_area:
            count += 1 

    return count


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
