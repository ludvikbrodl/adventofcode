from collections import defaultdict
from pathlib import Path
import numpy as np
from itertools import product

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return np.array([[int(digit) for digit in line] for line in get_lines(path)])


def get_adj_coords(coords: list[list[int]]):
    for x, y in zip(coords[0], coords[1]):
        xs = range(x - 1, x + 2)
        ys = range(y - 1, y + 2)
        for x, y in list(product(xs, ys)):
            if 0 <= x <= 9 and 0 <= y <= 9:
                yield x, y


def simulate_step(octopuses):
    matrix = np.array(octopuses, copy=True)
    matrix = matrix + 1  # grow all octos with 1
    will_flash = np.where(matrix > 9)
    while len(will_flash[0]):
        matrix = np.where(matrix < 10, matrix, -1)
        flashed_neighbours = get_adj_coords(will_flash)
        for x, y in flashed_neighbours:
            if matrix[x][y] >= 0:
                matrix[x][y] += 1
        will_flash = np.where(matrix > 9)
    matrix = np.where(matrix != -1, matrix, 0)
    return matrix


def simulate_flashes(octopuses, nbr_steps):
    flashes = np.array(octopuses, copy=True)
    tot = 0
    for step in range(nbr_steps):
        flashes = simulate_step(flashes)
        flashed_coords = np.where(flashes == 0)
        tot += len(flashed_coords[0])
    return tot


def part1_example():
    octopuses = get_data("input_example_ezi.txt")
    flashes = simulate_flashes(octopuses, 2)
    assert flashes == 9
    octopuses = get_data(INPUT_EXAMPLE)
    flashes = simulate_flashes(octopuses, 2)
    assert flashes == 35
    flashes = simulate_flashes(octopuses, 100)
    assert flashes == 1656
    return flashes


def part1():
    octopuses = get_data(INPUT)
    flashes = simulate_flashes(octopuses, 100)
    return flashes


def part2_example():
    pass


def part2():
    pass


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
