import random
set = ["rock", "paper", "scissors"]
choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
num = len(set)
result = random.randint(0, num-1)
if choice < num :
    print(f"You chose {set[choice]}")
    print(f"The computer chose {set[result]}")
    if choice == 0:
        if set[result] == "scissors":
            print("You win!")
        elif set[result] == "paper":
            print("You lose!")
    if choice == 1:
        if set[result] == "rock":
            print("You win!")
        elif set[result] == "scissors":
            print("You lose")
    if choice == 2:
        if set[result] == "paper":
            print("You win!")
        elif set[result] == "rock":
            print("You lose!")
    if set[choice] == set[result]:
        print("Draw!")
else:
    print("Invalid choice, try again.")


