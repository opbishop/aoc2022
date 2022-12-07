import string
from collections import defaultdict
import re

from common import get_input

# output = get_input(7)
output = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
INPUT_CHAR = "$"

class node:
    def __init__(self, name, parent_node, size=0):
        self.name = name
        self.size = int(size)
        self.parent = parent_node
        self.contents = []

    def get_size(self):
        if len(self.contents) == 0:
            return self.size

        return sum(node.get_size() for node in self.contents)


def build_tree(output):
    root_node = None
    current_node = None
    for line in output.split('\n'):
        if str.startswith(line, INPUT_CHAR):
            split_command = line.split(' ')
            if split_command[1] == "cd" and split_command[2] != "..":
                if current_node == None:
                    o = node(name=split_command[2], parent_node=None)
                    root_node = o
                    current_node = o
                else:
                    o = node(name=split_command[2], parent_node=current_node)
                    current_node.contents.append(o)
                    current_node = o
            if split_command[1] == "cd" and split_command[2] == "..":
                current_node = current_node.parent

        if line[0].isnumeric():
            o = node(name=line.split()[1], parent_node=current_node, size=line.split()[0])
            current_node.contents.append(o)

    return root_node


root = build_tree(output)
print(root.get_size())

