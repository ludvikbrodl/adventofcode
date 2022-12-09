from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[str]:
    return get_lines(path)


def simulate_movement(cmds):
    head = [0, 0]
    tail = [0, 0]
    tail_positions = set([tuple(tail)])
    for cmd in cmds:
        direction, nbr = cmd.split(" ")
        nbr = int(nbr)
        x_delta = 0
        y_delta = 0
        if direction == "R":
            x_delta = 1
        elif direction == "D":
            y_delta = -1
        elif direction == "U":
            y_delta = 1
        elif direction == "L":
            x_delta = -1
        for _ in range(nbr):
            head[0] += x_delta
            head[1] += y_delta
            x_diff = head[0] - tail[0]
            y_diff = head[1] - tail[1]
            # H = head
            # T = tail
            if (abs(x_diff) <= 1) and (abs(y_diff) <= 1):
                # if head and tail are "adjecent"/overlapping
                # no movement of the tail takes places
                continue
            if abs(x_diff) == 2 and y_diff == 0:
                # .....
                # H.T.H
                # .....
                tail[0] += int(x_diff / 2)
            elif abs(y_diff) == 2 and x_diff == 0:
                # .H.
                # ...
                # .T.
                # ...
                # .H.
                tail[1] += int(y_diff / 2)
            elif abs(x_diff) == 2:
                # H...H
                # ..T..
                # H...H
                tail[0] += int(x_diff / 2)
                tail[1] += y_diff
                pass
            elif abs(y_diff) == 2:
                # H.H
                # ...
                # .T.
                # ...
                # H.H
                tail[0] += x_diff
                tail[1] += int(y_diff / 2)
            tail_positions.add(tuple(tail))

    return len(tail_positions)


def simulate_movement_9_knots(cmds):
    head = [0, 0]
    knots = [[0, 0] for x in range(9)]
    tail_positions = set([(int(0), int(0))])

    for cmd in cmds:
        direction, nbr = cmd.split(" ")
        nbr = int(nbr)
        x_delta = 0
        y_delta = 0
        if direction == "R":
            x_delta = 1
        elif direction == "D":
            y_delta = -1
        elif direction == "U":
            y_delta = 1
        elif direction == "L":
            x_delta = -1
        for _ in range(nbr):
            head[0] += x_delta
            head[1] += y_delta
            all_objects_to_move = [head] + knots
            for knot_idx, (prev_knot, current_knot) in enumerate(
                zip(all_objects_to_move, all_objects_to_move[1:])
            ):
                x_diff = prev_knot[0] - current_knot[0]
                y_diff = prev_knot[1] - current_knot[1]
                # H = head
                # T = tail
                if (abs(x_diff) <= 1) and (abs(y_diff) <= 1):
                    # if head and tail are "adjecent"/overlapping
                    # no movement of the tail takes places
                    continue
                if abs(x_diff) == 2 and y_diff == 0:
                    # .....
                    # H.T.H
                    # .....
                    current_knot[0] += int(x_diff / 2)
                elif abs(y_diff) == 2 and x_diff == 0:
                    # .H.
                    # ...
                    # .T.
                    # ...
                    # .H.
                    current_knot[1] += int(y_diff / 2)
                elif (abs(x_diff) == 2) and (abs(y_diff) == 2):
                    # this case took me a while to find :()
                    # diagonal movement
                    # H.....H
                    # .......
                    # ...T...
                    # .......
                    # H.....H
                    current_knot[0] += int(x_diff / 2)
                    current_knot[1] += int(y_diff / 2)

                elif abs(x_diff) == 2:
                    # H...H
                    # ..T..
                    # H...H
                    current_knot[0] += int(x_diff / 2)
                    current_knot[1] += y_diff
                    pass
                elif abs(y_diff) == 2:
                    # H.H
                    # ...
                    # .T.
                    # ...
                    # H.H
                    current_knot[0] += x_diff
                    current_knot[1] += int(y_diff / 2)
                tail_positions.add(tuple(knots[-1]))
            pass

    return len(tail_positions), tail_positions


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    answer = simulate_movement(data)
    assert answer == 13

    return answer


def part1():
    data = get_data(INPUT)
    answer = simulate_movement(data)

    return answer


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    answer = simulate_movement_9_knots(data)[0]
    assert answer == 1
    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = simulate_movement_9_knots(data)
    assert answer[0] == 36
    print_tail_positions(answer[1])

    return answer[0]


def print_tail_positions(positions):
    x_coords = [pos[0] for pos in positions]
    y_coords = [pos[1] for pos in positions]
    for y_idx in reversed(range(min(y_coords), max(y_coords) + 1)):
        for x_idx in range(min(x_coords), max(x_coords) + 1):
            if (x_idx, y_idx) == (0, 0):
                print("s", end="")
            elif (x_idx, y_idx) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def part2():
    data = get_data(INPUT)
    answer = simulate_movement_9_knots(data)
    print_tail_positions(answer[1])
    return answer[0]


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
