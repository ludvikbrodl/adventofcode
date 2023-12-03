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
    data: list[list[str]] = [[char for char in line] for line in getLines(path)]
    return data


CHARS = {"{": "}", "[": "]", "<": ">", "(": ")"}

POINTS_PART1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

POINTS_PART2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def validate_chunks(lines: list[str]):
    errors = []
    incomplete_lines = []
    for line in lines:
        invalid_char = assert_code(line)
        if invalid_char:
            errors.append(invalid_char)
        else:
            incomplete_lines.append(line)
    return errors, incomplete_lines


def assert_code(code):
    stack: list[str] = []
    for token in code:
        if token in CHARS.keys():  # opening token
            stack.append(token)
        else:  # closing token
            last_token = stack.pop()
            if CHARS[last_token] != token:
                return token


def calc_score_part1(tokens):
    return sum([POINTS_PART1[token] for token in tokens])


def complete_line(line):
    stack: list[str] = []
    for token in line:
        if token in CHARS.keys():  # opening token
            stack.append(token)
        else:  # closing token
            stack.pop()
    stack.reverse()
    return [CHARS[token] for token in stack]


def find_missing_tokens(incomplete_lines):
    missing_tokens_lines: list[str] = []
    for line in incomplete_lines:
        completion_tokens = complete_line(line)
        missing_tokens_lines.append(completion_tokens)
    return missing_tokens_lines


def calc_score_part2(lines):
    sums = []
    for line in lines:
        line_sum = 0
        for token in line:
            line_sum *= 5
            line_sum += POINTS_PART2[token]
        sums.append(line_sum)
    sorted_sums = sorted(sums)
    return sorted_sums[len(sorted_sums) // 2]  # // = floor division


def part1_example():
    lines = get_data(INPUT_EXAMPLE)
    invalid_tokens, _ = validate_chunks(lines)
    score = calc_score_part1(invalid_tokens)
    assert 26397 == score
    return score


def part1():
    lines = get_data(INPUT)
    invalid_tokens, _ = validate_chunks(lines)
    score = calc_score_part1(invalid_tokens)
    return score


def part2_example():
    lines = get_data(INPUT_EXAMPLE)
    _, incomplete_lines = validate_chunks(lines)
    completion_lines = find_missing_tokens(incomplete_lines)
    score = calc_score_part2(completion_lines)
    return score


def part2():
    lines = get_data(INPUT)
    _, incomplete_lines = validate_chunks(lines)
    completion_lines = find_missing_tokens(incomplete_lines)
    score = calc_score_part2(completion_lines)
    return score


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
