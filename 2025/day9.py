import os
import time
from itertools import combinations
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


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename) 
    coords = [tuple(map(int, line.split(","))) for line in lines]
    
    max_area = 0
    for p1, p2 in combinations(coords, 2):
        x1, y1 = p1 
        x2, y2 = p2 

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        max_area = max(max_area, area) 

    return max_area


def intersects(p1, p2, p3, p4):
    x1, y1 = p1 
    x2, y2 = p2 
    x3, y3 = p3 
    x4, y4 = p4 

    is_horizontal1 = y1 == y2 
    is_horizontal2 = y3 == y4 

    if is_horizontal1 == is_horizontal2:
        # Parallel 
        return False 

    h = (p1, p2) if is_horizontal1 else (p3, p4)
    v = (p3, p4) if is_horizontal1 else (p1, p2)


    assert v[0][0] == v[1][0]
    assert h[0][1] == h[1][1]

    return min(h[0][0], h[1][0]) < v[0][0] < max(h[0][0], h[1][0]) and min(v[0][1], v[1][1]) < h[0][1] < max(v[0][1], v[1][1])


def lines_cross(d1, d2, poly):
    n = len(poly)

    for i in range(n):
        d3 = poly[i] 
        d4 = poly[(i+1)%n]

        if intersects(d1, d2, d3, d4):
            return True 

    return False


def point_in_polygon(x, y, poly):
    """
    poly: list of (x, y) vertices in order.
    returns True if (x, y) is inside or on the boundary.
    """

    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # Check if point is on a boundary segment
        if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2)):
            # Segment is vertical
            if x1 == x2 and x == x1:
                return True
            # Segment is horizontal
            if y1 == y2 and y == y1:
                return True

        # Ray casting upward: check for intersections
        intersects = ((y1 > y) != (y2 > y)) and \
                     (x < (x2 - x1) * (y - y1) / (y2 - y1 + 0.0) + x1)
        if intersects:
            inside = not inside

    return inside



def rectangle_ok(p1, p2, poly):
    x1, y1 = p1 
    x2, y2 = p2 

    if x1 == x2 or y1 == y2:
        return False 

    # Corners 
    c1 = p1 
    c2 = p2 
    c3 = (p1[0], p2[1])
    c4 = (p2[0], p1[1])

    # Check if corners are all in polygon
    for c in [c1, c2, c3, c4]:
        if not point_in_polygon(c[0], c[1], poly):
            return False 


    edges = [
        (c1, c3),
        (c1, c4),
        (c3, c2),
        (c4, c2),
    ]
    for d1, d2 in edges:
        if lines_cross(d1, d2, poly):
            return False 

    return True


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt" 

    lines = read_input(filename)
    coords = [tuple(map(int, line.split(","))) for line in lines] 
    
    max_area = 0
    tot = len(coords) * (len(coords) - 1) / 2
    for p1, p2 in tqdm(combinations(coords, 2), total=tot):
        x1, y1 = p1 
        x2, y2 = p2 
        if rectangle_ok(p1, p2, coords):
            area = (abs(x1- x2) + 1) * (abs(y1- y2) + 1)
            max_area = max(max_area, area)

    return max_area
        



if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
