from time  import sleep
from colorama import Fore, Style

print(Fore.BLUE + "Welcome To Computer Quiz!" + Style.RESET_ALL)
print(Fore.RED + "You Will Be Asked 4 Questions About Computers!" + Style.RESET_ALL)

playing = input("Do You Want To Play?:") 

if playing.lower()!= "yes":
    quit()

print("Okay! Let's Play 😊")
score=0
answer = input("What does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("Correct!😯")
    score += 1

else:
    print("Incorrect!😒") 
    ###########################
answer = input("What does GPU stands for ?")
if answer.lower() == "graphics processing unit":
    print("Correct!😯")
    score+=1

else:
    print("Incorrect!😒") 
    ###########################
answer = input("What does RAM stands for ?")
if answer.lower() == "random access memory":
    print("Correct!😯")
    score +=1

else:
    print("Incorrect!😒") 
    ###########################
answer = input("What does ROM stands for ?")
if answer.lower() == "read only memory":
    print("Correct!😯")
    score +=1

else:
    print("Incorrect!😒")

print("You got " +str(score)+ " Questions Correct!")
print(Fore.CYAN + f"congradulations! You got {str((score/4) * 100)}%." + Style.RESET_ALL)
print(Fore.GREEN + "Thank You For Playing Computer Quiz!" + Style.RESET_ALL)