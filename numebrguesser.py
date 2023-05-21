import random


def rolldice(dmin, dmax):
    return random.randint(dmin, dmax)


SCOREBOARD = {"first_score": 0, "second_score": 0}
CORRECT = {"p1": 0, "p2": 0}

ROUNDS = 1
PLAYER_ONE = 0
PLAYER_TWO = 0

while ROUNDS <= 25:
    number_1 = rolldice(1, 6)
    number_2 = rolldice(1, 6)
    total = number_1 + number_2
    print(f"### Round {ROUNDS} ###")

    while True:
        try:
            PLAYER_ONE = int(input("Player 1 guess: "))
            assert 1 < PLAYER_ONE < 13
        except AssertionError:
            print("Guess must be between 2 and 12. Try again.")
            continue
        else:
            break

    while True:
        try:
            PLAYER_TWO = int(input("Player 2 guess: "))
            assert 1 < PLAYER_TWO < 13
        except AssertionError:
            print("Guess must be between 2 and 12. Try again")
            continue
        else:
            break

    print(f"Round {ROUNDS} Dice Shows: {total}")

    if PLAYER_ONE == PLAYER_TWO:
        print(f"Round {ROUNDS} is a tie so nobody wins.")

    if PLAYER_ONE == total:
        SCOREBOARD["first_score"] += 10
        CORRECT["p1"] += 1
        print(f"Player 1 wins round {ROUNDS}")

    if PLAYER_TWO == total:
        SCOREBOARD["second_score"] += 10
        CORRECT["p2"] += 1
        print(f"Player 2 wins round {ROUNDS}")

    if total not in (PLAYER_ONE, PLAYER_TWO):
        print(f"No winner for round {ROUNDS}")

    if SCOREBOARD["first_score"] >= 100 or SCOREBOARD["second_score"] >= 100:
        break
    ROUNDS += 1

print(f"Total Number of Rounds Played: {ROUNDS}")
print(f'Player 1 Correct Guesses Total: {CORRECT["p1"]}')
print(f'Player 2 Correct Guesses Total: {CORRECT["p2"]}')
print(f'Player 1 score: {SCOREBOARD["first_score"]}')
print(f'Player 2 score: {SCOREBOARD["second_score"]}')


if SCOREBOARD["first_score"] >= 100 and SCOREBOARD["second_score"] >= 100:
    print("The game is a tie. Nobody wins.")
if SCOREBOARD["first_score"] >= 100:
    print("The WINNER of the game is: Player 1!")
if SCOREBOARD["second_score"] >= 100:
    print("The WINNER of the game is: Player 2!")
