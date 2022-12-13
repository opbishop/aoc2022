import math
import re
import string
import sys

import colorama

from common import get_input, get_new_grid, render_grid
from collections import defaultdict

puzzle_input = get_input(12)

puzzle_input = puzzle_input.split('\n')
START_CHAR = "S"
END_CHAR = "E"
CHAR_VALUES = {char: string.ascii_lowercase.find(char)+1 for char in string.ascii_lowercase}
CHAR_VALUES[START_CHAR] = 1
CHAR_VALUES[END_CHAR] = 26


def build_grid(puzzle_input):
    grid = get_new_grid(height=len(puzzle_input), width=len(puzzle_input[0]), default='.')
    for i, line in enumerate(puzzle_input):
        grid[i] = list(line)
    return grid


def get_valid_moves_from_cell(grid, position, visited):
    current_char = grid[position[0]][position[1]]
    current_value = CHAR_VALUES.get(current_char, current_char)

    potential_moves = [(position[0] -1, position[1]),(position[0] +1, position[1]),(position[0], position[1] -1),(position[0], position[1] +1)]
    valid_moves = []

    for move in potential_moves:
        if move in visited:
            continue
        if move[0] < 0 or move[0] >= len(grid):
            continue
        if move[1] < 0 or move[1] >= len(grid[0]):
            continue
        next_char = grid[move[0]][move[1]]
        next_value = CHAR_VALUES.get(next_char, next_char)
        if next_value - current_value > 1:
            continue
        valid_moves.append(move)
    return valid_moves


def find_shortest_path(grid, position, visited, shortest_path=sys.maxsize):
    this = grid[position[0]][position[1]]
    visited.add(position)
    if this == END_CHAR:
        shortest_path = min(len(visited), int(shortest_path))
        visited.remove(position)
        print(f"New shortest path is {shortest_path}")
        return shortest_path
    else:
        queue = get_valid_moves_from_cell(grid, position, visited)
        for move in queue:
            shortest_path = find_shortest_path(grid, move, visited, shortest_path)
    visited.remove(position)
    return shortest_path


def find_start(grid):
    position = tuple
    for i, row in enumerate(grid):
        if START_CHAR in row:
            position = i, row.index(START_CHAR)
    return position


grid = build_grid(puzzle_input)
path_length = find_shortest_path(grid, find_start(grid), set())
print(path_length)
