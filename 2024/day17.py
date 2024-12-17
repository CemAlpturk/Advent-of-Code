import os
import time

REG_A = 0
REG_B = 0
REG_C = 0
IP = 0


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


def parse_registers_and_program(lines: str) -> tuple[int, int, int, list[int]]:
    reg_str, program_str = lines.split("\n\n")

    regA_str, regB_str, regC_str = reg_str.split("\n")
    regA = int(regA_str.split(": ")[1].strip())
    regB = int(regB_str.split(": ")[1].strip())
    regC = int(regC_str.split(": ")[1].strip())

    program = [int(x) for x in program_str.split(": ")[1].strip().split(",")]

    return regA, regB, regC, program


def adv(oprand: int) -> None:
    global REG_A
    REG_A = int(REG_A / 2**oprand)


def bxl(oprand: int) -> None:
    global REG_B
    REG_B = REG_B ^ oprand


def bst(oprand: int) -> None:
    global REG_B
    REG_B = oprand % 8


def jnz(oprand: int) -> bool:
    global IP
    if REG_A == 0:
        return False
    IP = oprand
    return True


def bxc(_: int) -> None:
    global REG_B
    REG_B = REG_B ^ REG_C


def out(oprand: int) -> int:
    return oprand % 8


def bdv(oprand: int) -> None:
    global REG_B
    REG_B = int(REG_A / 2**oprand)


def cdv(oprand: int) -> None:
    global REG_C
    REG_C = int(REG_A / 2**oprand)


def combo(x: int) -> int:
    if x < 4:
        return x
    elif x == 4:
        return REG_A
    elif x == 5:
        return REG_B
    elif x == 6:
        return REG_C
    else:
        raise ValueError("Kek")


def run(
    a: int, b: int, c: int, program: list[int], nmax: int | None = None
) -> list[int]:
    global IP, REG_A, REG_B, REG_C

    IP = 0
    REG_A = a
    REG_B = b
    REG_C = c

    output: list[int] = []
    step = 0

    while IP < len(program):
        op = program[IP]
        x = program[IP + 1]
        # print(IP, op, x)
        match op:
            case 0:
                x = combo(x)
                adv(x)
                IP += 2

            case 1:
                bxl(x)
                IP += 2

            case 2:
                x = combo(x)
                bst(x)
                IP += 2

            case 3:
                flag = jnz(x)
                if not flag:
                    IP += 2

            case 4:
                bxc(x)
                IP += 2

            case 5:
                x = combo(x)
                o = out(x)
                output.append(o)
                # print(o)
                IP += 2

            case 6:
                x = combo(x)
                bdv(x)
                IP += 2

            case 7:
                x = combo(x)
                cdv(x)
                IP += 2

        step += 1
        if nmax and step > nmax:
            return output

    return output


def part1():
    # filename = "part1-test.txt"
    filename = "part1.txt"

    lines = read_input(filename)

    a, b, c, program = parse_registers_and_program(lines)

    output = run(a, b, c, program)
    return ",".join(map(str, output))


def part2():
    # filename = "part2-test.txt"
    filename = "part2.txt"

    lines = read_input(filename)

    a, b, c, program = parse_registers_and_program(lines)

    n = len(program)
    a = 0
    while True:
        output = run(a, b, c, program, n + 1)
        if output == program:
            return a
        a += 1


if __name__ == "__main__":
    start = time.perf_counter()
    result1 = part1()
    elapsed1 = time.perf_counter() - start
    print(f"Part1: {result1} (Time: {elapsed1:.6f}s)")

    start = time.perf_counter()
    result2 = part2()
    elapsed2 = time.perf_counter() - start
    print(f"Part2: {result2} (Time: {elapsed2:.6f}s)")
