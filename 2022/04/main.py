from pathlib import Path
import re

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    data = [re.search(r"(\d+-\d+),(\d+-\d+)", line) for line in get_lines(path)]
    intervals = [[x.group(1).split("-"), x.group(2).split("-")] for x in data]
    return intervals


def getCompleteOverlapCount(intervals):
    count = 0
    for aInterval, bInterval in intervals:
        aSet = set(range(int(aInterval[0]), int(aInterval[1]) + 1))
        bSet = set(range(int(bInterval[0]), int(bInterval[1]) + 1))
        union = aSet.intersection(bSet)
        if len(union) >= min(len(aSet), len(bSet)):
            count += 1
    return count


def getSingleItemOverlapCount(intervals):
    count = 0
    for aInterval, bInterval in intervals:
        aSet = set(range(int(aInterval[0]), int(aInterval[1]) + 1))
        bSet = set(range(int(bInterval[0]), int(bInterval[1]) + 1))
        union = aSet.intersection(bSet)
        if len(union) >= 1:
            count += 1
    return count


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = getCompleteOverlapCount(data)
    assert answer == 2

    return answer


def part1():
    data = get_data(INPUT)
    answer = getCompleteOverlapCount(data)
    return answer


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    answer = getSingleItemOverlapCount(data)
    assert answer == 4
    return answer


def part2():
    data = get_data(INPUT)
    answer = getSingleItemOverlapCount(data)
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
