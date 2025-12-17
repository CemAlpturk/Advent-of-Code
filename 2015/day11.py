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

def base26(s: str) -> int:
    val = 0 
    for c in s:
        val = val * 26 + (ord(c) - ord("a"))

    return val

def int_to_base26(n: int) -> str:
    if n == 0:
        return "a" * 8

    chars = []
    while n > 0:
        n, r = divmod(n, 26)
        chars.append(chr(r + ord("a")))
    
    while len(chars) < 8:
        chars.append("a")
    
    return "".join(reversed(chars))

def check_password(s: str) -> bool:
    
    # Check increments 
    k1 = False
    for i in range(len(s)-2):
        s1 = ord(s[i])
        s2 = ord(s[i+1])
        s3 = ord(s[i+2])

        if s2 == s1 + 1 and s3 == s2 + 1:
            k1 = True 
            break 

    for i in "iol":
        if i in s:
            return False 

    c = 0 
    i = 0 
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            c += 1 
            i += 2 
        else:
            i += 1 

    return c > 1 and k1




def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    password = lines[0]

    password = int_to_base26(base26(password)+1)

    while not check_password(password):
        password = int_to_base26(base26(password)+1)

    return password 


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)

    password = "cqjxxyzz"

    password = int_to_base26(base26(password)+1)

    while not check_password(password):
        password = int_to_base26(base26(password)+1)
    return password


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
