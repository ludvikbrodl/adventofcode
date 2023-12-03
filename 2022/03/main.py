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


def findPrio(rucksackContent):
    data = set()
    midIdx = int(len(rucksackContent) / 2)
    compartmentA = rucksackContent[:midIdx]
    compartmentB = rucksackContent[midIdx:]
    for c in compartmentA:
        data.add(c)
    for c in compartmentB:
        if c in data:
            return charToPrio(c)


def charToPrio(c):
    val = ord(c)
    if val >= 97:
        return val - 96
    else:
        return val - 64 + 26


def findBadgePrio(a, b, c):
    rucksacks = [set() for x in range(3)]
    for content, theSet in zip([a, b, c], rucksacks):
        theSet.update(*content)
    overlap = set.intersection(*rucksacks)
    return charToPrio(overlap.pop())


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = sum([findPrio(rucksack) for rucksack in data])
    assert answer == 157
    return answer


def part1():
    data = get_data(INPUT)
    answer = sum([findPrio(rucksack) for rucksack in data])
    return answer


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    answer = sum([findBadgePrio(*data[i : i + 3]) for i in range(0, len(data), 3)])
    assert 70
    return answer


def part2():
    data = get_data(INPUT)
    answer = sum([findBadgePrio(*data[i : i + 3]) for i in range(0, len(data), 3)])
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
