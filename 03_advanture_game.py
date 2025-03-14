from time import sleep
from colorama import Fore, Style

def slow_print(text, delay=0.02):
    """Prints text character by character with a delay for better interaction."""
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()  # Move to the next line after printing

# Start Quiz
slow_print(Fore.BLUE + "Welcome To The Ultimate Computer Quiz!" + Style.RESET_ALL, 0.02)
sleep(1)
slow_print(Fore.RED + "You Will Be Asked Multiple Questions About Computers!" + Style.RESET_ALL, 0.02)
sleep(1)

playing = input("Do You Want To Play? (yes/no): ")

if playing.lower() != "yes":
    slow_print("Alright! Maybe next time. 👋", 0.02)
    quit()

slow_print("Okay! Let's Begin 😊", 0.02)
sleep(1)

score = 0

# Extended Questions and Answers
questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does ROM stand for? ": "read only memory",
    "What does SSD stand for? ": "solid state drive",
    "Which company developed Windows OS? ": "microsoft",
    "What is the brain of the computer? ": "cpu",
    "Which type of memory is volatile? ": "ram",
    "What does HTTP stand for? ": "hypertext transfer protocol",
    "What is the full form of USB? ": "universal serial bus",
    "What does HTML stand for? ": "hypertext markup language",
    "Which programming language is known as the 'mother of all languages'? ": "c",
    "What does BIOS stand for? ": "basic input output system",
    "What is the main function of an operating system? ": "manage hardware and software",
    "What is an IP address used for? ": "identifying devices on a network",
    "Which company developed the Python programming language? ": "cwi",
    "What is the binary number system based on? ": "0 and 1",
    "Which key combination is used to copy text? ": "ctrl + c",
    "Which type of software helps users perform tasks? ": "application software",
    "What is the name of the first mechanical computer? ": "analytical engine"
}

# Ask Questions
for question, correct_answer in questions.items():
    slow_print(Fore.YELLOW + question + Style.RESET_ALL, 0.02)
    answer = input().lower()
    
    if answer == correct_answer:
        slow_print(Fore.GREEN + "Correct! 😯" + Style.RESET_ALL, 0.02)
        score += 1
    else:
        slow_print(Fore.RED + f"Incorrect! 😒 The correct answer is: {correct_answer}" + Style.RESET_ALL, 0.02)
    
    sleep(1)  # Short pause before next question

# Final Score
slow_print(Fore.CYAN + f"\nQuiz Completed! You answered {score} out of {len(questions)} questions correctly." + Style.RESET_ALL, 0.02)

percentage = (score / len(questions)) * 100
slow_print(Fore.MAGENTA + f"Your Score: {percentage:.2f}% 🎯" + Style.RESET_ALL, 0.02)

if percentage == 100:
    slow_print(Fore.GREEN + "🎉 Perfect Score! You're a Computer Genius! 🏆" + Style.RESET_ALL, 0.02)
elif percentage >= 75:
    slow_print(Fore.BLUE + "Great Job! You really know your computers! 💻" + Style.RESET_ALL, 0.02)
elif percentage >= 50:
    slow_print(Fore.YELLOW + "Not Bad! Keep Learning! 📚" + Style.RESET_ALL, 0.02)
else:
    slow_print(Fore.RED + "You need to study more! Keep practicing! 🤓" + Style.RESET_ALL, 0.02)

slow_print(Fore.GREEN + "\nThank You For Playing The Computer Quiz! 🎮" + Style.RESET_ALL, 0.02)
