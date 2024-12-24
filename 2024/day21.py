import os
import time
import numpy as np


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


def numpad_to_keypad(
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[list[str], tuple[int, int]]:
    d = (end_pos[0] - start[0], end_pos[1] - start[1])

    # Cannot pass through (3, 0)
    moves = []
    if d[0] > 0:
        moves.extend(["v"] * d[0])
    elif d[0] < 0:
        moves.extend(["^"] * -d[0])

    if d[1] > 0:
        moves.extend([">"] * d[1])
    if d[1] < 0:
        moves.extend(["<"] * -d[1])

    moves.append("A")

    return moves, end_pos


def part1():
    filename = "part1-test.txt"
    # filename = "part1.txt"

    lines = read_input(filename)
    nums = [line.strip() for line in lines.split("\n") if line]

    numpad = np.array(
        [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
    )
    keypad = np.array([["", "^", "A"], ["<", "v", ">"]])
    total_score = 0
    for num in nums:
        p1 = (3, 2)
        p2 = (0, 2)
        p3 = (0, 2)
        p4 = (0, 2)

        moves = []
        for n in num:
            goal_pos = list(
                map(lambda x: (x[0].item(), x[1].item()), zip(*np.where(numpad == n)))
            )[0]
            m, p1 = numpad_to_keypad(numpad, p1, n)
            moves.extend(m)

        print("".join(moves))

        moves1 = []
        for n in moves:
            m, p2 = numpad_to_keypad(keypad, p2, n)
            moves1.extend(m)

        print("".join(moves1))

        moves2 = []
        for n in moves1:
            m, p3 = numpad_to_keypad(keypad, p3, n)
            moves2.extend(m)

        print("".join(moves2))

        moves3 = []
        for n in moves2:
            m, p4 = numpad_to_keypad(keypad, p4, n)
            moves3.extend(m)

        # print("".join(moves3))
        l = len(moves3)
        val = int("".join([v for v in num if v.isnumeric()]))
        score = l * val
        print(num, l, val, score)

        total_score += score
        return

    return total_score


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
