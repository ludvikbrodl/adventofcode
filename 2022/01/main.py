from pathlib import Path

INPUT = "input.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").read().split("\n\n")]


def get_data(path) -> list[int]:
    return [[int(x) for x in l.split("\n")] for l in get_lines(path)]


def part1():
    data = get_data(INPUT)
    return max([sum(x) for x in data])


def part2():
    data = get_data(INPUT)
    return sum(sorted([sum(x) for x in data])[-3:])


def main():
    p1 = part1()
    p2 = part2()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
