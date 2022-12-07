import string
from collections import defaultdict

from common import get_input

output = get_input(7)
INPUT_CHAR = "$"

current_path = []
filesizes = defaultdict(int)
def build_tree(output, filesizes):
    for line in output.split('\n'):
        if str.startswith(line, INPUT_CHAR):
            split_command = line.split(' ')
            if split_command[1] == "cd" and split_command[2] != "..":
                current_path.append(split_command[2])
            elif split_command[1] == "cd" and split_command[2] == "..":
                current_dir_sum = filesizes['/'.join(current_path)[1:]]
                current_path.pop()
                filesizes['/'.join(current_path)[1:]] += current_dir_sum

        if str.isnumeric(line[0]):
            split_output = line.split(' ')
            filesizes['/'.join(current_path)[1:]] += int(split_output[0])

build_tree(output, filesizes)

total = 0
for dir, size in filesizes.items():
    if size <= 100000:
        total += size
print(total)