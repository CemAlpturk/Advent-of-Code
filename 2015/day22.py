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


HARD = True

# (mana)
spells = {
    "magic_missle": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}

def has_finished(state) -> bool:

    return state["boss_hit_points"] <= 0 or state["hit_points"] <= 0 

def can_cast(state) -> bool:
    return state["mana"] >= 53


def apply_effects(state):

    if state["shield_turns"] > 0:
        state["armor"] = 7 
        state["shield_turns"] -= 1
    else:
        state["armor"] = 0

    if state["poison_turns"] > 0:
        state["boss_hit_points"] -= 3 
        state["poison_turns"] -= 1 

    if state["recharge_turns"] > 0:
        state["mana"] += 101 
        state["recharge_turns"] -= 1

    return state


def play_turn(state, spell, hard=False):

    # Player turn 
    
    if has_finished(state):
        return state


    if hard:
        state["hit_points"] -= 1 


    if has_finished(state):
        return state 

    state = apply_effects(state)


    if has_finished(state):
        return state


    if state["mana"] < spells[spell]:
        return None
    state["mana"] -= spells[spell]
    state["total_mana_spent"] += spells[spell]

    match spell:
        case "magic_missle":
            state["boss_hit_points"] -= 4

        case "drain":
            state["boss_hit_points"] -= 2
            state["hit_points"] += 2

        case "shield":
            state["shield_turns"] = 6

        case "poison":
            state["poison_turns"] = 6 

        case "recharge":
            state["recharge_turns"] = 5 

    if has_finished(state):
        return state 

    # Boss turn 
    state = apply_effects(state)

    state["hit_points"] -= max(1, state["boss_damage"] - state["armor"])


    return state




def get_spells(state) -> list[str]:
    spls = []
    for spell in spells.keys():
        if state["mana"] >= spells[spell]:
            spls.append(spell)

    return spls 




def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    # Boss stats 
    boss_hit_points = int(lines[0].split(": ")[-1])
    boss_damage = int(lines[1].split(": ")[-1])

    hit_points = 50 
    mana = 500 
    armor = 0
    total_mana_spent = 0

    # State 
    state = {
        "boss_hit_points": boss_hit_points,
        "boss_damage": boss_damage,
        "hit_points": hit_points,
        "mana": mana,
        "total_mana_spent": total_mana_spent,
        "armor": armor,
        "shield_turns": 0,  # shield turns
        "poison_turns": 0,  # poison turns 
        "recharge_turns": 0,  # recharge turns
    }

    # bfs 
    queue = [state]
    min_mana = float("inf")
    while queue:
        u = queue.pop(0)

        if has_finished(u):
            if u["boss_hit_points"] <= 0:
                min_mana = min(min_mana, u["total_mana_spent"])
            continue

        if u["total_mana_spent"] > min_mana:
            continue

        for spell in spells.keys():
            v = play_turn(u.copy(), spell)
            if v is not None:
                queue.append(v)
    return min_mana




def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    
    # Boss stats 
    boss_hit_points = int(lines[0].split(": ")[-1])
    boss_damage = int(lines[1].split(": ")[-1])

    hit_points = 50 
    mana = 500 
    armor = 0
    total_mana_spent = 0

    # State 
    state = {
        "boss_hit_points": boss_hit_points,
        "boss_damage": boss_damage,
        "hit_points": hit_points,
        "mana": mana,
        "total_mana_spent": total_mana_spent,
        "armor": armor,
        "shield_turns": 0,  # shiield turns
        "poison_turns": 0,  # poison turns 
        "recharge_turns": 0,  # recharge turns
    }

    # bfs
    queue = [state]
    min_mana = float("inf")
    while queue:
        u = queue.pop(0)

        if has_finished(u):
            if u["boss_hit_points"] <= 0 and u["hit_points"] > 0:
                min_mana = min(min_mana, u["total_mana_spent"])
            continue

        if u["total_mana_spent"] > min_mana:
            continue

        for spell in spells.keys():
            v = play_turn(u.copy(), spell, True)
            if v is not None:
                queue.append(v)

    return min_mana

    



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
