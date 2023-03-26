import random


def play():
    user = input("what is your choice 'r' for rock,'p' for paper,'s' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if computer == user:
        return 'it is a tie'

    if isWin(user, computer):
        return 'You Won'

    return 'You Lost'

def isWin(player, opponent):
    if((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')):
        return True

print(play())