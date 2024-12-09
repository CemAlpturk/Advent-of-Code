import os
import time


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
    line = lines.strip()

    ids = []
    for i, v in enumerate(line):
        if i % 2 == 0:
            id = i // 2
            ids.extend([str(id)] * int(v))
        else:
            ids.extend(["."] * int(v))

    # ids = [v for v in ids]
    # print("".join(ids))
    p0 = ids.index(".")
    p1 = len(ids) - 1
    while ids[p1] == ".":
        p1 -= 1
    # print(p0, p1)
    # print(ids[p0], ids[p1])

    while p0 < p1:
        # Swap
        ids[p0], ids[p1] = ids[p1], ids[p0]

        while ids[p0] != ".":
            p0 += 1

        while ids[p1] == ".":
            p1 -= 1

        # print("".join(ids))

    # print("".join(ids))

    checksum = 0
    for i, v in enumerate(ids):
        checksum += i * int(v) if v != "." else 0

    return checksum


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    line = lines.strip()

    ids = []
    id_set = set()
    for i, v in enumerate(line):
        if i % 2 == 0:
            id = i // 2
            ids.extend([str(id)] * int(v))
            id_set.add(id)
        else:
            ids.extend(["."] * int(v))

    n = len(ids)
    # print("".join(ids))
    while id_set:
        # Select max id
        curr_id = max(id_set)
        id_set.remove(curr_id)

        # Get block start index
        block_start = ids.index(str(curr_id))
        block_end = block_start
        while block_end < n and ids[block_end] == str(curr_id):
            block_end += 1

        n_block = block_end - block_start

        # Find available space
        i = 0
        while i < block_start:
            if ids[i : i + n_block] == ["."] * n_block:
                ids[i : i + n_block] = [str(curr_id)] * n_block
                ids[block_start:block_end] = ["."] * n_block
                break
            i += 1

        # print("".join(ids))

    checksum = 0
    for i, v in enumerate(ids):
        checksum += i * int(v) if v != "." else 0

    return checksum


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
