def get_input(day):
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

def get_new_grid(size):
    grid = []
    for _ in range(size):
        grid.append([0] * size)
    return grid
