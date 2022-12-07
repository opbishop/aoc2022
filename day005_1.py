import string

from common import get_input

instructions = get_input(5)
stacks = [
    "BSVZGPW",
    "JVBCZF",
    "VLMHNZDC",
    "LDMZPFJB",
    "VFCGJBQR",
    "GFQTSLB",
    "LGCZV",
    "NLG",
    "JPHC"
]
stacks = [list(s) for s in stacks]

def move_stacked_crates(count, f, t):
    for i in range(count):
        crate = stacks[f].pop()
        stacks[t].append(crate)


for instruction in instructions.split('\n'):
    words = instruction.split(' ')
    num = int(words[1])
    from_stack = int(words[3]) -1
    to_stack = int(words[-1]) -1
    move_stacked_crates(num, from_stack, to_stack)

final = ''.join([stack[-1] for stack in stacks])
print(final)