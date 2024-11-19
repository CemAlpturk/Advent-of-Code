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


def find_error(line: str) -> str | None:
    stack = []
    map = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    for s in line:
        if s in ("(", "[", "{", "<"):
            stack.append(s)

        else:
            if map[stack[-1]] == s:
                stack.pop(-1)
            else:
                return s


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    score_map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in lines:
        error = find_error(line)
        score += score_map[error] if error else 0
    val = score
    print(f"Part1: {val}")


def autocorrect(line: str) -> str | None:
    stack = []
    map = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    for s in line:
        if s in ("(", "[", "{", "<"):
            stack.append(s)

        else:
            if map[stack[-1]] == s:
                stack.pop(-1)
            else:
                return

    correction = [map[s] for s in stack]
    return "".join(correction[::-1])


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    score_map = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []
    for line in lines:
        corrected = autocorrect(line)
        if corrected is None:
            continue
        score = 0
        for c in corrected:
            score *= 5
            score += score_map[c]

        scores.append(score)

    scores.sort()
    val = scores[len(scores) // 2]
    print(f"Part2: {val}")


if __name__ == "__main__":
    part1()
    part2()
