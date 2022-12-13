import math
import re

import colorama

from common import get_input, get_new_grid, render_grid
from collections import defaultdict

puzzle_input = get_input(11)


class monkey():
    num_items_inspected = 0
    def __init__(self, monkey_id, items, operation, test, if_true, if_false):
        self.id = monkey_id
        self.items = [int(item) for item in items]
        self.operation = operation
        self.test_num = int(test)
        self.if_true = int(if_true)
        self.if_false = int(if_false)

    def inspect_all_items(self):
        inspected_items = []
        for item in self.items:
            inspected_items.append(self.inspect(item))
        self.items = inspected_items
        return inspected_items

    def test_and_throw_all_items(self):
        thrown_items = defaultdict(list)
        for item in self.items:
            thrown_items[self.test(item)].append(item)
        self.items = []
        return thrown_items

    def inspect(self, old: int):
        new = self.operation(old)
        self.num_items_inspected += 1
        return math.floor(int(new) / 3)

    def test(self, item):
        if item % self.test_num == 0:
            return self.if_true
        else:
            return self.if_false


def parse_input(puzzle_input: str):
    monkeys = []
    for line in puzzle_input.split('\n'):
        if line.startswith("Monkey"):
            continue
        if line == '':
            monkeys.append(
                monkey(monkey_id=len(monkeys),
                       items=starting_items,
                       operation=operation,
                       test=test_num,
                       if_true=if_true,
                       if_false=if_false
                       )
            )
            continue
        line = line.strip()
        if line.startswith("Starting items:"):
            starting_items = list(re.findall('\d+', line))
        elif line.startswith("Operation: "):
            operation = line.split('new = ')[1]
            operation = eval("lambda old: " + operation)
            print(operation(1))
        elif line.startswith('Test: '):
            test_num = line.rsplit(' ', 1)[1]
        elif "true" in line:
            if_true = line[-1]
        else:
            if_false = line[-1]

    return monkeys

def print_monkey_contents(monkeys):
    for monkey in monkeys:
        print(f"Monkey {monkey.id}: {monkey.items}")


total_rounds = 20
monkeys = parse_input(puzzle_input)
for round in range(total_rounds):
    for monkey in monkeys:
        monkey.inspect_all_items()
        thrown_items = monkey.test_and_throw_all_items()
        for monkey_num, items_caught in thrown_items.items():
            print(f"Throwing to {monkey_num}")
            monkeys[monkey_num].items.extend(items_caught)

    print_monkey_contents(monkeys)

items_inspected = [monkey.num_items_inspected for monkey in monkeys]
print((sorted(items_inspected, reverse=True)[:2][0]) * (sorted(items_inspected, reverse=True)[:2][1]))