import os
import time
from collections import Counter
from toolbox.data_structures import Graph


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


def parse_graph(lines: list[str]) -> tuple[Graph, dict]:
    graph = Graph() 
    weights = {}
    for line in lines:
        words = line.split(" ")
        name = words[0] 
        weight = int(words[1][1:-1])
        weights[name] = weight
        if len(words) > 2:
            for v in words[3:]:
                v = v.replace(",", "")
                graph.add_edge(v, name, bidirectional=False)

    return graph, weights


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename) 
    graph, _ = parse_graph(lines)
    for u in graph.nodes():
        if u not in graph.adj_list:
            return u


def invert_graph(graph: Graph) -> Graph: 
    new_adj_list = {} 

    for u in graph.nodes():
        for v in graph.adj_list.get(u, []):
            if v not in new_adj_list:
                new_adj_list[v] = []
            new_adj_list[v].append(u)

    graph.adj_list = new_adj_list 
    return graph 



def part2():
    # filename = "part2-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph, weights = parse_graph(lines)

    root = None 
    for u in graph.nodes():
        if u not in graph.adj_list:
            root = u 
            break 

    graph = invert_graph(graph)

    def total_weight(u: str) -> int:
        sub = [total_weight(v) for v in graph.adj_list.get(u, [])]
        if len(set(sub)) > 1:
            (target, _), (failure, _) = Counter(sub).most_common()
            f_idx = sub.index(failure)
            v = graph.adj_list[u][f_idx]
            print(target - failure + weights[v])
        return weights[u] + sum(sub)

    total_weight(root)
        






if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
