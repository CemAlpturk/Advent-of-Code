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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    n = 100
    pos = 50
    count = 0
    for line in lines:
        d = line[0]
        k = int(line[1:])

        if d == "R":
            pos += k
        else:
            pos -= k 

        pos %= n 

        count += pos == 0 

    return count


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    n = 100 
    pos = 50 
    count = 0 
    for line in lines:
        d = line[0] 
        k = int(line[1:])

        t = k // n 
        k %= n  

        if d == "R":
            new_pos = (pos + k) % n 
            count += t + (new_pos < pos)
        else:
            new_pos = (pos - k) % n 
            count += t + (pos < new_pos)
            count -= pos == 0
            count += new_pos == 0

        pos = new_pos

    return count




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
