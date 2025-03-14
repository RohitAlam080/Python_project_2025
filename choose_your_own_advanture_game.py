import random
from colorama import Fore, Style
# Game introduction
name = input("Type your name: ")
print(f"\nWelcome, {name}, to this grand adventure!\n")
health = 100  # Player starts with 100 health
inventory = []  # Inventory to store collected items
score = 0
# Start of the adventure
answer = input(
    "You are on a dark road. The path splits ahead. You can go LEFT or RIGHT. Which way do you choose? (left/right):").lower()

# Left Path
if answer == "left":
    print(Fore.RED + "You arrive at a rushing river.")
    answer = input("Do you want to SWIM across or WALK around it? (swim/walk):").lower()
    print(Style.RESET_ALL)
    if answer == "swim":
        if random.randint(1, 2) == 1:
            print("\nYou barely made it across, but lost 30 health due to exhaustion.")
            health -= 30
            score += 20
        else:
            print("\nOh no! You were eaten by an alligator. GAME OVER.")
            quit()

    elif answer == "walk":
        print("\nYou walked for miles and found an abandoned hut. Inside, you find a **torch** and a **map**!")
        inventory.append("torch")
        inventory.append("map")

    else:
        print("\nNot a valid option. You get lost in the wilderness. GAME OVER.")
        quit()

# Right Path
elif answer == "right":
    print("\nYou venture into a dark forest. It's eerily quiet...")
    answer = input("You hear rustling in the bushes. Do you CHECK it or IGNORE it? (check/ignore):").lower()

    if answer == "check":
        if random.randint(1, 3) == 1:
            print("\nA wild bear appears and attacks you! You barely escape but lose 40 health.")
            health -= 40
            score += 10
        else:
            print("\nYou find a **healing potion**! You drink it and gain 20 health.")
            health += 20
            inventory.append("healing potion")
            score += 10

    elif answer == "ignore":
        print("\nYou wisely avoid the danger and move ahead, but you feel uneasy...")

    else:
        print("\nNot a valid option. You hesitate for too long and a bandit robs you! GAME OVER.")
        quit()

# Cave Adventure
print("\nYou spot a mysterious **cave** ahead. A sign reads: 'Enter if you dare!'")
answer = input("Do you ENTER the cave or CONTINUE walking? (enter/continue) ").lower()

if answer == "enter":
    print("\nInside, you find an ancient **chest** guarded by a statue.")
    answer = input("Do you OPEN the chest or LEAVE it alone? (open/leave)").lower()

    if answer == "open":
        if "torch" in inventory:
            print("\nYou use your torch to see inside. It's filled with **gold and a sword**!")
            inventory.append("gold")
            inventory.append("sword")
            score += 40
        else:
            print("\nThe statue suddenly moves! It's a trap! You barely escape, losing 50 health.")
            health -= 50

    elif answer == "leave":
        print("\nYou respect the warning and exit the cave safely.")

    else:
        print("\nNot a valid option. You stumble into a hidden trap! GAME OVER.")
        quit()

# Final Decision
print("\nAfter a long journey, you finally see the exit of the forest.")
answer = input("A WISE OLD MAN stands in your path. Do you TALK to him or IGNORE him? (talk/ignore) ").lower()

if answer == "talk":
    if "gold" in inventory:
        print("\nThe old man sees your gold and gives you a map to the **Hidden Kingdom**. YOU WIN!")
        score += 20
    else:
        print("\nThe old man warns you of dangers ahead. You thank him and move on.")
elif answer == "ignore":
    print("\nYou walk past the old man, but you feel like you missed something important...")

# Game Summary
print("\n🎉 Congratulations, you've completed the adventure! 🎉")
print(f"Your final health: {health}")
print(f"Your inventory: {inventory}")
print(f"Your score : {score}")
