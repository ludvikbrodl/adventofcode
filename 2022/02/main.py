from pathlib import Path

INPUT = "input.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return [l.split(" ") for l in get_lines(path)]


# opp/you
# A/X rock
# B/Y paper
# C/Z scissor
SCORE_MAP = {"X": 1, "Y": 2, "Z": 3}
ROUND_SCORE = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3},
}


def part1():
    data = get_data(INPUT)
    score = 0
    for fight in data:
        opp = fight[0]
        you = fight[1]
        score += SCORE_MAP[you]
        score += ROUND_SCORE[you][opp]
    return score


# X = lose
# Y = draw
# Z = win
SELECT_HAND_MAP = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"},
}


def part2():
    data = get_data(INPUT)
    score = 0
    for fight in data:
        opp = fight[0]
        outcome = fight[1]
        you = SELECT_HAND_MAP[outcome][opp]
        score += SCORE_MAP[you]
        score += ROUND_SCORE[you][opp]
    return score


def main():
    p1 = part1()
    p2 = part2()
    print(f"part 1: {p1}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
