from collections import defaultdict
from pathlib import Path
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return [int(digit) for digit in get_lines(path)[0].split(",")]


# dist: cost
# 1: 1
# 2: 3
# 3: 6
# 4: 10
# 5: 15
# 6: 21

# cost = dist/2 * dist+1
def calc_growing_cost(positions):
    max_x = max(positions)
    costs_dict: defaultdict[int, int] = defaultdict(int)
    for x in range(max_x + 1):
        for pos in positions:
            dist = abs(pos - x)
            costs_dict[x] += int(dist / 2 * (dist + 1))
    return costs_dict


def calc_costs(positions):
    max_x = max(positions)
    costs_dict: defaultdict[int, int] = defaultdict(int)
    for x in range(max_x + 1):
        for pos in positions:
            dist = abs(pos - x)
            costs_dict[x] += dist
    return costs_dict


def part1_example():
    positions = get_data(INPUT_EXAMPLE)
    cost_dict = calc_costs(positions)
    answer = min(cost_dict.values())
    assert answer == 37
    return answer


def part1():
    positions = get_data(INPUT)
    cost_dict = calc_costs(positions)
    answer = min(cost_dict.values())
    return answer


def part2_example():
    positions = get_data(INPUT_EXAMPLE)
    cost_dict = calc_growing_cost(positions)
    answer = min(cost_dict.values())
    assert 168 == answer
    return answer


def part2():
    positions = get_data(INPUT)
    cost_dict = calc_growing_cost(positions)
    answer = min(cost_dict.values())
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
