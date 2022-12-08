import itertools

from common import get_input
import pprint

tree_map = get_input(8)


def is_visible_from_edge(already_seen, tree_height, rest_of_slice):
    if not already_seen:
        if len(list(rest_of_slice)) == 0:
            return True
        if all(int(tree) < int(tree_height) for tree in rest_of_slice):
            return True


tree_map = tree_map.split('\n')
seen_map = []
for _ in tree_map:
    seen_map.append([0] * len(tree_map[0]))

for i, row in enumerate(tree_map):
    for j, col in enumerate(row):
        # we've already checked this tree, skip it
        if seen_map[i][j]:
            continue
        # we're on an edge, mark it as seen
        if i in (0, len(tree_map) - 1) or j in (0, len(tree_map[i]) - 1):
            seen_map[i][j] = 1
            continue
        # check east
        if is_visible_from_edge(seen_map[i][j], tree_map[i][j], tree_map[i][j + 1:]):
            seen_map[i][j] = 1
        # south
        if is_visible_from_edge(seen_map[i][j], tree_map[i][j], [r[j] for r in tree_map[i + 1:]]):
            seen_map[i][j] = 1
        # west
        if is_visible_from_edge(seen_map[i][j], tree_map[i][j], list(reversed(tree_map[i][:j]))):
            seen_map[i][j] = 1
        # north
        if is_visible_from_edge(seen_map[i][j], tree_map[i][j], list(reversed([r[j] for r in tree_map[:i]]))):
            seen_map[i][j] = 1

pprint.pprint(seen_map)
print(sum(itertools.chain.from_iterable(seen_map)))





