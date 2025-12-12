import os
import time
from typing import Callable
from functools import cache


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


def func(x):
    return lambda x=x: x


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    values: dict[str, Callable[[], int]] = {}
    
    @cache
    def get_val(x):
        return values[x]()

    for line in lines:
        words = line.split(" ")


        if words[0] == "NOT":
            u: str = words[1]
            v: str = words[-1]

            if u.isnumeric():
                values[v] = lambda u=u: (~int(u)) & 0xFFFF
            else:
                values[v] = lambda u=u: (~get_val(u)) & 0xFFFF
            continue 


        if words[1] == "->":
            u = words[0]
            v = words[-1]

            if u.isnumeric():
                values[v] = lambda u=u: int(u) & 0xFFFF
            else:
                values[v] = lambda u=u: get_val(u) 
            continue 

        u = words[0]
        command = words[1]
        v = words[2]
        w = words[-1]

        match command:
            case "AND":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_)
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val & v_val) & 0xFFFF 
            case "OR":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_) 
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val | v_val) & 0xFFFF
            case "LSHIFT":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_)
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val << v_val) & 0xFFFF
            case "RSHIFT":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_) 
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val >> v_val) & 0xFFFF
            case _:
                raise ValueError(f"command {command} not found")

        values[w] = fn

    return values["a"]()

def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    
    values: dict[str, Callable[[], int]] = {}
    
    @cache
    def get_val(x):
        return values[x]()

    for line in lines:
        words = line.split(" ")


        if words[0] == "NOT":
            u: str = words[1]
            v: str = words[-1]

            if u.isnumeric():
                values[v] = lambda u=u: (~int(u)) & 0xFFFF
            else:
                values[v] = lambda u=u: (~get_val(u)) & 0xFFFF
            continue 


        if words[1] == "->":
            u = words[0]
            v = words[-1]

            if u.isnumeric():
                values[v] = lambda u=u: int(u) & 0xFFFF
            else:
                values[v] = lambda u=u: get_val(u) 
            continue 

        u = words[0]
        command = words[1]
        v = words[2]
        w = words[-1]

        match command:
            case "AND":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_)
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val & v_val) & 0xFFFF 
            case "OR":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_) 
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val | v_val) & 0xFFFF
            case "LSHIFT":
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_)
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val << v_val) & 0xFFFF
            case "RSHIFT": 
                def fn(u_=u, v_=v):
                    u_val = get_val(u_) if u_ in values else int(u_) 
                    v_val = get_val(v_) if v_ in values else int(v_)
                    return (u_val >> v_val) & 0xFFFF
            case _:
                raise ValueError(f"command {command} not found")

        values[w] = fn

    values["b"] = lambda: 3176

    return values["a"]()
    

if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
