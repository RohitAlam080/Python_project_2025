from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)

def slow_text(text, delay=0.06):
    for char in str(text):  # Convert any input to a string before printing
        print(char, end='', flush=True)
        sleep(delay)
    print()

def calculator():
    num1 = float(input(Fore.BLUE + "Enter first number: " + Style.RESET_ALL))
    sleep(0.4)
    opt = input(Fore.CYAN + "Enter operator (+,-,*,/): " + Style.RESET_ALL)
    sleep(0.4)
    num2 = float(input(Fore.YELLOW + "Enter second number: " + Style.RESET_ALL))
    sleep(0.4)
    
    
    if opt == "+":
        slow_text(str(num1 + num2))  # Convert result to string
    elif opt == "-":
        slow_text(str(num1 - num2))  # Convert result to string
    elif opt == "*":
        slow_text(str(num1 * num2))  # Convert result to string
    elif opt == "/":
        slow_text(str(num1 / num2))  # Convert result to string
    else:
        slow_text("Invalid operator")

    again = input(Fore.GREEN + "Do you want to calculate again? (Y/N): " + Style.RESET_ALL)
    if again.lower() == "y":
        calculator()
    else:
        slow_text(Fore.RED + "Goodbye!" + Style.RESET_ALL)

calculator()
