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


def get_valid_moves_from_cell(grid, position):
    current_char = grid[position[0]][position[1]]
    current_value = CHAR_VALUES.get(current_char, current_char)

    potential_moves = [(position[0] -1, position[1]),(position[0] +1, position[1]),(position[0], position[1] -1),(position[0], position[1] +1)]
    valid_moves = []

    for move in potential_moves:
        if move[0] < 0 or move[0] >= len(grid):
            continue
        if move[1] < 0 or move[1] >= len(grid[0]):
            continue
        next_char = grid[move[0]][move[1]]
        next_value = CHAR_VALUES.get(next_char, next_char)
        if next_value - current_value < -1:
            continue
        valid_moves.append(move)
    return valid_moves


def dijkstra_algorithm(grid, position):
    unvisited_nodes = set([(row, col) for row in range(len(grid)) for col in range(len(grid[0]))])

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[position] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = get_valid_moves_from_cell(grid, current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + 1
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def find_start(grid):
    position = tuple
    for i, row in enumerate(grid):
        if START_CHAR in row:
            position = i, row.index(START_CHAR)
    return position


def find_end(grid):
    position = tuple
    for i, row in enumerate(grid):
        if END_CHAR in row:
            position = i, row.index(END_CHAR)
    return position


def all_a(grid):
    return set([(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 'a'])

a_paths = []
grid = build_grid(puzzle_input)
start_position = find_start(grid)
end_position = find_end(grid)
previous_nodes, shortest_path = dijkstra_algorithm(grid, end_position)
for a in all_a(grid):
    a_paths.append(shortest_path[a])
print(min(a_paths))

