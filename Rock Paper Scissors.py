import random as r

draw = 0
won = 0
player_answer = input("Your Turn: ")
computer_choice = r.choice(["Rock", "Paper", "Scissors"])
print(computer_choice)

if computer_choice == player_answer:
    draw = True

if player_answer == "Scissors":
    if computer_choice == "Rock":
        won = False
    if computer_choice == "Paper":
        won = True

if player_answer == "Rock":
    if computer_choice == "Scissors":
        won = True
    if computer_choice == "Paper":
        won = False

if player_answer == "Paper":
    if computer_choice == "Rock":
        won = True
    if computer_choice == "Paper":
        won = False

if not won:
    print("You lost")

if won:
    print("You won")

if draw:
    print("Tie")

