with open('config/day002.txt', 'r') as f:
    input = f.read()

strats = list()
for line in input.split('\n'):
    strats.append(tuple(line.split(' ')))

scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "win": 6,
    "draw": 3,
    "loss": 0
}

actions = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

total_score = 0
for round in strats:
    result = None
    opp_action = actions[round[0]]
    my_action = actions[round[1]]

    if opp_action == my_action:
        result = "draw"
    elif opp_action == "rock" and my_action == "paper":
        result = "win"
    elif opp_action == "rock" and my_action == "scissors":
        result = "loss"
    elif opp_action == "paper" and my_action == "scissors":
        result = "win"
    elif opp_action == "paper" and my_action == "rock":
        result = "loss"
    elif opp_action == "scissors" and my_action == "rock":
        result = "win"
    elif opp_action == "scissors" and my_action == "paper":
        result = "loss"

    total_score += scores[my_action]
    total_score += scores[result]

print(total_score)