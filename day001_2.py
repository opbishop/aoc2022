from collections import defaultdict

with open('config/day001.txt', 'r') as f:
    input = f.read()

elf_calories = defaultdict(set)
elf_num = 1
running_sum = 0

for line in input.split('\n'):
    if line == "":
        elf_calories[running_sum].add(elf_num)
        elf_num += 1
        running_sum = 0
    else:
        running_sum += int(line)


def get_highest_cals(elf_dict: dict, n=1):
    sorted_calories = sorted(list(elf_dict.keys()), reverse=True)
    i = 0
    to_return = dict()

    while len(to_return) < n:
        highest_cals = sorted_calories[i]
        matching_elves: set = elf_dict[highest_cals]
        if all(elf in to_return for elf in matching_elves):
            i += 1
        else:
            for elf in matching_elves:
                if elf not in to_return:
                    to_return[elf] = highest_cals
                    break
    return to_return

elves_with_highest = get_highest_cals(elf_calories, 5)
print(sum(elves_with_highest.values()))