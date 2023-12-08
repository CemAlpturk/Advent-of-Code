def process_card(card: str) -> tuple[list[int], list[int]]:
    values = card.split(":")[1]
    winning_nums = [int(num) for num in values.split("|")[0].split(" ") if num != ""]
    nums = [int(num) for num in values.split("|")[1].split(" ") if num != ""]

    return winning_nums, nums


def part1(filename: str) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            line = line.strip("\n")

            winning_nums, nums = process_card(line)
            count = 0
            for num in winning_nums:
                if num in nums:
                    count += 1
            if count > 0:
                sum += 2 ** (count - 1)
    print(sum)


def part2(filename: str) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()

    n_cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        line = line.strip("\n")
        winning_nums, nums = process_card(line)

        count = 0
        for num in winning_nums:
            if num in nums:
                count += 1
                n_cards[i + count] += n_cards[i]

    print(sum(n_cards))


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
