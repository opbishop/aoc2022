from common import get_input

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
        positions[0] = curr[0] -1, curr[1]
    elif direction == 'R':
        positions[0] = curr[0], curr[1] + 1
    elif direction == 'D':
        positions[0] = curr[0] + 1, curr[1]
    elif direction == 'L':
        positions[0] = curr[0], curr[1] - 1
    return positions


def follow(positions, curr):
    if curr > len(positions) -1:
        return
    next = positions[curr -1]
    this = positions[curr]
    dx, dy = next[1] - this[1], next[0] - this[0]

    # check if we need to move at all
    if this == next:
        return
    if sum([abs(dx), abs(dy)]) == 1:
        return
    if ((dx**2) + (dy**2)) == ((1**2) + (1**2)):
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

    follow(positions, curr +1)

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

SIZE = 26
def get_new_map():
    seen_map = []
    for _ in range(SIZE+1):
        seen_map.append([f'{bcolors.OKGREEN}0'] * (SIZE+1))
    return seen_map

start = 12, 12
positions = [start]*10
tail_positions = {positions[-1]}


def draw_map(positions, tail_positions):
    seen_map = get_new_map()
    seen_map[start[0]][1] = "s"
    print("----")
    for tail_position in tail_positions:
        seen_map[tail_position[0]][tail_position[1]] = f"{bcolors.WARNING}#{bcolors.OKGREEN}"
    for node in range(len(positions)):
        x, y = positions[node]
        seen_map[x][y] = node if node != 0 else 'H'
    for l in seen_map:
        print(''.join([str(s) for s in l]))

seen_map = get_new_map()
for instruction in instructions.split('\n'):
    direction, num = instruction.split()[0], int(instruction.split()[1])
    for _ in range(num):
        positions, seen_map = move_head(direction, positions)
        follow(positions, 1)
        tail_positions.add(positions[-1])
draw_map(positions,tail_positions)
print(len(tail_positions))





