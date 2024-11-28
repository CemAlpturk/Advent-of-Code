# Part 1

def compute_score(opponent: str, me: str) -> int:
    # compute winner
    win = None
    if opponent == 'A':  # rock
        if me == 'X':  # rock
            win = None
            score = 1
        elif me == 'Y':  # paper
            win = True
            score = 2
        else:
            win = False  # scissors
            score = 3
    elif opponent == 'B':  # paper
        if me == 'X':  # rock
            win = False
            score = 1
        elif me == 'Y':  # paper
            win = None
            score = 2
        else:  # scissors
            win = True
            score = 3
    else:  # scissors
        if me == 'X':  # rock
            win = True
            score = 1
        elif me == 'Y':  # paper
            win = False
            score = 2
        else:  # scissors
            win = None
            score = 3

    if win:
        score += 6
    elif win is None:
        score += 3

    return score


def compute_move(opponent_move: str, outcome: str) -> str:
    move = None
    if opponent_move == 'A':  # rock
        if outcome == 'X':  # lose
            move = 'Z'  # scissors
        elif outcome == 'Y':  # draw
            move = 'X'  # rock
        else:  # win
            move = 'Y'  # paper

    elif opponent_move == 'B':  # paper
        if outcome == 'X':  # lose
            move = 'X'  # rock
        elif outcome == 'Y':  # draw
            move = 'Y'  # paper
        else:  # win
            move = 'Z'  # scissors

    else:  # scissors
        if outcome == 'X':  # lose
            move = 'Y'  # paper
        elif outcome == 'Y':  # draw
            move = 'Z'  # scissors
        else:  # win
            move = 'X'  # rock

    return move


file = 'inputs/day-2.txt'

with open(file) as f:
    lines = f.readlines()

# Process input
opponent_moves = []
my_moves = []
for line in lines:
    vals = line.split('\n')[0].split()
    opponent_moves.append(vals[0])
    my_moves.append(vals[1])

# Total scores
total_score = 0
for i in range(len(my_moves)):
    total_score += compute_score(opponent_moves[i], my_moves[i])

print(total_score)

# Part 2
new_score = 0
for i in range(len(my_moves)):
    move = compute_move(opponent_moves[i], my_moves[i])
    new_score += compute_score(opponent_moves[i], move)

print(new_score)
