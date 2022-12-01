from pathlib import Path
from typing import Counter

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return open(file_location, "r").read().strip()


def get_data(path) -> list[int]:
    data = get_lines(path)
    template, pairs = tuple(data.split("\n\n"))

    pairs = {
        line.strip().split(" -> ")[0]: line.strip().split(" -> ")[1]
        for line in pairs.split("\n")
    }
    return template, pairs


def naive(template, pairs_dict, nbr_steps):
    for nbr in range(nbr_steps):
        inserted_count = 0
        for idx, c in enumerate(template[:-1]):
            template_pair = (
                template[inserted_count + idx] + template[inserted_count + idx + 1]
            )
            # first_char, second_char = tuple(pairs[0])
            if template_pair in pairs_dict:
                char_to_insert = pairs_dict[template_pair]
                template = (
                    template[: inserted_count + idx + 1]
                    + char_to_insert
                    + template[inserted_count + idx + 1 :]
                )
                inserted_count += 1
    return template


def count_version(template, pairs_dict, nbr_steps):
    bins = Counter()
    for idx, c in enumerate(template[:-1]):
        template_pair = template[idx] + template[idx + 1]
        bins[template_pair] += 1

    # next_bins = bins
    for nbr in range(nbr_steps):
        # curr_bins = next_bins.copy()
        # next_bins = Counter()
        prev_bins = bins.copy()
        for template_pair, occurences in prev_bins.items():
            if template_pair in pairs_dict:
                bins[template_pair] -= occurences
                next_3_chars = (
                    template_pair[0] + pairs_dict[template_pair] + template_pair[1]
                )
                bins[next_3_chars[0:2]] += occurences
                bins[next_3_chars[1:3]] += occurences
    answer = Counter()
    for pairs, occurences in bins.items():
        answer[pairs[0]] += occurences
    # add the last char of the template as it will not be counted in loop above
    answer[template[-1]] += 1

    return answer


def part1_example():
    template, pairs = get_data(INPUT_EXAMPLE)
    answer = naive(template, pairs, 10)
    counts = Counter(answer)
    most_common, least_common = counts.most_common()[0], counts.most_common()[-1]
    assert most_common[1] == 1749
    assert least_common[1] == 161
    result = most_common[1] - least_common[1]
    assert result == 1588

    return result


def part1():
    template, pairs = get_data(INPUT)
    answer = naive(template, pairs, 10)
    counts = Counter(answer)
    most_common, least_common = counts.most_common()[0], counts.most_common()[-1]
    result = most_common[1] - least_common[1]
    return result


def part2_example():
    template, pairs = get_data(INPUT_EXAMPLE)

    answer = count_version(template, pairs, 10)
    most_common, least_common = answer.most_common()[0], answer.most_common()[-1]
    assert most_common[1] == 1749
    assert least_common[1] == 161
    result = most_common[1] - least_common[1]
    assert result == 1588

    answer = count_version(template, pairs, 40)
    most_common, least_common = answer.most_common()[0], answer.most_common()[-1]
    assert most_common[1] == 2192039569602
    assert least_common[1] == 3849876073
    result = most_common[1] - least_common[1]
    assert result == 2188189693529

    return result


def part2():
    template, pairs = get_data(INPUT)
    answer = count_version(template, pairs, 40)
    counts = Counter(answer)
    most_common, least_common = counts.most_common()[0], counts.most_common()[-1]
    result = most_common[1] - least_common[1]
    return result


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
