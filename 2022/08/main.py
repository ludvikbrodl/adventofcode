from pathlib import Path
from itertools import product
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path):
    input_lines = get_lines(path)

    data = np.full((len(input_lines[0]), len(input_lines)), -1, dtype=int)
    for y_idx, row in enumerate(input_lines):
        data[:][y_idx] = list(row)

    return data


def check_all_indices(matrix):
    nbr_tress = 0
    for x, y in product(range(len(matrix)), range(len(matrix[0]))):
        if check_visiblity(matrix, x, y):
            nbr_tress += 1
    return nbr_tress


def check_visiblity(matrix, x, y):
    if x == 0 or x == (len(matrix) - 1) or y == 0 or y == (len(matrix[0]) - 1):
        return True
    up = matrix[:y, x]
    down = matrix[y + 1 :, x]  # inclusive end range + 1
    left = matrix[y, :x]
    right = matrix[y, x + 1 :]  # inclusive end range + 1

    threshold = matrix[y][x]
    for sight_line in [up, down, left, right]:
        visible = True
        for val in sight_line:
            if val >= threshold:
                visible = False
        if visible:
            return True
    return False


def part1_example():

    data = get_data(INPUT_EXAMPLE)
    answer = check_all_indices(data)
    assert answer == 21

    return answer


def part1():
    data = get_data(INPUT)
    answer = check_all_indices(data)
    return answer


def part2_example():
    return
    data = get_data(INPUT_EXAMPLE_EZI)
    answer = check_all_indices(data)
    assert answer == 1

    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = check_all_indices(data)
    assert answer == 2

    data = get_data(INPUT_EXAMPLE)
    answer = check_all_indices(data)
    assert answer == 3

    return answer


def part2():
    return
    data = get_data(INPUT)
    answer = check_all_indices(data)
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
