print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("enter your choice:")
from random import choice
player2 = choice(['rock', 'paper', 'scissors'])
# print("computer choices: " + player2)

if player1 == "rock" or player1 == "paper" or player1 == "scissors":
    print("computer choices: " + player2)
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("player1 wins!")
        elif player2 == "paper":
            print("player2 wins!")
    elif player1 == "paper":
        if player2 == "rock":
            print("player1 wins!")
        elif player2 == "scissors":
            print("player2 wins!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("player1 wins!")
        elif player2 == "rock":
            print("player2 wins!")
else:
    print("something went wrong")
