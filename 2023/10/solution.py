import os
import numpy as np


def run_maze(maze: np.ndarray, start: np.ndarray) -> np.ndarray:
    # Find connecting pipes and choose one at random
    curr_x, curr_y = start
    # visited = [(curr_x, curr_y)]
    maze_mask = np.zeros_like(maze, dtype=bool)
    dists = np.ones_like(maze, dtype=int) * -1
    dists[curr_x, curr_y] = 0
    curr = maze[curr_x, curr_y]
    prev = curr
    step = 1
    while True:
        left = maze[curr_x, curr_y - 1] if curr_y > 0 else None
        right = maze[curr_x, curr_y + 1] if curr_y < maze.shape[1] - 1 else None
        up = maze[curr_x - 1, curr_y] if curr_x > 0 else None
        down = maze[curr_x + 1, curr_y] if curr_x < maze.shape[0] - 1 else None
        # print(curr)
        # print(f"Left: {left}, Right: {right}, Up: {up}, Down: {down}\n")
        if prev != "S" and "S" in [left, right, up, down]:
            print("Complete")
            break
        if curr == "S":
            maze_mask[curr_x, curr_y] = True
            prev = curr
            if left in ["-", "F", "L", "S"] and not maze_mask[curr_x, curr_y - 1]:
                curr_y -= 1
                maze_mask[curr_x, curr_y] = True
            elif right in ["-", "7", "J", "S"] and not maze_mask[curr_x, curr_y + 1]:
                curr_y += 1
                maze_mask[curr_x, curr_y] = True
            elif up in ["|", "7", "F", "S"] and not maze_mask[curr_x - 1, curr_y]:
                curr_x -= 1
                maze_mask[curr_x, curr_y] = True
            elif down in ["|", "J", "L", "S"] and not maze_mask[curr_x + 1, curr_y]:
                curr_x += 1
                maze_mask[curr_x, curr_y] = True
            else:
                print("Error")
                break

        elif curr == "|":
            prev = curr
            if up in ["|", "7", "F", "S"] and not maze_mask[curr_x - 1, curr_y]:
                curr_x -= 1
                maze_mask[curr_x, curr_y] = True
            elif down in ["|", "J", "L", "S"] and not maze_mask[curr_x + 1, curr_y]:
                curr_x += 1
                maze_mask[curr_x, curr_y] = True
            else:
                print("Error")
                break

        elif curr == "-":
            prev = curr
            if left in ["-", "F", "L", "S"] and not maze_mask[curr_x, curr_y - 1]:
                curr_y -= 1
                maze_mask[curr_x, curr_y] = True
            elif right in ["-", "7", "J", "S"] and not maze_mask[curr_x, curr_y + 1]:
                curr_y += 1
                maze_mask[curr_x, curr_y] = True
            else:
                print("Error")
                break

        elif curr == "L":
            prev = curr
            if right in ["-", "7", "J", "S"] and not maze_mask[curr_x, curr_y + 1]:
                curr_y += 1
                maze_mask[curr_x, curr_y] = True
            elif up in ["|", "7", "F", "S"] and not maze_mask[curr_x - 1, curr_y]:
                curr_x -= 1
                maze_mask[curr_x, curr_y] = True
            else:
                print("Error")
                break

        elif curr == "J":
            prev = curr
            if left in ["-", "F", "L", "S"] and not maze_mask[curr_x, curr_y - 1]:
                curr_y -= 1
                maze_mask[curr_x, curr_y] = True
            elif up in ["|", "7", "F", "S"] and not maze_mask[curr_x - 1, curr_y]:
                curr_x -= 1
                maze_mask[curr_x, curr_y] = True

        elif curr == "7":
            prev = curr
            if left in ["-", "F", "L", "S"] and not maze_mask[curr_x, curr_y - 1]:
                curr_y -= 1
                maze_mask[curr_x, curr_y] = True
            elif down in ["|", "J", "L", "S"] and not maze_mask[curr_x + 1, curr_y]:
                curr_x += 1
                maze_mask[curr_x, curr_y] = True

        elif curr == "F":
            prev = curr
            if right in ["-", "7", "J", "S"] and not maze_mask[curr_x, curr_y + 1]:
                curr_y += 1
                maze_mask[curr_x, curr_y] = True
            elif down in ["|", "J", "L", "S"] and not maze_mask[curr_x + 1, curr_y]:
                curr_x += 1
                maze_mask[curr_x, curr_y] = True

        curr = maze[curr_x, curr_y]
        dists[curr_x, curr_y] = step
        step += 1

    return maze_mask, dists


def max_distance(pipes: np.ndarray, dists: np.ndarray, start: np.ndarray) -> np.ndarray:
    max_dist = 0
    max_step = None
    for i in range(pipes.shape[0]):
        for j in range(pipes.shape[1]):
            if pipes[i, j]:
                dist = np.abs(i - start[0]) + np.abs(j - start[1])
                if dist > max_dist:
                    max_dist = dist
                    max_step = dists[i, j]
    return max_step


def part1(filename: str) -> None:
    path = os.path.join(
        os.path.dirname(__file__),
        filename,
    )
    with open(path) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    maze = np.array([list(line) for line in lines])
    # print(maze)

    # Starting point
    start = np.argwhere(maze == "S")[0]

    maze_mask, dists = run_maze(maze, start)
    print(maze_mask)
    print(dists)
    # max_dist = max_distance(maze_mask, dists, start)
    max_dist = np.max(dists)
    print((max_dist + 1) / 2)


if __name__ == "__main__":
    part1("test.txt")
