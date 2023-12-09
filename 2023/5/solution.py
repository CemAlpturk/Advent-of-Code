def read_part(part: str) -> list[tuple[int, int, int]]:
    return [
        tuple(int(x) for x in line.split(" "))
        for line in part.split("\n")[1:]
        if line != ""
    ]


def invert_part(part: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    return [(source, dest, step) for dest, source, step in part]


def get_map(inp_maps: list[tuple[int, int, int]]) -> callable:
    def _map(seed: int) -> int:
        for dest, source, step in inp_maps:
            if source <= seed < source + step:
                return dest + seed - source
        return seed

    return _map


def check_seed(seed: int, ranges: list[tuple[int, int]]) -> bool:
    for start, step in ranges:
        if start <= seed < start + step:
            return True
    return False


def part1(filename: str) -> None:
    with open(filename) as f:
        lines = f.read()

    parts = lines.split("\n\n")

    initial_seeds = [int(seed) for seed in parts[0].split(":")[1].strip().split(" ")]

    seed_to_soil = read_part(parts[1])
    seed_to_soil_map = get_map(seed_to_soil)

    soil_to_fertilizer = read_part(parts[2])
    soil_to_fertilizer_map = get_map(soil_to_fertilizer)

    fertilizer_to_water = read_part(parts[3])
    fertilizer_to_water_map = get_map(fertilizer_to_water)

    water_to_light = read_part(parts[4])
    water_to_light_map = get_map(water_to_light)

    light_to_temperature = read_part(parts[5])
    light_to_temperature_map = get_map(light_to_temperature)

    temperature_to_humidity = read_part(parts[6])
    temperature_to_humidity_map = get_map(temperature_to_humidity)

    humidity_to_location = read_part(parts[7])
    humidity_to_location_map = get_map(humidity_to_location)

    # Find location for each seed
    seed_to_location = {}
    for seed in initial_seeds:
        soil = seed_to_soil_map(seed)
        fertilizer = soil_to_fertilizer_map(soil)
        water = fertilizer_to_water_map(fertilizer)
        light = water_to_light_map(water)
        temperature = light_to_temperature_map(light)
        humidity = temperature_to_humidity_map(temperature)
        location = humidity_to_location_map(humidity)
        seed_to_location[seed] = location

    min_location = min(seed_to_location.values())
    print(min_location)


def part2(filename: str) -> None:
    with open(filename) as f:
        lines = f.read()

    parts = lines.split("\n\n")

    seeds = [int(seed) for seed in parts[0].split(":")[1].strip().split(" ")]
    initial_seeds = []
    for i in range(0, len(seeds), 2):
        initial_seeds.append((seeds[i], seeds[i + 1]))

    # Inverse maps
    humidity_to_location = read_part(parts[7])
    location_to_humidity = invert_part(humidity_to_location)
    location_to_humidity_map = get_map(location_to_humidity)

    temperature_to_humidity = read_part(parts[6])
    humidity_to_temperature = invert_part(temperature_to_humidity)
    humidity_to_temperature_map = get_map(humidity_to_temperature)

    light_to_temperature = read_part(parts[5])
    temperature_to_light = invert_part(light_to_temperature)
    temperature_to_light_map = get_map(temperature_to_light)

    water_to_light = read_part(parts[4])
    light_to_water = invert_part(water_to_light)
    light_to_water_map = get_map(light_to_water)

    fertilizer_to_water = read_part(parts[3])
    water_to_fertilizer = invert_part(fertilizer_to_water)
    water_to_fertilizer_map = get_map(water_to_fertilizer)

    soil_to_fertilizer = read_part(parts[2])
    fertilizer_to_soil = invert_part(soil_to_fertilizer)
    fertilizer_to_soil_map = get_map(fertilizer_to_soil)

    seed_to_soil = read_part(parts[1])
    soil_to_seed = invert_part(seed_to_soil)
    soil_to_seed_map = get_map(soil_to_seed)

    def location_to_seed_map(location: int) -> int:
        humidity = location_to_humidity_map(location)
        temperature = humidity_to_temperature_map(humidity)
        light = temperature_to_light_map(temperature)
        water = light_to_water_map(light)
        fertilizer = water_to_fertilizer_map(water)
        soil = fertilizer_to_soil_map(fertilizer)
        return soil_to_seed_map(soil)

    # Brute force location from 0 untill we find a seed
    # in the given ranges

    location = 0
    seed = location_to_seed_map(location)
    while not check_seed(seed, initial_seeds):
        location += 1
        seed = location_to_seed_map(location)

    print(location)


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
