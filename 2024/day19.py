import os
import time


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


def is_possible(word: str, vocab_set: set[str]) -> bool:
    n = len(word)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and word[j:i] in vocab_set:
                dp[i] = True
                break

    return dp[n]


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)
    vocab_str, words_str = lines.split("\n\n")

    vocab = vocab_str.split(", ")
    words = words_str.strip().split("\n")

    vocab_set = set(vocab)

    return sum(is_possible(word, vocab_set) for word in words)


def count_construct(word: str, vocab_set: set[str]) -> int:
    n = len(word)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if word[j:i] in vocab_set:
                dp[i] += dp[j]

    return dp[n]


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)
    vocab_str, words_str = lines.split("\n\n")

    vocab = vocab_str.split(", ")
    words = words_str.strip().split("\n")

    vocab_set = set(vocab)

    return sum(count_construct(word, vocab_set) for word in words)


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
