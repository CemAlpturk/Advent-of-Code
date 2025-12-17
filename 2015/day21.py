import os
import time
from itertools import combinations, chain, product


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


weapons = {
    "Dagger": (8, 4, 0),
    "Shortsword": (10, 5, 0),
    "Warhammer": (25, 6, 0),
    "Longsword": (40, 7, 0),
    "Greataxe": (74, 8, 0),
}

armors = {
    "Leather": (13, 0, 1),
    "Chainmail": (31, 0, 2),
    "Splintmail": (53, 0, 3),
    "Bandedmail": (75, 0, 4),
    "Platemail": (102, 0, 5),
}

rings = {
    "Damage +1": (25, 1, 0),
    "Damage +2": (50, 2, 0),
    "Damage +3": (100, 3, 0),
    "Defense +1": (20, 0, 1),
    "Defense +2": (40, 0, 2),
    "Defense +3": (80, 0, 3),
}


def play(
    hit_points: int,
    damage: int,
    armor: int,
    boss_hit_points: int,
    boss_damage: int,
    boss_armor: int, 
) -> bool:
    while hit_points > 0 and boss_hit_points > 0:
        # Player starts 
        boss_hit_points -= max(1, damage - boss_armor)

        if boss_hit_points <= 0:
            return True 

        # Boss turn 
        hit_points -= max(1, boss_damage - armor) 

        if hit_points <= 0:
            return False

    return False


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    
    boss_hit_points = int(lines[0].split(": ")[-1])
    boss_damage = int(lines[1].split(": ")[-1])
    boss_armor = int(lines[2].split(": ")[-1])

    hit_points = 100

    # shop 
    w_s = combinations(weapons, 1)
    a_s = chain(combinations(armors, 0), combinations(armors, 1))
    r_s = chain(combinations(rings, 0), combinations(rings, 1), combinations(rings, 2))

    items = product(w_s, a_s, r_s)



    min_cost = float("inf")
    for weapon, arm, ring in items:
        cost = 0
        damage = weapons[weapon[0]][1]
        cost += weapons[weapon[0]][0]
        armor = armors[arm[0]][2] if arm else 0
        cost += armors[arm[0]][0] if arm else 0
        for r in ring:
            damage += rings[r][1]
            armor += rings[r][2]
            cost += rings[r][0]

        if play(hit_points, damage, armor, boss_hit_points, boss_damage, boss_armor):
            min_cost = min(min_cost, cost)

    return min_cost

         



def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    boss_hit_points = int(lines[0].split(": ")[-1])
    boss_damage = int(lines[1].split(": ")[-1])
    boss_armor = int(lines[2].split(": ")[-1])

    hit_points = 100

    # shop 
    w_s = combinations(weapons, 1)
    a_s = chain(combinations(armors, 0), combinations(armors, 1))
    r_s = chain(combinations(rings, 0), combinations(rings, 1), combinations(rings, 2))

    items = product(w_s, a_s, r_s)



    max_cost = -float("inf")
    for weapon, arm, ring in items:
        cost = 0
        damage = weapons[weapon[0]][1]
        cost += weapons[weapon[0]][0]
        armor = armors[arm[0]][2] if arm else 0
        cost += armors[arm[0]][0] if arm else 0
        for r in ring:
            damage += rings[r][1]
            armor += rings[r][2]
            cost += rings[r][0]

        if not play(hit_points, damage, armor, boss_hit_points, boss_damage, boss_armor):
            max_cost = max(max_cost, cost)

    return max_cost




if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
