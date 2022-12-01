from pathlib import Path

INPUT = "input.txt"

script_location = Path(__file__).absolute().parent
file_location = script_location / INPUT

data = [int(l) for l in open(file_location, "r").readlines()]
count = 0
for i, value in enumerate(data):
    if i == 0:
        continue
    if value > data[i - 1]:
        count += 1

print(count)
