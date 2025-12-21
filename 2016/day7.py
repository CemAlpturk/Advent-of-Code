import os
import time
import re


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


def is_abba(s: str) -> bool:
    if len(s) < 4:
        return False 

    return any(a == d and b == c and a != b for a, b, c, d in zip(s, s[1:], s[2:], s[3:]))

def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt" 

    lines = read_input(filename)
    count = 0
    regex = re.compile(r"\[[^\[\]]*\]|[^\[\]]+")
    for line in lines:
        parts = re.findall(regex, line)
        # print(parts)
        line_ok = False
        # print(parts) 
        for part in parts:
            if part.startswith("["):
                if is_abba(part[1:-1]):
                    line_ok = False
                    break 
            else:
                if is_abba(part):
                    line_ok = True 
                    
        # print(line_ok)
        count += line_ok
        

    return count


def get_triplets(s: str) -> list[str]:
    return list(a + b + c for a, b, c in zip(s, s[1:], s[2:]) if a != b and a == c)

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    count = 0
    regex = re.compile(r"\[[^\[\]]*\]|[^\[\]]+")
    for line in lines:
        parts = re.findall(regex, line)
        supernet = [part for part in parts if not part.startswith("[")]
        hypernet = [part for part in parts if part.startswith("[")]

        is_ok = False 
        for part in supernet:
            for a, b, _ in get_triplets(part):
                target = b + a + b
                for p in hypernet:
                    if target in p:
                        is_ok = True 
                        break 

                if is_ok:
                    break 
            if is_ok:
                break 
        count += is_ok 

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
