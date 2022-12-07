import string

from common import get_input

content = get_input(3)

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
priorities = 0

group = []
def process_rucksacks(group):

    char_in_all = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()

    if str.islower(char_in_all):
        priority = lowercase.find(char_in_all) + 1
    else:
        priority = uppercase.find(char_in_all) + 27

    return priority

for rucksack in content.split('\n'):
    if len(group) == 3:
        priorities += (process_rucksacks(group))
        group = []
        group.append(rucksack)
    else:
        group.append(rucksack)

priorities += (process_rucksacks(group))
print(priorities)