from collections import defaultdict
from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"

segmentCount2Digit = {
    2: "[1]",
    3: "[7]",
    4: "[4]",
    5: "[2, 3, 5]",
    6: "[0, 6, 9]",
    7: "[8]",
}

digit2SegmentCount = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 0: 6}

digit2Positions = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"],
}

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


def getLines(path: str):
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return open(file_location, "r").readlines()


def getOutput(line: str):
    return line.split(" | ")[1]


def getInput(line: str):
    return line.split(" | ")[0]


def digitMatch(charList: list[str]):
    match len(charList):
        case 1:
            return [0]


def count_unique_outputs(path):
    lines = getLines(path)
    # key = digits: list[int]
    # value = occurences
    d = defaultdict(int)
    for l in lines:
        out = getOutput(l).strip()
        for chars in out.split():
            charCount = len(chars)
            d[segmentCount2Digit[charCount]] += 1

    filterDigits = ["[1]", "[4]", "[7]", "[8]"]
    occurence_1478 = 0
    for key, chars in d.items():
        if key in filterDigits:
            occurence_1478 += chars
    return occurence_1478


def part1_example():
    x = count_unique_outputs(INPUT_EXAMPLE)
    assert x == 26
    return x


def part1():
    return count_unique_outputs(INPUT)


def part2_example():
    lines = getLines(INPUT_EXAMPLE)


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
