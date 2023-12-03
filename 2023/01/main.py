from pathlib import Path
import re

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EZI = "input_example_ezi.txt"


# Mapping of words to numeric values
word_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").read().split("\n")]


def get_data(path) -> list[str]:
    return [l for l in get_lines(path)]


def part2_example():
    data = get_data(INPUT_EZI)
    answer = part2_calc(data)
    assert answer == 281

    return answer


def extract_numbers_part2(line):
    digits = []
    for idx, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            split_str = line[idx:]
            for word in word_to_digit.keys():
                if split_str.startswith(word):
                    digits.append(word_to_digit[word])
    # Extract the first and last numbers
    first_number = digits[0]
    last_number = digits[-1]

    return first_number, last_number


def part2_calc(data):
    total_sum = 0

    for line in data:
        # Find all digits in the line
        first_digit, last_digit = extract_numbers_part2(line)
        # Combine the digits to form a 2-digit number
        two_digit_number = first_digit * 10 + last_digit

        # Accumulate the sum
        total_sum += two_digit_number

    return total_sum


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = part1_calc(data)
    assert answer == 142

    return answer


def part1():
    data = get_data(INPUT)
    return part1_calc(data)


def part1_calc(data):
    total_sum = 0

    for line in data:
        # Find all digits in the line
        digits = [int(char) for char in line if char.isdigit()]

        # Check if at least two digits are found
        if len(digits) >= 2:
            # Extract the first and last digits from the list
            first_digit = digits[0]
            last_digit = digits[-1]
        else:
            first_digit = digits[0]
            last_digit = digits[0]
        # Combine the digits to form a 2-digit number
        two_digit_number = first_digit * 10 + last_digit

        # Accumulate the sum
        total_sum += two_digit_number

    return total_sum


def part2():
    data = get_data(INPUT)
    answer = part2_calc(data)

    return answer


def main():
    part1_example()
    p1 = part1()
    print(f"part 1: {p1}")
    part2_example()
    p2 = part2()
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
