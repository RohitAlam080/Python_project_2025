import random

top_of_range = input("Type a Number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("Please type a number larger then 0 next time.")
        quit()
else:
    print("Please type a valid number next time.")
    quit()

random_number = random.randint(1,top_of_range) # Generate a random number 
guesses =0

while True:
    guesses+=1
    user_guess = input("Make a Guess:")

    if user_guess.isdigit():
        user_guess =int(user_guess)
    else:
        print("please type a number next time.")
        continue

    if user_guess == random_number: # check the user guess here
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")

    else:
        print("You were below the number!")

    
print(f"You got it in {guesses} guesses!")  # show  attempts here