from pathlib import Path
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[str]:
    return get_lines(path)


def check_cycle(cycle):
    if (cycle % 40) == 20:
        return True
    return False


def sum_signal_strengths(cmds):
    cycle = 1
    X = 1
    signals = []
    for cmd in cmds:
        cycle += 1
        if check_cycle(cycle):
            signals.append(X * cycle)
        if cmd == "noop":
            continue
        cycle += 1
        V = cmd.split(" ")[1]
        X += int(V)
        if check_cycle(cycle):
            signals.append(X * cycle)
    if check_cycle(cycle):
        signals.append(X * cycle)

    return sum(signals)


def check_cycle_and_sprite_overlap(cycle, sprite_x):
    x_pos = cycle % 40
    if x_pos == 0:
        # include cycle 40, 80, 120, ...
        # there must be a smarter expression... but im tired :)
        x_pos = 40
    if cycle == 200:
        pass
    if sprite_x <= x_pos <= (sprite_x + 2):
        return "#"
    return "."


def calc_crt_output(cmds):
    cycle = 1
    sprite_x = 1

    signals = []
    signals.append(check_cycle_and_sprite_overlap(cycle, sprite_x))
    for cmd in cmds:
        cycle += 1
        signals.append(check_cycle_and_sprite_overlap(cycle, sprite_x))
        if cmd == "noop":
            continue
        cycle += 1
        V = cmd.split(" ")[1]
        sprite_x += int(V)
        signals.append(check_cycle_and_sprite_overlap(cycle, sprite_x))
    signals.append(check_cycle_and_sprite_overlap(cycle, sprite_x))
    return signals


def part1_example():

    data = get_data(INPUT_EXAMPLE)
    answer = sum_signal_strengths(data)
    assert answer == 13140

    return answer


def part1():
    data = get_data(INPUT)
    answer = sum_signal_strengths(data)

    return answer


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    answer = calc_crt_output(data)
    for i in range(len(answer)):
        if i % 40 == 0:
            print("")
        print(answer[i], end="")
    return answer


def part2():
    data = get_data(INPUT)
    answer = calc_crt_output(data)
    for i in range(len(answer)):
        if i % 40 == 0:
            print("")
        print(answer[i], end="")
    return answer


def main():
    ex1 = part1_example()
    ex2 = part2_example()
    p1 = part1()
    p2 = part2()
    print(f"example part 1: {ex1}")
    print(f"part 1: {p1}")
    print(f"example part 2: {ex2}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
