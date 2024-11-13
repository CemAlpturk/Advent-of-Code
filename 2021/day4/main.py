import os

import numpy as np


def read_input(filename: str) -> list[str]:

    filepath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            filename,
        )
    )

    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines


def is_win(selected: np.ndarray) -> bool:
    n, m = selected.shape
    for i in range(n):
        if np.all(selected[i]):
            return True

    for j in range(m):
        if np.all(selected[:, j]):
            return True

    return False


def part1() -> None:
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    draws = [int(val) for val in lines[0].strip("\n").split(",")]

    cards = []
    card = []
    for line in lines[2:]:
        if len(line) > 1:
            vals = [int(val) for val in line.strip("\n").split(" ") if val != ""]
            card.append(vals)
        else:
            cards.append(np.array(card))
            card = []
    cards.append(np.array(card))

    cards_selected = [np.zeros_like(card, dtype=np.bool_) for card in cards]

    score = None
    # Play bingo
    for draw in draws:
        if score:
            break
        for card, selected in zip(cards, cards_selected):
            idxs = card == draw
            selected[idxs] = True

            if is_win(selected):
                sum = card[~selected].sum()
                score = sum * draw
                break

    assert score is not None

    print(f"Part1: {score}")


def part2() -> None:
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    draws = [int(val) for val in lines[0].strip("\n").split(",")]

    cards = []
    card = []
    for line in lines[2:]:
        if len(line) > 1:
            vals = [int(val) for val in line.strip("\n").split(" ") if val != ""]
            card.append(vals)
        else:
            cards.append(np.array(card))
            card = []
    cards.append(np.array(card))

    cards_selected = [np.zeros_like(card, dtype=np.bool_) for card in cards]
    card_won = [False for _ in cards]
    score = None
    # Play bingo
    for draw in draws:
        if score:
            break
        for i, (card, selected) in enumerate(zip(cards, cards_selected)):
            if card_won[i]:
                continue
            idxs = card == draw
            selected[idxs] = True

            if is_win(selected):
                card_won[i] = True
                if all(card_won):
                    sum = card[~selected].sum()
                    score = sum * draw
                    break

    assert score is not None

    print(f"Part2: {score}")


if __name__ == "__main__":
    part1()
    part2()
