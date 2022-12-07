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
    "C": "scissors"
}

expected_results = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}


def determine_action(opponent_action, expected_result):
    if expected_result == "draw":
        return opponent_action

    if opponent_action == "rock" and expected_result == "win":
        return "paper"
    elif opponent_action == "rock" and expected_result == "loss":
        return "scissors"
    elif opponent_action == "paper" and expected_result == "win":
        return "scissors"
    elif opponent_action == "paper" and expected_result == "loss":
        return "rock"
    elif opponent_action == "scissors" and expected_result == "win":
        return "rock"
    elif opponent_action == "scissors" and expected_result == "loss":
        return "paper"


total_score = 0
for round in strats:
    result = None
    opp_action = actions[round[0]]
    my_action = determine_action(opp_action, expected_results[round[1]])

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