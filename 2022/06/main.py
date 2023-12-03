from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return open(file_location, "r").read().strip()


def get_data(path) -> list[int]:
    return get_lines(path)


START_OF_PACKET_LENGTH = 4


def x(data, packet_length=START_OF_PACKET_LENGTH):
    seq = [
        "dummy"
    ]  # needs to be here otherwise the loop will pop the first marker on idx == pack_length
    for idx, marker in enumerate(data):
        seq.append(marker)
        if idx < packet_length - 1:
            continue
        seq.pop(0)
        if len(set(seq)) >= packet_length:
            return idx + 1
        # oldestMarker = marker


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = x(data)
    assert answer == 6

    return answer


def part1():
    data = get_data(INPUT)
    return x(data)
    data = get_data(INPUT)
    answer = x(data)
    return answer


def part2_example():
    assert x("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert x("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert x("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert x("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert x("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
    return


def part2():
    data = get_data(INPUT)
    return x(data, 14)
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
