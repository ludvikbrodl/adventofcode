from os import error
from pathlib import Path
import numpy as np
from numpy.lib.shape_base import row_stack

INPUT = "input.txt"

script_location = Path(__file__).absolute().parent
file_location = script_location / INPUT

lines = open(file_location, "r").readlines()
binary_list = [
    list((line.strip())) for line in lines
]  # [[a0, a1, a2, a3, ...], [b0, b1, b2, ..], ...]

data = np.array(binary_list).astype(np.integer)


def get_most_common_bits(data):
    digit_count = len(data[0])
    row_count = len(data)
    d = np.array(data).astype(np.integer)
    ones_count = d.sum(axis=0)
    zeros_count = [row_count] * digit_count - ones_count

    overwheling_zeroes = [0 if count > row_count / 2 else 1 for count in zeros_count]
    overwheling_ones = [0 if count > row_count / 2 else 1 for count in ones_count]
    equal = [1 if count == row_count / 2 else 0 for count in ones_count]
    return overwheling_zeroes, overwheling_ones, equal


def bits_to_int(bit_array):
    reversed = bit_array.copy()
    reversed.reverse()
    nbr = 0
    for idx, bit in enumerate(reversed):
        nbr += 0 if bit == 0 else 2 ** idx
    return nbr


# epsilon = most common bit in position = oxygen generator rating
# gamma = least common bit in position = CO2 scrubber rating


def filter_rating(data, most_or_least_common):  # 0 = least_common, 1 = most_common
    current_data = data.copy()
    width = len(current_data)
    for idx in range(width):
        zeroes, ones, equals = get_most_common_bits(current_data)
        if equals[idx] == 1:
            most_common_bit = most_or_least_common
        elif most_or_least_common == 1:
            most_common_bit = zeroes[idx]
        elif most_or_least_common == 0:
            most_common_bit = ones[idx]
        # most_common_bit = 0 if get_most_common_bits(current_data)[most_or_least_common][idx] else 1
        next_data = []
        for row in current_data:
            if row[idx] == most_common_bit:
                next_data.append(row)
        current_data = next_data
        if len(current_data) == 1:
            break
    return current_data[0]


oxygen = filter_rating(data, 1)
co2 = filter_rating(data, 0)
print(oxygen, co2)
oxygen_decimal = bits_to_int(list(oxygen))
co2_decimal = bits_to_int(list(co2))
print(oxygen_decimal, co2_decimal, oxygen_decimal * co2_decimal)
