import itertools

from common import get_input
import pprint

tree_map = get_input(8)


def get_scenic_score(tree_height, rest_of_slice):
    s = 0
    for tree in rest_of_slice:
        if int(tree) < int(tree_height):
            s += 1
        else:
            s += 1
            break
    return s


tree_map = tree_map.split('\n')
seen_map = []
for _ in tree_map:
    seen_map.append([0] * len(tree_map[0]))

for i, row in enumerate(tree_map):
    for j, col in enumerate(row):
        east = get_scenic_score(tree_map[i][j], tree_map[i][j + 1:])
        south = get_scenic_score(tree_map[i][j], [r[j] for r in tree_map[i + 1:]])
        west = get_scenic_score(tree_map[i][j], list(reversed(tree_map[i][:j])))
        north = get_scenic_score(tree_map[i][j], list(reversed([r[j] for r in tree_map[:i]])))
        seen_map[i][j] = (east * south * west * north)

pprint.pprint(seen_map)
print(max(itertools.chain.from_iterable(seen_map)))





