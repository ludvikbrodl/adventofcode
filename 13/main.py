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
        print("matrix shape", matrix.shape)
        if axis == "x":
            new_matrix = matrix[:, :nbr]
            to_flip_part = matrix[:, nbr + 1 :]
            flipped = np.flip(to_flip_part, axis=1)
            matrix = new_matrix[:, : flipped.shape[1]] + flipped
        else:
            new_matrix = matrix[:nbr][:]
            to_flip_part = matrix[nbr + 1 :][:]
            flipped = np.flip(to_flip_part, axis=0)
            matrix = new_matrix[: flipped.shape[0]][:] + flipped
        print("to_flip_part", to_flip_part)
        print("flipped", flipped)
        print("matrix", matrix)

    print("matrix shape", matrix.shape)
    # odd = 0 if nbr % 2 == 1 else 1
    # if axis == "x":
    #     to_fold_part = matrix[:, nbr:]
    #     flipped = np.flip(to_fold_part, axis=1)
    #     matrix = matrix[:, : nbr + odd] + flipped
    # else:
    #     to_fold_part = matrix[nbr:][:]
    #     flipped = np.flip(to_fold_part, axis=0)
    #     matrix = matrix[: nbr + odd][:] + flipped
    #     # matrix =
    return np.count_nonzero(matrix)


def part1_example():
    dots, fold_insts = get_data(INPUT_EXAMPLE)
    answer = calc_visible_dots(dots, fold_insts, 1)
    assert answer == 17

    answer = calc_visible_dots(dots, fold_insts, 2)
    assert answer == 16

    return answer


def part1():
    dots, fold_insts = get_data(INPUT)
    answer = calc_visible_dots(dots, fold_insts, 1)
    return answer


def part2_example():
    return
    # data = get_data(INPUT_EXAMPLE)
    # answer = x(data)
    # assert answer == 3

    # return answer


def part2():
    return
    data = get_data(INPUT)
    answer = x(data)
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
