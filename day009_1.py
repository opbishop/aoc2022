import itertools

from common import get_input
import pprint

instructions = get_input(9)

def get_scenic_score(tree_height, rest_of_slice):
    s = 0
    for tree in rest_of_slice:
        if int(tree) < int(tree_height):
            s += 1
        else:
            s += 1
            break
    return s


def move_up(head_pos, tail_pos, seen_map):
    MOVE_TAIL = head_pos[0] < tail_pos[0]
    head_pos = (head_pos[0] -1, head_pos[1])
    if MOVE_TAIL:
        tail_pos = head_pos[0] +1, head_pos[1]

    return head_pos, tail_pos, seen_map

def move_down(head_pos, tail_pos, seen_map):
    MOVE_TAIL = head_pos[0] > tail_pos[0]
    head_pos = (head_pos[0] + 1, head_pos[1])
    if MOVE_TAIL:
        tail_pos = head_pos[0] - 1, head_pos[1]

    return head_pos, tail_pos, seen_map

def move_right(head_pos, tail_pos, seen_map):
    MOVE_TAIL = head_pos[1] > tail_pos[1]
    head_pos = (head_pos[0], head_pos[1] + 1)
    if MOVE_TAIL:
        tail_pos = head_pos[0], head_pos[1] -1

    return head_pos, tail_pos, seen_map

def move_left(head_pos, tail_pos, seen_map):
    MOVE_TAIL = head_pos[1] < tail_pos[1]
    head_pos = (head_pos[0], head_pos[1] -1)
    if MOVE_TAIL:
        tail_pos = head_pos[0], head_pos[1] +1

    return head_pos, tail_pos, seen_map

SIZE = 6

# seen_map = []
# for _ in range(SIZE):
#     seen_map.append([0] * SIZE)
# seen_map[len(seen_map) -1][0] = "s"

tail_pos = (100, 0)
head_pos = (100, 0)
start_pos = (100, 0)

tail_positions = {tail_pos}

move_funcs = {
    'U': move_up,
    'R': move_right,
    'D': move_down,
    'L': move_left
}
for instruction in instructions.split('\n'):
    direction, num = instruction.split()[0], int(instruction.split()[1])
    print(instruction)
    for _ in range(num):
        head_pos, tail_pos, seen_map = move_funcs[direction](head_pos, tail_pos, None)
        # seen_map[tail_pos[0]][tail_pos[1]] = '#'
        tail_positions.add(tail_pos)
        print(tail_pos)

        # seen_map[head_pos[0]][head_pos[1]] = "H"
        # seen_map[tail_pos[0]][tail_pos[1]] = "T"


# print(max(itertools.chain.from_iterable(seen_map)))
print(len(tail_positions))





