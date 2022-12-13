import math
import re
import string
import sys

import colorama

from common import get_input, get_new_grid, render_grid
from collections import defaultdict

puzzle_input = get_input(13)
# puzzle_input = """[1,1,3,1,1]
# [1,1,5,1,1]
#
# [[1],[2,3,4]]
# [[1],4]
#
# [9]
# [[8,7,6]]
#
# [[4,4],4,4]
# [[4,4],4,4,4]
#
# [7,7,7,7]
# [7,7,7]
#
# []
# [3]
#
# [[[]]]
# [[]]
#
# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""
puzzle_input = puzzle_input.split('\n\n')


def compare(left, right, top=False):
    if type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == int:
        if left < right:
            return True
        elif right < left:
            return False
    elif type(left) == list and type(right) == list:
        if len(left) == 0 and len(right) != 0:
            return True
        elif len(right) == 0 and len(left) != 0:
            return False

        for pair in zip(left, right):
            result = compare(pair[0], pair[1])
            if result is None:
                if len(right) < len(left):
                    return False
                elif len(right) > len(left):
                    return True
            else:
                return result


total = []
for i, line_pair in enumerate(puzzle_input, 1):
    left, right = line_pair.split('\n')
    left = eval(left)
    right = eval(right)
    if compare(left, right, True):
        total.append(i)
print(sum(total))
