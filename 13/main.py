from pathlib import Path
import numpy as np

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> str:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return open(file_location, "r").read().strip()


def get_data(path):
    data = get_lines(path)
    dots, fold_insts = tuple(data.split("\n\n"))
    dots = [tuple(map(int, coords.split(","))) for coords in dots.split("\n")]

    fold_insts = [
        (line.strip().split("=")[0][-1], int(line.strip().split("=")[1]))
        for line in fold_insts.split("\n")
    ]
    return dots, fold_insts


def calc_visible_dots(dots, fold_insts, nbr_folds=1):
    x_max, y_max = (
        max([coord[0] for coord in dots]) + 1,
        max([coord[1] for coord in dots]) + 1,
    )
    matrix = np.zeros((y_max, x_max))
    for x, y in dots:
        matrix[y][x] = 1
    # print("nonzero", np.count_nonzero(matrix))
    for axis, nbr in fold_insts[:nbr_folds]:
        if axis == "y":
            next_matrix = matrix[:nbr, :]
            to_fold = matrix[nbr + 1 :, :]
            flipped_to_fold = np.flip(to_fold, axis=0)
            next_matrix[-flipped_to_fold.shape[0] :, :] += flipped_to_fold
            matrix = next_matrix
        else:
            next_matrix = matrix[:, :nbr]
            to_fold = matrix[:, nbr + 1 :]
            flipped_to_fold = np.flip(to_fold, axis=1)
            next_matrix[:, -flipped_to_fold.shape[1] :] += flipped_to_fold
            matrix = next_matrix
    return matrix


def part1_example():
    dots, fold_insts = get_data(INPUT_EXAMPLE)
    answer = calc_visible_dots(dots, fold_insts, 1)
    answer = np.count_nonzero(answer)
    assert answer == 17

    answer = calc_visible_dots(dots, fold_insts, 2)
    answer = np.count_nonzero(answer)
    assert answer == 16

    return answer


def part1():
    dots, fold_insts = get_data(INPUT)
    answer = calc_visible_dots(dots, fold_insts, 1)
    answer = np.count_nonzero(answer)
    return answer


def part2():
    dots, fold_insts = get_data(INPUT)
    answer = calc_visible_dots(dots, fold_insts, len(fold_insts))
    answer = np.where(answer > 0, 1, " ")
    script_location = Path(__file__).absolute().parent
    file_location = script_location / "code.txt"
    np.savetxt(file_location, answer, fmt="%s")
    return open(file_location, "r").read()


def main():
    ex1 = part1_example()
    p1 = part1()
    p2 = part2()
    print(f"example part 1: {ex1}")
    print(f"part 1: {p1}")
    print(f"part 2:\n{p2}")


if __name__ == "__main__":
    main()
