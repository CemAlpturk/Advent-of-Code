import os


def read_input(filename: str) -> list[str]:

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return [line.strip("\n") for line in lines]


def part1() -> None:
    # filename = "part1-test3.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    graph = {}

    for line in lines:
        p1, p2 = line.split("-")
        if p1 in graph:
            graph[p1].append(p2)
        else:
            graph[p1] = [p2]

        if p2 in graph:
            graph[p2].append(p1)
        else:
            graph[p2] = [p1]

    paths = []

    def dfs(node: str, path: list[str]) -> None:
        if not node.isupper() and node in path:
            return
        if node == "end":
            paths.append(path + [node])
            return

        if node in graph:
            for child in graph[node]:
                dfs(child, path + [node])

    dfs("start", [])

    val = len(paths)
    print(f"Part1: {val}")


def part2() -> None:
    # filename = "part2-test3.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    graph = {}

    for line in lines:
        p1, p2 = line.split("-")
        if p1 in graph:
            graph[p1].append(p2)
        else:
            graph[p1] = [p2]

        if p2 in graph:
            graph[p2].append(p1)
        else:
            graph[p2] = [p1]

    paths = []

    def dfs(node: str, path: list[str]) -> None:
        # Check number of visits to lowercase nodes in path
        counts = set()
        visited_twice = False
        for v in path:
            if v.isupper():
                continue

            if v in counts:
                visited_twice = True
                break
            counts.add(v)

        if visited_twice and not node.isupper() and node in path:
            return

        if node == "end":
            paths.append(path + [node])
            return

        if node in graph:
            for child in graph[node]:
                if child == "start":
                    continue
                dfs(child, path + [node])

    dfs("start", [])

    val = len(paths)
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
