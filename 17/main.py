from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> tuple[tuple[int]]:  # ((x_start, x_end), (y_start, y_end))
    line = get_lines(path)[0]
    coords = line.split(": ")[1].split(", ")
    x, y = tuple(coords)
    x = x.split("=")[1].split("..")
    x = tuple([int(x[0]), int(x[1])])
    y = y.split("=")[1].split("..")
    y = tuple([int(y[1]), int(y[0])])
    return x, y


def check_x(velocity, start, end):
    x = 0
    while True:
        x += velocity
        if velocity > 0:
            velocity -= 1
        elif velocity < 0:
            velocity += 1
        else:
            velocity = 0
        if start <= x <= end:
            return x
        elif velocity == 0 or x > end:
            return False


def get_lowest_x_vel(start, end):
    for idx in range(end):
        will_hit = check_x(idx, start, end)
        if will_hit:
            return idx


def get_highest_x_vel(start, end):
    return end


def check_y(velocity, start, end):
    y = 0
    while True:
        y += velocity
        velocity -= 1
        if start <= y <= end:
            return y
        elif velocity == 0 or y < end:
            return False


def sim_xy(x_velocity, y_velocity, x, y):
    y_cord = 0
    x_cord = 0
    while True:
        if x_velocity == 6 and y_velocity == 9:
            pass
        x_start, x_end = x
        y_start, y_end = y
        y_cord += y_velocity
        y_velocity -= 1
        x_cord += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        else:
            x_velocity = 0
        if x_cord > x_end and y_cord < y_end:
            return "xy_overshoot"
        elif x_cord > x_end:
            return "x_overshoot"
        elif y_cord < y_end:
            return "y_overshoot"
        elif (y_start >= y_cord >= y_end) and (x_start <= x_cord <= x_end):
            return "hit"


def get_highest_y_vel(x_velocity, y_lower, x, y):
    y_velocity = y_lower
    highest_found = y_velocity
    for _ in range(5000):
        result = sim_xy(x_velocity, y_velocity, x, y)
        if result == "hit":
            highest_found = y_velocity
        y_velocity += 1
    return highest_found  # highest possible


def get_lowest_y_vel(start, end):
    return end


def calc(x, y):
    x_start, x_end = x
    y_start, y_end = y
    max_y_vel = abs(y_end)
    return sum(range(max_y_vel))


def part1_example():
    x, y = get_data(INPUT_EXAMPLE)
    answer = calc(x, y)
    assert answer == 45

    return answer


def part1():
    x, y = get_data(INPUT)
    answer = calc(x, y)

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
