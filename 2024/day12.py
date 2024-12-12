import os
import time
import numpy as np


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


def grid_to_graph(grid: np.ndarray) -> dict[tuple[int, int], list[tuple[int, int]]]:
    graph = {}
    n, m = grid.shape

    for i in range(n):
        for j in range(m):
            pos = (i, j)
            graph[pos] = []

            if i > 0:
                graph[pos].append((i - 1, j))

            if i < n - 1:
                graph[pos].append((i + 1, j))

            if j > 0:
                graph[pos].append((i, j - 1))

            if j < m - 1:
                graph[pos].append((i, j + 1))

    return graph


def get_regions(
    grid: np.ndarray,
    graph: dict[tuple[int, int], list[tuple[int, int]]],
) -> list[list[tuple[int, int]]]:
    regions = []
    s = set(graph.keys())

    while s:
        region = []
        start = s.pop()
        visited = set()
        q = [start]

        while q:
            u = q.pop(0)
            if u in visited:
                continue

            visited.add(u)
            region.append(u)
            if u in s:
                s.remove(u)

            for v in graph[u]:
                if grid[*u] == grid[*v]:
                    q.append(v)

        regions.append(region)

    return regions


def get_cost(
    grid: np.ndarray,
    graph: dict[tuple[int, int], list[tuple[int, int]]],
    region: list[tuple[int, int]],
) -> int:
    n, m = grid.shape

    area = len(region)

    perim = 0

    q = [region[0]]
    visited = set()

    while q:
        u = q.pop(0)
        if u in visited:
            continue

        visited.add(u)

        c = 4 - len(graph[u])

        for v in graph[u]:
            if grid[*v] == grid[*u]:
                q.append(v)
            else:
                c += 1

        perim += c

    return area * perim


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])

    graph = grid_to_graph(grid)
    regions = get_regions(grid, graph)
    cost = 0
    for region in regions:
        cost += get_cost(grid, graph, region)

    return cost


def count_corners(
    grid: np.ndarray,
    region: list[tuple[int, int]],
) -> int:
    n, m = grid.shape
    corners = 0
    for u in region:
        up = (u[0] - 1, u[1])
        down = (u[0] + 1, u[1])
        left = (u[0], u[1] - 1)
        right = (u[0], u[1] + 1)
        sw = (u[0] + 1, u[1] - 1)
        se = (u[0] + 1, u[1] + 1)
        nw = (u[0] - 1, u[1] - 1)
        ne = (u[0] - 1, u[1] + 1)

        # Count the number of neighbors
        c = 0
        for x, y in (up, down, left, right):
            if 0 <= x < n and 0 <= y < m:
                if grid[*u] == grid[x, y]:
                    c += 1

        if c == 0:
            corners += 4
            continue

        if c == 1:
            corners += 2
            continue

        if c > 2:
            continue

        if c == 2:
            # Check if opposing neighbors
            # Up-down
            check = True
            for x, y in (up, down):
                check = check and (0 <= x < n and 0 <= y < n and grid[*u] == grid[x, y])

            if check:
                continue

            # Left-right
            check = True
            for x, y in (left, right):
                check = check and (0 <= x < n and 0 <= y < n and grid[*u] == grid[x, y])

            if check:
                continue

            # Check inner corner

            corners += 2

    return corners


def add(p: tuple[int, int], s: tuple[int, int]) -> tuple[int, int]:
    return (p[0] + s[0], p[1] + s[1])


def in_bounds(p: tuple[int, int], grid: np.ndarray):
    n, m = grid.shape
    return 0 <= p[0] < n and 0 <= p[1] < m


def isEdge(
    grid: np.ndarray,
    p: tuple[int, int],
    d: tuple[int, int],
    region: list[tuple[int, int]],
):
    p1 = add(p, d)
    return not in_bounds(p1, grid) or p1 not in region


SIDEDIRS = {
    (-1, 0): [(0, 1), (0, -1)],
    (1, 0): [(0, 1), (0, -1)],
    (0, -1): [(-1, 0), (1, 0)],
    (0, 1): [(-1, 0), (1, 0)],
}


def calculate_edges(grid: np.ndarray, region: list[tuple[int, int]]) -> int:
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    sides = 0
    for p in region:
        for d in dirs:
            if isEdge(grid, p, d, region) and (p, d) not in visited:
                visited.add((p, d))
                for s in SIDEDIRS[d]:
                    p2 = add(p, s)
                    while p2 in region and isEdge(grid, p2, d, region):
                        visited.add((p2, d))
                        p2 = add(p2, s)

                sides += 1

    return sides


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    grid = np.array([[v for v in line.strip()] for line in lines.split("\n") if line])
    graph = grid_to_graph(grid)
    regions = get_regions(grid, graph)

    cost = 0
    for region in regions:
        area = len(region)
        corners = calculate_edges(grid, region)
        price = area * corners
        # print(grid[*region[0]], area, corners, price)
        cost += price

    return cost


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
