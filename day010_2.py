import colorama

from common import get_input, get_new_grid, render_grid
from collections import defaultdict

instructions = get_input(10)
instructions = instructions.split('\n')

cycle = 1
x = [1]
queue = defaultdict(list)

instruction_times = {
    "noop": 1,
    "addx": 2
}

signal_strengths = []

# set up the crt screen
GRID_WIDTH = 40
GRID_HEIGHT = 6
crt = get_new_grid(GRID_WIDTH, GRID_HEIGHT, '?')
colours = {
    '.': colorama.Fore.LIGHTBLUE_EX,
    '#': colorama.Fore.LIGHTYELLOW_EX
}

pixel_x = 0
pixel_y = 0


def sprite_is_visible(x, pixel_x):
    # sprite is visible if the x register is 1 behind or in front of the pixel, or exactly on top of it
    return abs(x - pixel_x) in (0, 1)


def update_sprite(crt, pixel_x, pixel_y, x):
    if sprite_is_visible(x, pixel_x):
        crt[pixel_y][pixel_x] = '#'
    else:
        crt[pixel_y][pixel_x] = '.'
    pixel_x += 1
    # pixel has gone off the screen, reset it on the next row
    if pixel_x == GRID_WIDTH:
        pixel_x = 0
        pixel_y += 1
    render_grid(crt, colours)
    return crt, pixel_x, pixel_y


while True:
    if len(instructions) == 0 and len(queue) == 0:
        break

    if len(instructions) != 0 and len(queue) == 0:
        instruction = instructions.pop(0)
        try:
            command, value = instruction.split()
        except ValueError:
            command = instruction
        else:
            queue[cycle + instruction_times[command] - 1].append(int(value))

    crt, pixel_x, pixel_y = update_sprite(crt, pixel_x, pixel_y, sum(x))

    actions_to_apply = queue[cycle]
    try:
        del queue[cycle]
    except KeyError:
        pass
    if len(actions_to_apply) != 0:
        for v in actions_to_apply:
            x.append(v)

    cycle += 1
