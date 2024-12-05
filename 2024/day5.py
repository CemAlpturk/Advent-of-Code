import os
import time
from collections import defaultdict
from functools import cmp_to_key


def read_input(filename: str) -> str:
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
        data = f.read()

    return data


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    rules_str, updates_str = lines.split("\n\n")

    rules = [tuple(map(int, rule.strip().split("|"))) for rule in rules_str.split("\n")]
    updates = [
        list(map(int, update.strip().split(",")))
        for update in updates_str.split("\n")
        if update
    ]
    rule_graph = defaultdict(list)
    for x, y in rules:
        rule_graph[y].append(x)

    total = 0
    for update in updates:
        accept = True
        seen = set()
        update_total = set(update)
        for u in update:
            # print(u)
            reqs = rule_graph[u]
            # print(reqs)
            for r in reqs:
                if r in update_total and r not in seen:
                    accept = False
                    break
            if not accept:
                break
            seen.add(u)
        if accept:
            n = len(update)
            total += update[n // 2]

    return total


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    rules_str, updates_str = lines.split("\n\n")

    rules = [tuple(map(int, rule.strip().split("|"))) for rule in rules_str.split("\n")]
    updates = [
        list(map(int, update.strip().split(",")))
        for update in updates_str.split("\n")
        if update
    ]

    rule_graph = defaultdict(list)
    for x, y in rules:
        rule_graph[y].append(x)

    cmp = cmp_to_key(lambda x, y: -(x in rule_graph[y]))

    total = 0
    for update in updates:
        accept = True
        seen = set()
        update_total = set(update)
        for u in update:
            # print(u)
            reqs = rule_graph[u]
            # print(reqs)
            for r in reqs:
                if r in update_total and r not in seen:
                    accept = False
                    break
            if not accept:
                break
            seen.add(u)
        if not accept:
            # Solution goes here
            # Reorder the updates
            s = sorted(update, key=cmp)
            total += s[len(s) // 2]

    return total


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
