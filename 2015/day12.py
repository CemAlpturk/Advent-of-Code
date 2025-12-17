import os
import time
import json 

import jax.tree_util as jtu


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
    d = json.loads(lines[0])
    
    return jtu.tree_reduce(lambda x, y: x + y, jtu.tree_map(lambda x: int(x) if isinstance(x, int) else 0, d))



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    d = json.loads(lines[0])
    
    def count(tree) -> int:
        c = 0
        if isinstance(tree, dict):
            if not ("red" in tree.keys() or "red" in tree.values()):
                for v in tree.values():
                    c += count(v)
        elif isinstance(tree, (list, tuple)):
            for x in tree:
                c += count(x)
        elif isinstance(tree, int):
            c = tree 

        return c

    return count(d)
    


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
