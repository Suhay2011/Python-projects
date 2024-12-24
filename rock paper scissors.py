import random #importing random module

while True : #iterate loop
    user_action = input("Enter a choice (rock paper scissors):")#take input
    possible_action = ["Rock", "Paper", "Scissiors"]
    computer_action = randon.choice(possible_action)

    print(f"You chose {user_action}, computer chose{computer_action}. /n")
#display both outputs what is selected by you and the computer

#condition to check who won the game
    if user_action == computer_action:
       print("Both players selected {user_action}. It's a Tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes Scissors! You Win!")
        else:
            print("Paper covers Rock! You Loose!:(")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You Win!")
        else:
            print("Scissors cuts Paper! You Loose!:(")
    elif user_action == "Scissors":
        if computer_action == "Paper":
           print("Scissors cuts Paper! You Win!")
           else:
            print("Rock smashes scissors! You Loose!:(")


            