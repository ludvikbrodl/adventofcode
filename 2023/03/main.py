from pathlib import Path
import re
from typing import List

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"

# WIDTH = 140
# HEIGHT = 140
# WIDTH = 10
# HEIGHT = 10


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[str]:
    return get_lines(path)


DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),  # Adjacent positions
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]  # Diagonal positions


class SerialNumber:
    def __init__(self, value, positions):
        self.value = value
        self.positions = positions

    def get_adjacent_positions(self, matrix):
        # Define possible relative positions (up, down, left, right)
        for pos in self.positions:
            for dr, dc in DIRECTIONS:
                new_row, new_col = pos[0] + dr, pos[1] + dc

                # Check if the new position is within the bounds of the matrix
                if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                    yield (new_row, new_col)

    def is_valid_machine_number(self, matrix):
        for adj_pos in self.get_adjacent_positions(matrix):
            if bool(re.match(r"[^.\d]+", matrix[adj_pos[1]][adj_pos[0]])):
                return True
        return False


class Cog:
    def __init__(self, position):
        self.position = position
        self.adj_numbers = []


def part1_calc(lines):
    all_serial_numbers = []
    pattern = re.compile(r"\d+")
    for y_pos, line in enumerate(lines):
        matches = pattern.finditer(line)
        for match in matches:
            number = match.group()
            start_position = match.start()
            end_position = match.end()
            # Extract individual digit positions
            positions = []
            for x_pos in range(start_position, end_position):
                positions.append((x_pos, y_pos))
            all_serial_numbers.append(SerialNumber(number, positions))

    matrix = []
    for y_pos, line in enumerate(lines):
        row_data = []
        for x_pos, c in enumerate(line):
            row_data.append(c)
        matrix.append(row_data)
    sum = 0
    for serial_number in all_serial_numbers:
        if serial_number.is_valid_machine_number(matrix):
            sum += int(serial_number.value)
    return sum


def part2_calc(lines):
    number_pattern = re.compile(r"\d+")
    cogs: List[Cog] = []
    all_serial_numbers: List[SerialNumber] = []

    # Only here to get the size of the data
    matrix = []
    for y_pos, line in enumerate(lines):
        row_data = []
        for x_pos, c in enumerate(line):
            row_data.append(c)
        matrix.append(row_data)

    # Create the cogs
    for y_pos, line in enumerate(lines):
        for x_pos, c in enumerate(line):
            if c == "*":
                cogs.append(Cog((x_pos, y_pos)))

    # Create the machine numbers
    for y_pos, line in enumerate(lines):
        matches = number_pattern.finditer(line)
        for match in matches:
            number = match.group()
            start_position = match.start()
            end_position = match.end()
            # Extract individual digit positions
            positions = []
            for x_pos in range(start_position, end_position):
                positions.append((x_pos, y_pos))

            all_serial_numbers.append(SerialNumber(number, positions))

    # Add all adjecent serial numbers to the cogs
    for cog in cogs:
        for serial_number in all_serial_numbers:
            if cog.position in serial_number.get_adjacent_positions(matrix):
                cog.adj_numbers.append(int(serial_number.value))

    # Calc the final value
    sum = 0
    for cog in cogs:
        if len(cog.adj_numbers) > 1:
            sum += cog.adj_numbers[0] * cog.adj_numbers[1]

    return sum


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = part1_calc(data)
    assert answer == 4361, answer

    return answer


def part1():
    data = get_data(INPUT)
    answer = part1_calc(data)
    return answer


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    answer = part2_calc(data)
    assert answer == 467835

    return answer


def part2():
    data = get_data(INPUT)
    answer = part2_calc(data)
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
