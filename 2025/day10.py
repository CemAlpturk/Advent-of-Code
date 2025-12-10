import os
import time
import scipy
from tqdm import tqdm


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


def button_vals(button: tuple[int, ...], w: int) -> int:
    value = 0
    for pos in button:
        # Convert MSB-indexed pos to normal LSB bit index
        bit_index = w - 1 - pos
        value |= 1 << bit_index
    return value
    


def process_input(lines: list[str]):

    targets = []
    buttons = []
    
    for line in lines:
        # Target lights
        start = line.find("[") + 1
        stop = line.find("]")
        
        target_lights_str = line[start:stop]
        target_lights_str = "".join(str(int(s == "#")) for s in target_lights_str)
        w = len(target_lights_str)
        target_lights = int(target_lights_str, 2)

        # Buttons 
        start = stop + 1 
        stop = line.find("{")

        button = [tuple(map(int, x[1:-1].split(","))) for x in line[start:stop].split(" ") if x]
        button = list(map(lambda x: button_vals(x, w), button))

        targets.append(target_lights)
        buttons.append(button)

    return targets, buttons 


def process_input2(lines: list[str]):

    buttons = []
    joltages = [] 

    for line in lines:

        start = line.find("]") + 1 
        stop = line.find("{")
        button = [list(map(int, x[1:-1].split(","))) for x in line[start:stop].split(" ") if x]
        
        # Joltage
        start = stop + 1 
        joltage = list(map(int, line[start:-1].split(",")))
        
        buttons.append(button)
        joltages.append(joltage)

    return buttons, joltages

def bfs(target: int, buttons: list[int]) -> int:
    start = 0
    visited = set()
    queue = [(start, 0)]

    while queue:
        v, d = queue.pop(0)

        if v == target:
            return d 
        if v not in visited:
            visited.add(v)

            # Neighbors 
            for b in buttons:
                u = v ^ b 
                if u not in visited:
                    queue.append((u, d+1))

    return -1 


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    targets, buttons = process_input(lines)
    tot = 0
    for t, b in zip(targets, buttons):
        d = bfs(t, b) 
        tot += d 

    return tot





def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    buttons, joltages = process_input2(lines)
    
    tot = 0 
    for i, jolts in tqdm(enumerate(joltages)):
        buts = buttons[i] 

        A = [[0 for i_ in range(len(buts))] for j in range(len(jolts))]
        for j, but in enumerate(buts):
            for light in but:
                A[light][j] = 1

        c = [1 for i_ in range(len(buts))]
        res = scipy.optimize.linprog(c, A_eq=A, b_eq=jolts, integrality=1)
        
        if not res.success:
            print("Couldn't find optimal solution")
            return -1

        tot += sum(res.x)

    return int(tot)



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
