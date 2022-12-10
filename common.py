import colorama


def get_input(day):
    # this is a gross hack
    if day > 9:
        with open(f'config/day0{day}.txt', 'r') as f:
            return f.read()
    else:
        with open(f'config/day00{day}.txt', 'r') as f:
            return f.read()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_new_grid(width, height=0, default=0):
    if height == 0:
        height = width

    grid = []
    for _ in range(height):
        grid.append([default] * width)
    return grid

def render_grid(grid, colour_dict):
    print("----")
    for row in grid:
        for char in row:
            if char in colour_dict:
                print(colour_dict[char] + str(char) + colorama.Style.RESET_ALL, end='')
            else:
                print(char, end='')
        print('\n', end='')
