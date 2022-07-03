import random

# r > s, p > r, s > p --> condition

def play(handUser):
    hand = ["r", "s", "p"]
    handComp = random.choice(hand)

    if handUser in hand:
        if handUser == handComp:
            return(f"You: {sub(handUser)} \nComputer: {sub(handComp)} \n It was a TIE!!")
        if condition(handUser, handComp):
            return(f"You: {sub(handUser)} \nComputer: {sub(handComp)} \n You WIN!!!")
        return(f"You: {sub(handUser)} \nComputer: {sub(handComp)} \n Computer Won!!")
    else:
        print('Enter valid input!!')

def condition(player, computer):
    #condition of player winning
    if (player == "r" and computer == "s" \
        or player == "p" and computer == "r" \
        or player == "s" and computer == "p"):
        return True

def sub(hand):
    if hand == 'r':
        return game[0]
    elif hand == 'p':
        return game[1]
    return game[2]

game = ["Rock", "Paper", "Scissors"]
title = " "
print(title.join(game))
print("'r' for rock, 's' for scissors, 'p' for paper")
print(play(input("What is your Choice: ")))
