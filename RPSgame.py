from random import choice
# player_score = 0
# computer_score = 0
roundtimes = 3
player = None
computer = choice(['rock', 'paper', 'scissors'])
# print("computer choices: " + player2)
while True:
    player_score = 0
    computer_score = 0

    for time in range(roundtimes):
        print("...rock...")
        print("...paper...")
        print("...scissors...")
        print(f"your score:{player_score} ; comupter's score:{computer_score}")        
        player = input("enter your choice:").lower()
        if player != "q":   
            if player == computer:
                print("computer choice:" + computer)
                print("It's a tie!")
            elif player == "rock" and computer == "scissors":
                player_score += 1
                print("computer choice:" + computer)
                print("player wins!")
            elif player == "paper" and computer == "rock":
                player_score += 1
                print("computer choice:" + computer)
                print("player wins!")
            else:
                computer_score += 1
                print("computer choice:" + computer)
                print("computer wins!")
        else:
            print("Bye!")
            break


    if player_score > computer_score:
        print(f"you won! your: {player_score}, computer's: {computer_score}")        
    elif computer_score > player_score:
        print(f"computer won! your: {player_score}, computer's: {computer_score}")  
    else:
        print(f"It's tie! your: {player_score}, computer's: {computer_score}")

    answer = input("Do you want to play again? (y/n)").lower()
    if answer == "y":
        computer = choice(['rock', 'paper', 'scissors'])   
    else:
        break
