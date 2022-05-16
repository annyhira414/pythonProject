import random


def play_game():
    user = input("what is your choice 'r' for rock , 'p' for paper, 's' for scissors ??? - ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("tiy game ")

    if who_winner(user, computer):
        return "you win"

    return "you lost"
    # p > r,  r > s, s > p


def who_winner(player, opponent, ):
    if (player == 'p' and opponent == 'r') or (
            player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
        return True


print(play_game())
