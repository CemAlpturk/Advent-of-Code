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


def compositions(n: int, m: int):
    if n == 1:
        yield (m,)
        return 

    for i in range(m+1):
        for rest in compositions(n-1, m-i):
            yield (i,) + rest 



def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    ingredients = {} 
    for line in lines:
        name = line.split(":")[0]
        words = line.split(" ")

        capacity = int(words[2][:-1])
        durability = int(words[4][:-1])
        flavor = int(words[6][:-1])
        texture = int(words[8][:-1])
        # calories = int(words[-1][:-1])

        ingredients[name] = (capacity, durability, flavor, texture)

    n = len(ingredients)
    m = 100 
    best_score = 0
    for comp in compositions(n, m):
        score = 1
        for i in range(4):
            s = 0
            for ingredient, c in zip(ingredients.values(), comp):
                s += ingredient[i]*c
            score *= max(0, s)
        best_score = max(best_score, score)


    return best_score



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    ingredients = {} 
    for line in lines:
        name = line.split(":")[0]
        words = line.split(" ")

        capacity = int(words[2][:-1])
        durability = int(words[4][:-1])
        flavor = int(words[6][:-1])
        texture = int(words[8][:-1])
        calories = int(words[-1])

        ingredients[name] = (capacity, durability, flavor, texture, calories)

    n = len(ingredients)
    m = 100 
    cal = 500
    best_score = 0
    for comp in compositions(n, m):
        score = 1
        for i in range(4):
            s = 0
            for ingredient, c in zip(ingredients.values(), comp):
                s += ingredient[i]*c
            score *= max(0, s)

        calories = 0
        for ingredient, c in zip(ingredients.values(), comp):
            calories += ingredient[-1] * c 
        if calories == cal:
            best_score = max(best_score, score)


    return best_score

    


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
