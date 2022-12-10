from common import get_input, bcolors, get_new_grid
from collections import defaultdict

instructions = get_input(10)

instructions = instructions.split('\n')
cycle = 1
x = [1]
queue = defaultdict(list)

instruction_times = {
    "noop": 1,
    "addx": 2
}

signal_strengths = []

while True:
    if len(instructions) == 0 and len(queue) == 0:
        break

    if len(instructions) != 0 and len(queue) == 0:
        instruction = instructions.pop(0)
        try:
            command, value = instruction.split()
        except ValueError:
            command = instruction
        else:
            queue[cycle+instruction_times[command]-1].append(int(value))

    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strengths.append(cycle * sum(x))
        print(f"Cycle: {cycle}; x={sum(x)}; signal strength={sum(x) * cycle}")

    actions_to_apply = queue[cycle]
    try:
        del queue[cycle]
    except KeyError:
        pass
    if len(actions_to_apply) != 0:
        for v in actions_to_apply:
            x.append(v)

    cycle += 1

print(sum(signal_strengths))
