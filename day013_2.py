import math
import re
import string
import sys

import colorama

from common import get_input, get_new_grid, render_grid
from collections import defaultdict

from day013_1 import compare

puzzle_input = get_input(13)
puzzle_input = puzzle_input.split('\n\n')


total_sorted = []
puzzle_input = [x.split('\n') for x in puzzle_input]
puzzle_input = [eval(item) for sublist in puzzle_input for item in sublist]
divider_packets = [[[2]], [[6]]]
puzzle_input.extend(divider_packets)

sorted_arr = [puzzle_input[0]]
puzzle_input = puzzle_input[1:]
for i in range(len(puzzle_input)):
    inserted = False
    for j in range(len(sorted_arr)):
        left = puzzle_input[i]
        right = sorted_arr[j]
        if compare(left, right):
            inserted = True
            sorted_arr.insert(j, left)
            break
    if not inserted:
        sorted_arr.append(puzzle_input[i])

indices = [sorted_arr.index(packet) +1 for packet in divider_packets]
print(math.prod(indices))