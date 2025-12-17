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
    speed = {}
    time = {}
    rest = {}

    for line in lines:
        words = line.split(" ") 
        name = words[0] 
        s = int(words[3])
        t = int(words[6])
        r = int(words[-2])

        speed[name] = s
        time[name] = t 
        rest[name] = r 

    t = 2503 
    max_dist = 0 
    for deer in speed.keys():
        tot = time[deer] + rest[deer] 

        k = 2503 // tot 
        c = 2503 % tot 

        dist = k * speed[deer] * time[deer]

        c = min(c, time[deer])
        dist += c * speed[deer]

        max_dist = max(max_dist, dist)

    return max_dist
            


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    speed = {}
    time = {}
    rest = {}

    for line in lines:
        words = line.split(" ") 
        name = words[0] 
        s = int(words[3])
        t = int(words[6])
        r = int(words[-2])

        speed[name] = s
        time[name] = t 
        rest[name] = r 

    t = 2503
    scores = {d: 0 for d in speed.keys()}
    for ti in range(1, t+1):
        dists = {}
        max_dist = 0
        for deer in speed.keys():
            tot = time[deer] + rest[deer] 

            k = ti // tot 
            c = ti % tot 

            dist = k * speed[deer] * time[deer]

            c = min(c, time[deer])
            dist += c * speed[deer]

            dists[deer] = dist
            max_dist = max(max_dist, dist)

        for deer in speed.keys():
            if dists[deer] == max_dist:
                scores[deer] += 1 


    return max(scores.values())
    


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
