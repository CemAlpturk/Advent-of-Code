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


def parse_package(packet: str):
    print(packet)
    if len(packet) < 7:
        return 0
    packet_version = int(packet[:3], 2)
    packet_type_id = int(packet[3:6], 2)
    print(f"packet_version: {packet_version}")
    print(f"packet type: {packet_type_id}")
    if packet_type_id == 4:
        # Literal type
        print("Literal")
        literal = packet[6:]
        value = ""
        end_idx = None
        for i in range(0, len(literal), 5):
            flag = literal[i]
            value += literal[i + 1 : i + 5]
            if flag == "0":
                end_idx = i + 5
                break

        print(int(value, 2))
        remaining = literal[end_idx:] if end_idx else ""
        return packet_version + parse_package(remaining)

    else:
        # Operator type
        # parse_operator(packet[6:])
        print("Operator")
        operator = packet[6:]
        length_type_id = operator[0]

        if length_type_id == "0":
            length = int(operator[1:16], 2)
            print(f"length: {length}")
            remaining = operator[16 : 16 + length]

        else:
            num = int(operator[1:12], 2)
            print(f"num {num}")
            remaining = operator[12:]

        return packet_version + parse_package(remaining)


def parse_literal(literal: str):
    value = ""
    end_idx = None
    for i in range(0, len(literal), 5):
        flag = literal[i]
        value += literal[i + 1 : i + 5]
        if flag == "0":
            end_idx = i + 5
            break

    print(int(value, 2))
    remaining = literal[end_idx:] if end_idx else ""

    parse_package(remaining)


def parse_operator(operator: str):
    length_type_id = operator[0]

    if length_type_id == "0":
        length = int(operator[1:16], 2)
        # print(length)
        remaining = operator[16 : 16 + length]

    parse_package(remaining)


hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def part1():
    filename = "part1-test5.txt"
    # filename = "part1.txt"

    lines = read_input(filename)

    hex = lines[0]
    packet = "".join(hex_to_bin[i] for i in hex)

    return parse_package(packet)


def part2():
    filename = "part2-test.txt"
    # filename = "part2.txt"

    lines = read_input(filename)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
