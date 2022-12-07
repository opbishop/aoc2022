import string

from common import get_input

content = get_input(4)
count = 0


def fully_contains(first, second):
    first_start, first_end = first.split('-')
    second_start, second_end = second.split('-')

    first_range = range(int(first_start), int(first_end)+1)
    second_range = range(int(second_start), int(second_end)+1)

    return len(set(first_range).intersection(set(second_range))) != 0


for line in content.split('\n'):
    first = line.split(',')[0]
    second = line.split(',')[1]
    if fully_contains(first,second):
        count += 1
    elif fully_contains(second, first):
        count += 1

print(count)