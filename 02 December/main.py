# A = Rock = 1 point
# B = Paper = 2 points
# C = Scissors = 3 points
# X = Rock Response
# Y = Paper Response
# Z = Scissors Response

# Bonus points:
# Loss = 0 points
# Draw = 3 points
# Win = 6 points

OPTIONS = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

SCORES = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Loss": 0,
    "Draw": 3,
    "Win": 6,
}

# Open the input file and read it into an array
with open('input.txt') as f:
    lines: str = f.readlines()

# Remove the newline character from the end of each line
lines = [line.rstrip() for line in lines]

player_score: int = 0

# Loop through the lines
for line in lines:
    # Get the first character of the line
    elf = OPTIONS.get(line[0])
    # Get the last character of the line
    response = OPTIONS.get(line[-1])

    if elf == response:  # Get the draw out of the way first
        result = "Draw"
        print(f"Elf {elf} and response {response} is a {result}")

    elif elf == "Rock":
        if response == "Paper":
            result = "Win"
            print(f"Elf {elf} and response {response} is a {result}")
        else:
            result = "Loss"
            print(f"Elf {elf} and response {response} is a {result}")
    elif elf == "Paper":
        if response == "Scissors":
            result = "Win"
            print(f"Elf {elf} and response {response} is a {result}")
        else:
            result = "Loss"
            print(f"Elf {elf} and response {response} is a {result}")
    elif elf == "Scissors":
        if response == "Rock":
            result = "Win"
            print(f"Elf {elf} and response {response} is a {result}")
        else:
            result = "Loss"
            print(f"Elf {elf} and response {response} is a {result}")

    player_score += SCORES.get(result) + SCORES.get(response)  # Match the result of the game to the scores dictionary
    round_score = SCORES.get(result) + SCORES.get(response)  # Just used for printing. Not needed for the actual score.

    print(f"You {result}! You get {round_score} points.")


print(f"Player score: {player_score}")

# Part 2
# Determine the outcome
# X = The player should lose
# Y = The player should draw
# Z = The player should win

# Round 2 - FIGHT!
round_two = 0

PREDETERMINED_OUTCOMES = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}

# Loop through the lines
for line in lines:
    elf = OPTIONS.get(line[0])
    outcome = PREDETERMINED_OUTCOMES.get(line[-1])

    if outcome == "Draw":
        response = elf
    elif outcome == "Loss":
        if elf == "Rock":
            response = "Scissors"
        elif elf == "Paper":
            response = "Rock"
        elif elf == "Scissors":
            response = "Paper"
    elif outcome == "Win":
        if elf == "Rock":
            response = "Paper"
        elif elf == "Paper":
            response = "Scissors"
        elif elf == "Scissors":
            response = "Rock"

    round_two += SCORES.get(outcome) + SCORES.get(response)
    current_round_score = SCORES.get(outcome) + SCORES.get(response)  # Just used for printing. Not needed for the actual score.

    print(f"Round 2 score: {round_two}")

