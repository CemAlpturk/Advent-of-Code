import os


def main() -> None:
    input_path = os.path.join(
        os.path.dirname(__file__),
        "input.txt",
    )
    with open(input_path, "r") as file:
        inputs = file.read()

    lines = inputs.split("\n")[:-1]

    # Part 1
    conf = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    games = {}
    valid_sum = 0
    # Process the lines
    for line in lines:
        # Game number
        game_num = line.split(":")[0].split(" ")[1]
        game = line.split(":")[1].strip()

        # Round
        rounds = game.split(";")

        games[game_num] = []
        valid = True
        for round in rounds:
            cubes = round.split(",")
            round_dict = {}
            for cube in cubes:
                for color in conf.keys():
                    if color in cube:
                        tmp = cube.replace(color, "").strip()
                        if tmp != "":
                            round_dict[color] = int(tmp)

                            # Check if round is valid
                            if int(tmp) > conf[color]:
                                valid = False
                                break
            games[game_num].append(round_dict)

        if valid:
            valid_sum += int(game_num)

    print("Part 1")
    print(valid_sum)

    # Part 2
    def _compute_power(game: list[dict[str, int]]) -> int:
        power = 1
        # Compute min number of cubes required
        min_cubes = {k: 0 for k in conf.keys()}
        for color in conf.keys():
            for round in game:
                if color in round.keys():
                    min_cubes[color] = max(min_cubes[color], round[color])

            if min_cubes[color] > 0:
                power *= min_cubes[color]

        return power

    power_sum = 0
    for game_num in games.keys():
        game = games[game_num]
        power_sum += _compute_power(game)

    print("Part 2")
    print(power_sum)


if __name__ == "__main__":
    main()
