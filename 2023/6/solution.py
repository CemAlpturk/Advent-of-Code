def optimal_times(time: int, best_distance: int) -> int:
    count = 0
    for t_press in range(1, time):
        speed = t_press
        dist = speed * (time - t_press)
        if dist > best_distance:
            count += 1

    return count


def part1(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    times = [int(t.strip()) for t in lines[0].split(":")[1].split(" ") if t != ""]
    distances = [int(d.strip()) for d in lines[1].split(":")[1].split(" ") if d != ""]

    mult = 1
    for t, d in zip(times, distances):
        mult *= optimal_times(t, d)

    print(mult)


def part2(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    times = [int(t.strip()) for t in lines[0].split(":")[1].split(" ") if t != ""]
    distances = [int(d.strip()) for d in lines[1].split(":")[1].split(" ") if d != ""]

    # Merge the values
    time = int("".join([str(t) for t in times]))
    distance = int("".join([str(d) for d in distances]))

    print(optimal_times(time, distance))


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
