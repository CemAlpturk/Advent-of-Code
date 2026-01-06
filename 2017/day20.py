import os
import time
from tqdm import trange


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

    positions = [] 
    velocities = []
    accelerations = []

    for line in lines:
        p_s, v_s, a_s = line.split(", ")
        p = list(map(int, p_s[3:-1].split(","))) 
        v = list(map(int, v_s[3:-1].split(",")))
        a = list(map(int, a_s[3:-1].split(",")))

        positions.append(p)
        velocities.append(v)
        accelerations.append(a)


    for _ in range(10000):
        for i, (p, v, a) in enumerate(zip(positions, velocities, accelerations)):
            v = [v[0]+a[0], v[1]+a[1], v[2]+a[2]]
            p = [p[0]+v[0], p[1]+v[1], p[2]+v[2]]
            positions[i] = p
            velocities[i] = v 

    dists = list(map(lambda p: abs(p[0])+abs(p[1])+abs(p[2]), positions))
    return dists.index(min(dists))



def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    positions = [] 
    velocities = []
    accelerations = []

    for line in lines:
        p_s, v_s, a_s = line.split(", ")
        p = list(map(int, p_s[3:-1].split(","))) 
        v = list(map(int, v_s[3:-1].split(",")))
        a = list(map(int, a_s[3:-1].split(",")))

        positions.append(p)
        velocities.append(v)
        accelerations.append(a)

    collided = set()
    for _ in trange(10000):
        for i, (p, v, a) in enumerate(zip(positions, velocities, accelerations)):
            if i in collided:
                continue 
            v = [v[0]+a[0], v[1]+a[1], v[2]+a[2]]
            p = [p[0]+v[0], p[1]+v[1], p[2]+v[2]]
            positions[i] = p
            velocities[i] = v 

        for i, p1 in enumerate(positions):
            if i in collided:
                continue
            for j, p2 in enumerate(positions):
                if i == j: 
                    continue 
                if j in collided:
                    continue 

                if p1 == p2:
                    collided.add(i)
                    collided.add(j)

    return len(positions) - len(collided)
                




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
