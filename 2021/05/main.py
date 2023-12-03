from collections import defaultdict
from pathlib import Path
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def get_lines(path: str):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path):
    # [(start, end)] where start & end = (x, y)
    data: list[tuple(tuple(int, int))] = []
    for line in get_lines(path):
        start, end = line.split(" -> ")
        data.append(
            (
                tuple([int(coord) for coord in start.split(",")]),
                tuple([int(coord) for coord in end.split(",")]),
            )
        )
    return data


def get_size(entries):
    all_start = [t[0] for t in entries]
    all_end = [t[1] for t in entries]
    all_coords = all_start + all_end
    all_x = [coord[0] for coord in all_coords]
    all_y = [coord[1] for coord in all_coords]
    return max(all_x) + 1, max(all_y) + 1


def filter_horizontal_and_vertical(entries):
    filtered = []
    diagonal = []
    for start, end in entries:
        x0, y0 = start
        x1, y1 = end
        if x0 == x1 or y0 == y1:
            filtered.append((start, end))
        else:
            diagonal.append((start, end))
    return filtered, diagonal


def create_mask_matrix(x, y):
    return [[0] * y for x in range(x)]


# this function is extremely expensive - not sure why
def sum_of_matrixes(arr: list[list[list[int]]]):
    sum_matrix = np.zeros(shape=(len(arr[0]), len(arr[0][0])))
    for matrix in arr:
        sum_matrix += np.array(matrix)
    return sum_matrix


def calc_path(entry, fresh_mask):
    (x0, y0), (x1, y1) = entry
    x_low = x0 if x0 < x1 else x1
    x_high = x1 if x1 > x0 else x0
    y_low = y0 if y0 < y1 else y1
    y_high = y1 if y1 > y0 else y0
    for x in range(x_low, x_high + 1):
        for y in range(y_low, y_high + 1):
            fresh_mask[y][x] = 1


def calc_path_diagonal(entry, fresh_mask):
    (x0, y0), (x1, y1) = entry
    x_low = x0 if x0 < x1 else x1
    x_high = x1 if x1 > x0 else x0
    # left -> right
    if x0 < x1:
        x_dir = 1
    # right -> left
    else:
        x_dir = -1
    # down -> up
    if y0 < y1:
        y_dir = 1
    # up -> down
    else:
        y_dir = -1
    for count in range(x_high - x_low + 1):
        fresh_mask[y0 + count * y_dir][x0 + count * x_dir] = 1


def calc_danger_zone_incl_diagonal(entries):
    x_len, y_len = get_size(entries)
    non_diagonal_entries, diagonal = filter_horizontal_and_vertical(entries)
    masks: list[list[list[int]]] = []
    for e in non_diagonal_entries:
        mask = create_mask_matrix(x_len, y_len)
        calc_path(e, mask)
        masks.append(mask)
    for e in diagonal:
        mask = create_mask_matrix(x_len, y_len)
        calc_path_diagonal(e, mask)
        masks.append(mask)
    # sum masks to get danger zone
    return sum_of_matrixes(masks)


def calc_danger_zone(entries):
    x_len, y_len = get_size(entries)
    non_diagonal_entries, _ = filter_horizontal_and_vertical(entries)
    masks: list[list[list[int]]] = []
    for e in non_diagonal_entries:
        mask = create_mask_matrix(x_len, y_len)
        calc_path(e, mask)
        masks.append(mask)
    # sum masks to get danger zone
    return sum_of_matrixes(masks)


def count_overlaps(matrix: list[list[int]]):
    sum = 0
    for row in matrix:
        for val in row:
            if val > 1:
                sum += 1
    return sum


def part1_example():
    entries: list[tuple(tuple(int, int))] = get_data(INPUT_EXAMPLE)
    danger_matrix = calc_danger_zone(entries)
    overlap_count = count_overlaps(danger_matrix)
    assert 5 == overlap_count
    return overlap_count


def part1():
    return  # 10 second run time, skip during dev
    entries: list[tuple(tuple(int, int))] = get_data(INPUT)
    danger_matrix = calc_danger_zone(entries)
    overlap_count = count_overlaps(danger_matrix)
    return overlap_count


def part2_example():
    entries: list[tuple(tuple(int, int))] = get_data(INPUT_EXAMPLE)
    danger_matrix = calc_danger_zone_incl_diagonal(entries)
    overlap_count = count_overlaps(danger_matrix)
    assert 12 == overlap_count
    return overlap_count


def part2():
    # return
    entries: list[tuple(tuple(int, int))] = get_data(INPUT)
    danger_matrix = calc_danger_zone_incl_diagonal(entries)
    overlap_count = count_overlaps(danger_matrix)
    return overlap_count


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
