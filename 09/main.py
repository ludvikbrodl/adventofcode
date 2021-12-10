from collections import defaultdict
from pathlib import Path
import copy

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def getLines(path: str):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path):
    heatmap: list[list[int]] = [
        [int(digit) for digit in line] for line in getLines(path)
    ]
    return heatmap


# adjecent in this case are 4 positions = above, below, right, left
def get_adj_values(heatmap, x, y):
    coords = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
    vals = []
    for x, y in coords:
        if x >= 0 and y >= 0 and y < len(heatmap[0]) and x < len(heatmap):
            vals.append(heatmap[x][y])
    return vals


# adjecent in this case are 4 positions = above, below, right, left
def get_adj_coordinates(heatmap, x, y):
    coords = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
    checked_coords = []
    for x, y in coords:
        if x >= 0 and y >= 0 and y < len(heatmap[0]) and x < len(heatmap):
            checked_coords.append((x, y))
    return checked_coords


def get_sum_of_non_hits(board, hitBoard):
    sum = 0
    for y, row in enumerate(hitBoard):
        for x, val in enumerate(row):
            if val == 0:
                sum += int(board[y][x])
    return sum


def calc_hits(heatmap):
    hitboard = create_mask_3d_array(heatmap)
    for x, _ in enumerate(heatmap):
        for y, _ in enumerate(heatmap[0]):
            adjs = get_adj_values(heatmap, x, y)
            less_than_count = 0
            for adj_value in adjs:
                if adj_value > heatmap[x][y]:
                    less_than_count += 1
                if less_than_count == len(adjs):
                    hitboard[x][y] = 1
    return hitboard


def create_mask_3d_array(heatmap):
    return [[0] * len(heatmap[0]) for x in range(len(heatmap))]


def calc_risk_level(heatmap, low_point_mask):
    risk_level = 0
    for x, mask_col in enumerate(low_point_mask):
        for y, mask_val in enumerate(mask_col):
            if mask_val == 1:
                risk_level += 1 + heatmap[x][y]
    return risk_level


def calc_basin_masks(heatmap, low_point_mask):
    low_point_coords = []
    for x, row in enumerate(low_point_mask):
        for y, val in enumerate(row):
            if val == 1:
                low_point_coords.append((x, y))
    basin_masks = []
    for lp_x, lp_y in low_point_coords:
        basin_mask = create_mask_3d_array(heatmap)
        basin_masks.append(basin_mask)
        recursive_adjecent_add(heatmap, basin_mask, lp_x, lp_y)
    return basin_masks


def recursive_adjecent_add(heatmap, mask, x, y):
    mask[x][y] = 1
    adj_coords = get_adj_coordinates(heatmap, x, y)
    for a_x, a_y in adj_coords:
        a_val = heatmap[a_x][a_y]
        if a_val < 9 and a_val > heatmap[x][y]:
            recursive_adjecent_add(heatmap, mask, a_x, a_y)


def sum_of_3d_list(arr: list[list[int]]):
    sum = 0
    for row in arr:
        for val in row:
            sum += val
    return sum


def sort_masks_on_size(list_of_3d_lists: list[list[list[int]]]):
    return sorted(list_of_3d_lists, key=sum_of_3d_list)


def part1_example():
    heatmap = get_data(INPUT_EXAMPLE)
    low_point_mask = calc_hits(heatmap)
    risk_level = calc_risk_level(heatmap, low_point_mask)
    answer = risk_level
    assert answer == 15
    return answer


def part1():
    heatmap = get_data(INPUT)
    low_point_mask = calc_hits(heatmap)
    risk_level = calc_risk_level(heatmap, low_point_mask)
    answer = risk_level
    return answer


def part2_example():
    heatmap = get_data(INPUT_EXAMPLE)
    low_point_mask = calc_hits(heatmap)
    basin_masks = calc_basin_masks(heatmap, low_point_mask)
    size_sorted_basin_masks = sort_masks_on_size(basin_masks)
    answer = 1
    for basin_mask in size_sorted_basin_masks[-3:]:
        answer *= sum_of_3d_list(basin_mask)
    assert answer == 1134
    return answer


def part2():
    heatmap = get_data(INPUT)
    low_point_mask = calc_hits(heatmap)
    basin_masks = calc_basin_masks(heatmap, low_point_mask)
    size_sorted_basin_masks = sort_masks_on_size(basin_masks)
    answer = 1
    for basin_mask in size_sorted_basin_masks[-3:]:
        answer *= sum_of_3d_list(basin_mask)
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
