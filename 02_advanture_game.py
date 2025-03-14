import random
from time import sleep
from colorama import Fore, Style

def print_slow(text, color=Fore.WHITE):
    """Simulates text appearing slowly for immersion with colors."""
    for char in text:
        print(color + char, end='', flush=True)
        sleep(0.02)
    print(Style.RESET_ALL)  # Reset color

def get_input(prompt):
    try:
        return input(prompt).lower()
    except OSError:
        return ""

# Game Introduction
score = 0
health = 100
inventory = []
gold = 10

name = get_input(Fore.YELLOW + "Type your name, brave adventurer: " + Style.RESET_ALL)
print_slow(f"\n🎉 Welcome, {name}, to the Realm of Eldoria! A land of magic and mystery... 🏰\n", Fore.CYAN)

# First Choice: Entering the Forest or Staying in Town
answer = get_input(Fore.GREEN + "You stand at the entrance of a dark forest. Do you ENTER the forest 🌲 or RETURN to town 🏨? " + Style.RESET_ALL)

if answer == "enter":
    print_slow("\n🌲 You step into the eerie woods, where shadows whisper secrets...", Fore.MAGENTA)
    answer = get_input("A fork in the road! Do you go LEFT 🏮 towards a glowing shrine, RIGHT 🐺 towards distant howling, or STRAIGHT into the unknown? ")
    
    if answer == "left":
        print_slow("\n✨ You find an ancient shrine. Inside, a spirit offers you a MAGIC AMULET! 🔮", Fore.YELLOW)
        inventory.append("Magic Amulet")
        score += 10
    elif answer == "right":
        print_slow("\n🐺 You are attacked by wolves! You barely escape but lose 30 health.", Fore.RED)
        health -= 30
        score += 5
    elif answer == "straight":
        print_slow("\n🕷️ You discover a hidden cave filled with treasure but guarded by giant spiders!", Fore.BLUE)
        choice = get_input("Do you FIGHT 🗡️ or RUN 🏃? ")
        if choice == "fight":
            if random.randint(1, 3) == 1:
                print_slow("\n🕷️ The spiders overwhelm you. You barely escape but lose 50 health.", Fore.RED)
                health -= 50
            else:
                print_slow("\n💰 You defeat the spiders and find gold and a sword!", Fore.GREEN)
                inventory.append("Sword")
                gold += 50
                score += 20
        else:
            print_slow("\n🏃 You flee safely but leave empty-handed.", Fore.YELLOW)
else:
    print_slow("\n🏨 You return to town and find a bustling market.", Fore.BLUE)
    answer = get_input("Do you visit the BLACKSMITH ⚔️, the HERBALIST 🌿, or the TAVERN 🍻? ")
    
    if answer == "blacksmith":
        if gold >= 10:
            print_slow("\n⚔️ You buy a sturdy sword for 10 gold!", Fore.GREEN)
            inventory.append("Sword")
            gold -= 10
            score += 10
        else:
            print_slow("\n💰 You don't have enough gold!", Fore.RED)
    elif answer == "herbalist":
        print_slow("\n🌿 You buy a healing potion and restore 20 health.", Fore.GREEN)
        health += 20
        score += 5
    elif answer == "tavern":
        print_slow("\n🍻 You overhear rumors about a hidden dungeon containing treasures...", Fore.YELLOW)

# Second Phase: Facing the Dragon
print_slow("\nAfter your preparations, you hear rumors of a DRAGON 🐉 in the mountains...", Fore.CYAN)
answer = get_input("Do you SEEK the dragon 🐉, EXPLORE the ruins 🏛️, or HUNT for bandits 💀? ")

if answer == "seek":
    print_slow("\n🔥 You find the dragon’s lair. It awakens, staring at you!", Fore.RED)
    if "Sword" in inventory:
        print_slow("\n⚔️ You fight bravely and slay the dragon! You win! 🎉", Fore.GREEN)
        score += 50
    elif "Magic Amulet" in inventory:
        print_slow("\n🔮 The dragon senses your amulet and spares you, revealing hidden treasures. You win! 🎉", Fore.YELLOW)
        score += 100
    else:
        print_slow("\n💀 You are no match for the dragon. It burns you to ashes. GAME OVER. ☠️", Fore.RED)
        quit()

elif answer == "explore":
    print_slow("\n🏛️ The ruins contain ancient writings and a golden chest...", Fore.MAGENTA)
    if "Magic Amulet" in inventory:
        print_slow("\n✨ The amulet glows, and the chest opens! You gain 50 gold! 💰", Fore.YELLOW)
        gold += 50
        score += 30
    else:
        print_slow("\n⚠️ A trap is triggered! You barely escape, losing 40 health.", Fore.RED)
        health -= 40
        score += 10

elif answer == "hunt":
    print_slow("\n💀 You track down a gang of bandits terrorizing the land.", Fore.BLUE)
    if "Sword" in inventory:
        print_slow("\n⚔️ You defeat the bandits and claim their loot!", Fore.GREEN)
        gold += 30
        score += 40
    else:
        print_slow("\n💀 The bandits overpower you. You barely escape but lose 60 health.", Fore.RED)
        health -= 60
        score += 10

# Game Summary
print_slow("\n🏆 Adventure Complete! 🏆", Fore.CYAN)
print(Fore.GREEN + f"Your final health: {health}")
print(Fore.BLUE + f"Your inventory: {inventory}")
print(Fore.YELLOW + f"Your total gold: {gold}")
print(Fore.MAGENTA + f"Your final score: {score}" + Style.RESET_ALL)
