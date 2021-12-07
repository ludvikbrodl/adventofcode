from os import error
from pathlib import Path
import numpy as np
from numpy.lib.shape_base import row_stack 

INPUT = "input.txt"

script_location = Path(__file__).absolute().parent
file_location = script_location / INPUT

lines = open(file_location, "r").readlines()
binary_list = [list((line.strip())) for line in lines] #[[a0, a1, a2, a3, ...], [b0, b1, b2, ..], ...]

arr = np.array(binary_list).astype(np.integer)
digit_count = len(binary_list[0])
row_count = len(binary_list)
ones_count = arr.sum(axis=0)
zeros_count = [row_count] * digit_count  - ones_count
print(ones_count, zeros_count)

gamma = [0 if count > row_count  / 2  else 1 for count in zeros_count]
epsilon = [0 if count > row_count  / 2  else 1 for count in ones_count]
print(gamma, epsilon)

gamma_decimal = 0
epsilon_decimal = 0
gamma.reverse() #bits are counted from the right
for idx, bit in enumerate(gamma):
    gamma_decimal += 0 if bit == 0 else 2 ** idx
    epsilon_decimal += 0 if bit == 1 else 2 ** idx

print(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal)