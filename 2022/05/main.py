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


def get_start_state(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    state = re.search("(.*?) \n\n", open(file_location, "r").read(), re.DOTALL)[0]
    return state.split("\n")[:-2]


def get_instructions(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    instructions = re.search("move(.*)", open(file_location, "r").read(), re.DOTALL)[0]

    return instructions.split("\n")


def get_data(path) -> list[int]:
    return (get_start_state(path), get_instructions(path))


def simulate_reorder_9000(y):
    start_state, inst = get_data(y)
    nbr_stacks = int(start_state[-1][-2])
    stacks = [[] for x in range(nbr_stacks)]
    start_state = start_state[:-1]
    for x in reversed(start_state):
        for stack_idx, stack_idx_in_state in zip(
            range(nbr_stacks), range(1, len(x), 4)
        ):
            letter = x[stack_idx_in_state]
            if letter != " ":
                stacks[stack_idx].append(letter)
    for op in inst:
        matches = re.search("move (\d+) from (\d+) to (\d+)", op)
        times, fromIdx, toIdx = matches[1], matches[2], matches[3]
        for _ in range(int(times)):
            letter_to_move = stacks[int(fromIdx) - 1].pop()
            stacks[int(toIdx) - 1].append(letter_to_move)
    return "".join([x[-1] for x in stacks])


def simulate_reorder_9001(y):
    start_state, inst = get_data(y)
    nbr_stacks = int(start_state[-1][-2])
    stacks = [[] for x in range(nbr_stacks)]
    start_state = start_state[:-1]
    for x in reversed(start_state):
        for stack_idx, stack_idx_in_state in zip(
            range(nbr_stacks), range(1, len(x), 4)
        ):
            letter = x[stack_idx_in_state]
            if letter != " ":
                stacks[stack_idx].append(letter)
    for op in inst:
        matches = re.search("move (\d+) from (\d+) to (\d+)", op)
        nbr_crates, fromIdx, toIdx = matches[1], matches[2], matches[3]
        crate_group = []  # only diff from 9000 is from here and down
        for _ in range(int(nbr_crates)):
            letter_to_move = stacks[int(fromIdx) - 1].pop()
            crate_group.append(letter_to_move)

        for letter in reversed(crate_group):
            stacks[int(toIdx) - 1].append(letter)
    return "".join([x[-1] for x in stacks])


def part1_example():
    answer = simulate_reorder_9000(INPUT_EXAMPLE)
    assert answer == "CMZ"
    return answer


def part1():
    answer = simulate_reorder_9000(INPUT)
    return answer


def part2_example():
    answer = simulate_reorder_9001(INPUT_EXAMPLE)
    assert answer == "MCD"
    return answer


def part2():
    answer = simulate_reorder_9001(INPUT)
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
