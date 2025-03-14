import random

user_wins =0
computer_wins =0

options = ["rock","paper","scissors"]

while True:
    user_input =input("Type Rock/Paper/Scissors or Q to quits:").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input! Please type rock, paper or scissors.")
        continue

    random_number = random.randint(0,2)
    computer_pick =options[random_number] #Rock :0 ,paper:1 ,scissors: 2

    print(f"computer picked {computer_pick}.")
    # win conditions
    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins +=1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins +=1

    elif user_input == computer_pick:
        print("It's a Tie!") 
        
    else:
        print("You lost!")
        computer_wins +=1

# Final results
print(f"You won {user_wins} times")
print(f"The Computer Won {computer_wins}times")
print("Goodbye!")

