import colorama

from common import get_input, get_new_grid, render_grid

# instructions = get_input(9)
instructions = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def move_head(direction, positions):
    curr = positions[0]
    if direction == 'U':
        positions[0] = curr[0] - 1, curr[1]
    elif direction == 'R':
        positions[0] = curr[0], curr[1] + 1
    elif direction == 'D':
        positions[0] = curr[0] + 1, curr[1]
    elif direction == 'L':
        positions[0] = curr[0], curr[1] - 1
    return positions


def follow(positions, curr):
    if curr > len(positions) - 1:
        return
    next = positions[curr - 1]
    this = positions[curr]
    dx, dy = next[1] - this[1], next[0] - this[0]

    # check if we need to move at all
    if this == next:
        return
    # next node is only 1 space from this
    if sum([abs(dx), abs(dy)]) == 1:
        return
    # next node is diagonally 1 away from this
    if ((dx ** 2) + (dy ** 2)) == ((1 ** 2) + (1 ** 2)):
        return

    if dx != 0 and dy == 0:
        # move horizontally
        positions[curr] = this[0], this[1] + (1 if dx > 0 else -1)
    elif dy != 0 and dx == 0:
        # move vertically
        positions[curr] = this[0] + (1 if dy > 0 else -1), this[1]
    else:
        # move diagonally
        positions[curr] = this[0] + (1 if dy > 0 else -1), this[1] + (1 if dx > 0 else -1)

    follow(positions, curr + 1)


HEIGHT = 18
WIDTH = 24
start = 12, 12
positions = [start] * 10
tail_positions = {positions[-1]}

DEFAULT_CHAR = '.'
colours = {
    '.': colorama.Fore.BLUE,
    '#': colorama.Fore.LIGHTYELLOW_EX,
    'H': colorama.Fore.LIGHTRED_EX
}
for i in range(10):
    colours[i] = colorama.Fore.LIGHTYELLOW_EX


def draw_grid(snake_positions, snake_tail_visited_positions):
    grid = get_new_grid(width=WIDTH, height=HEIGHT, default=DEFAULT_CHAR)
    for tail_position in snake_tail_visited_positions:
        grid[tail_position[0]][tail_position[1]] = '#'
    for node in range(len(snake_positions)):
        x, y = snake_positions[node]
        grid[x][y] = node if node != 0 else 'H'
    render_grid(grid, colours)


for instruction in instructions.split('\n'):
    direction, num = instruction.split()[0], int(instruction.split()[1])
    for _ in range(num):
        positions = move_head(direction, positions)
        follow(positions, 1)
        tail_positions.add(positions[-1])
draw_grid(positions, tail_positions)
print(len(tail_positions))
