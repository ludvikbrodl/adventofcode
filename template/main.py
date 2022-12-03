from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return get_lines(path)


def x(y):
    return
    pass


def part1_example():
    return
    data = get_data(INPUT_EXAMPLE_EZI)
    answer = x(data)
    assert answer == 1

    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = x(data)
    assert answer == 2

    data = get_data(INPUT_EXAMPLE)
    answer = x(data)
    assert answer == 3

    return answer


def part1():
    return
    data = get_data(INPUT)
    answer = x(data)
    return answer


def part2_example():
    return
    data = get_data(INPUT_EXAMPLE_EZI)
    answer = x(data)
    assert answer == 1

    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = x(data)
    assert answer == 2

    data = get_data(INPUT_EXAMPLE)
    answer = x(data)
    assert answer == 3

    return answer


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
