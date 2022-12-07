import string

from common import get_input

content = get_input(3)

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
priorities = 0
for rucksack in content.split('\n'):
    midpoint = int(len(rucksack) / 2)
    first = rucksack[:midpoint]
    second = rucksack[midpoint:]

    char_in_both = set(first).intersection(set(second)).pop()

    if str.islower(char_in_both):
        priority = lowercase.find(char_in_both) + 1
    else:
        priority = uppercase.find(char_in_both) + 27

    priorities += priority
print(priorities)