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
    if sprite_x <= x_pos <= sprite_x + 2:
        return True
    return False


def calc_crt_output(cmds):
    cycle = 1
    sprite_x = 1

    signals = []
    for cmd in cmds:
        cycle += 1
        if check_cycle_and_sprite_overlap(cycle, sprite_x):
            signals.append(sprite_x * cycle)
        if cmd == "noop":
            continue
        cycle += 1
        V = cmd.split(" ")[1]
        sprite_x += int(V)
        if check_cycle_and_sprite_overlap(cycle, sprite_x):
            signals.append(sprite_x * cycle)
    if check_cycle_and_sprite_overlap(cycle, sprite_x):
        signals.append(sprite_x * cycle)

    return sum(signals)


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
    return
    data = get_data(INPUT_EXAMPLE_EZI)
    answer = sum_signal_strengths(data)
    assert answer == 1

    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = sum_signal_strengths(data)
    assert answer == 2

    data = get_data(INPUT_EXAMPLE)
    answer = sum_signal_strengths(data)
    assert answer == 3

    return answer


def part2():
    return
    data = get_data(INPUT)
    answer = sum_signal_strengths(data)
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
