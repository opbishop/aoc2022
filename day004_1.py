import string

from common import get_input

content = get_input(4)
count = 0


def fully_contains(first, second):
    first_start, first_end = first.split('-')
    second_start, second_end = second.split('-')

    return int(first_start) <= int(second_start) and int(first_end) >= int(second_end)


for line in content.split('\n'):
    first = line.split(',')[0]
    second = line.split(',')[1]
    if fully_contains(first,second):
        count += 1
    elif fully_contains(second, first):
        count += 1

print(count)