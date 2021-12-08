from collections import defaultdict
from pathlib import Path
import copy

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"


def getLines(path: str):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return open(file_location, "r").readlines()


def getOutput(line: str):
    return line.split(" | ")[1]


def getInput(line: str):
    return line.split(" | ")[0]


def get_data(path):
    lines = getLines(path)
    nbr_seq = lines[0].strip().split(",")
    board_lines = [l.strip() for l in lines[2:]]
    boards: list[list[int]] = []
    for board_id in range(int((len(board_lines) + 1) / 6)):
        boards.append([])
        for row in range(5):
            cols = board_lines[board_id * 6 + row].split()
            boards[board_id].append(cols)
    return nbr_seq, boards


def get_hit_coord(board, val_to_match):
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == val_to_match:
                return y, x
    return None, None


def checkForBingo(hit_board):
    for y, row in enumerate(hit_board):
        if row == [1, 1, 1, 1, 1]:
            return True, hit_board
        if (
            hit_board[0][y]
            & hit_board[1][y]
            & hit_board[2][y]
            & hit_board[3][y]
            & hit_board[4][y]
        ):
            return True, hit_board


def get_winning_board(path):
    nbr_seq, boards = get_data(path)
    hit_boards = create_hit_board(boards)
    for nbr in nbr_seq:
        for board_idx, board in enumerate(boards):
            y, x = get_hit_coord(board, nbr)
            if y != None:
                hit_boards[board_idx][y][x] = 1
                if checkForBingo(hit_boards[board_idx]):
                    return board, hit_boards[board_idx], nbr


def get_sum_of_non_hits(board, hitBoard):
    sum = 0
    for y, row in enumerate(hitBoard):
        for x, val in enumerate(row):
            if val == 0:
                sum += int(board[y][x])
    return sum


def create_hit_board(boards):
    HIT_MATRIX = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    boards_hit = []
    for x in range(len(boards)):
        boards_hit.append(copy.deepcopy(HIT_MATRIX))
    return boards_hit


def part1_example():
    board, hit_board, last_nbr = get_winning_board(INPUT_EXAMPLE)
    sum_of_non_hit = get_sum_of_non_hits(board, hit_board)
    answer = sum_of_non_hit * int(last_nbr)
    assert sum_of_non_hit == 188
    assert last_nbr == "24"
    assert answer == 4512
    return answer


def part1():
    board, hit_board, last_nbr = get_winning_board(INPUT)
    sum_of_non_hit = get_sum_of_non_hits(board, hit_board)
    answer = sum_of_non_hit * int(last_nbr)
    return answer


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
