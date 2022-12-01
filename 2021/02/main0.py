from os import error
from pathlib import Path

INPUT = "input.txt"

script_location = Path(__file__).absolute().parent
file_location = script_location / INPUT

lines = open(file_location, "r").readlines()
tuple_list = [
    (line.split()[0], line.split()[1]) for line in lines
]  # [(command0, distance0), (command1, distance1), ....]

depth = 0
length = 0
for cmd, dist in tuple_list:
    dist = int(dist)
    match cmd:
        case "forward":
            length += dist
        case "down":
            depth += dist
        case "up":
            depth -= dist
        case _:
            raise error("should not happend")
print(depth, length, depth * length)
