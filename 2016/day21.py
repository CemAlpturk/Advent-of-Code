import os
import time
from itertools import permutations


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


def scramble(operation: str, password: list[str]) -> list[str]:
    words = operation.split(" ") 
    if words[0] == "swap" and words[1] == "position":
        i = int(words[2])
        j = int(words[-1])
        password[i], password[j] = password[j], password[i] 
    elif words[0] == "swap" and words[1] == "letter":
        c = words[2]
        d = words[-1]
        for i, s in enumerate(password):
            if s == c:
                password[i] = d
            elif s == d:
                password[i] = c 

    elif words[0] == "rotate" and words[1] != "based":
        n = int(words[2])
        if words[1] == "left":
            n = -n 
            
        n %= len(password)
        password = password[-n:] + password[:-n]

    elif words[0] == "rotate" and words[1] == "based":
        u = words[-1]
        idx = password.index(u)
        n = 1 + idx + (idx >= 4)
        n %= len(password)
        password = password[-n:] + password[:-n]

    elif words[0] == "reverse":
        i = int(words[2])
        j = int(words[-1])

        password = password[:i] + password[i:j+1][::-1] + password[j+1:]

    elif words[0] == "move":
        i = int(words[2])
        j = int(words[-1])

        v = password.pop(i)
        password.insert(j, v)
    
    return password


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    password = list("abcdefgh")

    for operation in lines:
          password = scramble(operation, password)   
    return "".join(password)




def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    target = list("fbgdceah")

    for password in permutations("abcdefgh"):
        ps = list(password)
        for operation in lines:
            ps = scramble(operation, ps)
        if ps == target:
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
