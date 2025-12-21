import os
import time
import hashlib 


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
    door_id = lines[0] 
    target = "0" * 5
    x = 0
    password = ""
    while len(password) < 8:
        s = door_id + str(x)
        res = hashlib.md5(s.encode()).hexdigest()
        if res[:5] == target:
            password += res[5]
            # print(s, res, password)
        x += 1

    return password




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    door_id = lines[0] 
    target = "0" * 5 
    x = 0 
    password = ["-"] * 8
    while "-" in password:
        s = door_id + str(x) 
        res = hashlib.md5(s.encode()).hexdigest()
        if res[:5] == target and int(res[5], 16) < 8 and password[int(res[5])] == "-":
            password[int(res[5])] = res[6]
            # print(s, res, password)

        x += 1

    return "".join(password)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
