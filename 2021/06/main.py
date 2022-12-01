from collections import defaultdict
from pathlib import Path
from collections import Counter
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return [int(digit) for digit in get_lines(path)[0].split(",")]


def simulate_days_brute(fishys: list[int], nbr_days):
    output = fishys.copy()
    for day in range(nbr_days):
        pass_day(output)
    return output


def pass_day(fishys: list[int]):
    new_fishys = []
    for idx, fish in enumerate(fishys):
        if fish == 0:
            fishys[idx] = fish = 6
            new_fishys.append(8)
        else:
            fishys[idx] -= 1
    for new_fish in new_fishys:
        fishys.append(new_fish)


def simulate_days_using_bins(fishys: list[int], nbr_days):
    total_fishys: Counter = Counter(fishys)
    for day in range(nbr_days):
        for age in reversed(range(1, 11)):
            total_fishys[9 - age] = total_fishys[9 - age + 1]
        total_fishys[6] += total_fishys[-1]
        total_fishys[8] += total_fishys[-1]
        del total_fishys[-1]

    return sum(total_fishys.values())


def part1_example():
    fishys = get_data(INPUT_EXAMPLE)
    day_18 = simulate_days_brute(fishys, 18)
    assert 26 == len(day_18)
    day_80 = simulate_days_brute(fishys, 80)
    assert 5934 == len(day_80)
    return len(day_80)


def part1():
    fishys = get_data(INPUT)
    day_80 = simulate_days_brute(fishys, 80)
    return len(day_80)


def part2_example():
    fishys = get_data(INPUT_EXAMPLE)
    result = simulate_days_using_bins(fishys, 256)
    assert 26_984_457_539 == result
    return result


def part2():
    fishys = get_data(INPUT)
    result = simulate_days_using_bins(fishys, 256)
    return result


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
