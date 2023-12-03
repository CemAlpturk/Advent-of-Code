import os


def main() -> None:
    # Get input from file
    file_path = os.path.join(
        os.path.dirname(__file__),
        "input.txt",
    )

    with open(file_path, "r") as file:
        inputs = file.read()

    # Part 1
    inputs = inputs.split("\n")
    sum = 0
    for line in inputs:
        nums = [c for c in line if c.isdigit()]

        if len(nums) == 0:
            continue

        first, last = nums[0], nums[-1]

        # Merge the numbers
        num = int(first + last)
        sum += num

    print("Part 1:")
    print(sum)

    # Part 2
    sum = 0
    d = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    replacements = {
        "1": "one1one",
        "2": "two2two",
        "3": "three3three",
        "4": "four4four",
        "5": "five5five",
        "6": "six6six",
        "7": "seven7seven",
        "8": "eight8eight",
        "9": "nine9nine",
    }

    for line in inputs:
        # Replace the words with the numbers
        for word, num in d.items():
            line = line.replace(word, replacements[str(num)])
        # Same as before
        nums = [c for c in line if c.isdigit()]
        # print(nums)
        if len(nums) == 0:
            continue
        first, last = nums[0], nums[-1]
        if first == "0":
            print(nums)
        num = int(first + last)
        sum += num

    print("Part 2:")
    print(sum)


if __name__ == "__main__":
    main()
