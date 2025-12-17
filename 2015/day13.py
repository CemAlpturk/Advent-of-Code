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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    weights = {} 
    ppl = set()
    for line in lines:
        words = line.split(" ")
        u = words[0]
        v = words[-1][:-1]
        w = int(words[3])

        if words[2] == "lose":
            w = -w 

        weights[(u, v)] = w 
        ppl.add(u)
        ppl.add(v)

    best = -float("inf")
    for perm in permutations(ppl):
        score = 0
        for i in range(len(perm)):
            u = perm[i]
            v = perm[(i-1) % len(perm)]
            w = perm[(i+1) % len(perm)]

            score += weights[(u,v)] + weights[(u,w)]
        
        best = max(best, score)

    return best



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    weights = {} 
    ppl = set()
    ppl.add("me")
    for line in lines:
        words = line.split(" ")
        u = words[0]
        v = words[-1][:-1]
        w = int(words[3])

        if words[2] == "lose":
            w = -w 

        weights[(u, v)] = w 
        weights[(u,"me")] = 0
        weights[("me", u)] = 0
        weights[(v, "me")] = 0
        weights[("me", v)] = 0
        ppl.add(u)
        ppl.add(v)


    best = -float("inf")
    for perm in permutations(ppl):
        score = 0
        for i in range(len(perm)):
            u = perm[i]
            v = perm[(i-1) % len(perm)]
            w = perm[(i+1) % len(perm)]

            score += weights[(u,v)] + weights[(u,w)]
        
        best = max(best, score)

    return best
    

if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
