import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

filename = "quiz_questions.txt"

def welcome_message():
    print(Fore.YELLOW + "========" + Style.BRIGHT + "Welcome to Quiz Creator" + Style.RESET_ALL + Fore.YELLOW + "=========")
    time.sleep(2)

def get_question():
    print(Fore.YELLOW + "Please enter your quiz question.")
    return input(Fore.YELLOW + "Q: ")

def get_options():
    print(Fore.YELLOW + "Please input the 4 possible answers.")
    choice_a = input("For letter a: ")
    choice_b = input("For letter b: ")
    choice_c = input("For letter c: ")
    choice_d = input("For letter d: ")
    return choice_a, choice_b, choice_c, choice_d

def get_correct_answer():
    while True:
        answer = input("The correct answer? (a, b, c, or d): ").lower()
        if answer in ['a', 'b', 'c', 'd']:
            print(Fore.YELLOW + "Saving the question and answer...")
            time.sleep(3)
            print(Fore.GREEN + "Done!")
            time.sleep(1)
            return answer
        else:
            print(Fore.RED + "Invalid input, please choose only a, b, c, or d")
            time.sleep(1)

def save_to_file(question, choice_a, choice_b, choice_c, choice_d, correct):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"Q: {question}\n")
        file.write(f"a. {choice_a}\n")
        file.write(f"b. {choice_b}\n")
        file.write(f"c. {choice_c}\n")
        file.write(f"d. {choice_d}\n")
        file.write(f"Correct Answer: {correct}\n\n")
        file.write("=" * 50 + "\n\n")

def ask_continue():
    while True:
        print(Fore.YELLOW + "Do you want to add another quiz question?")
        response = input(Fore.GREEN + "yes" + Style.RESET_ALL + " or " + Fore.RED + "no" + Style.RESET_ALL + "?: ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            print(Fore.YELLOW + "Exiting...")
            time.sleep(3)
            print("Your quiz questions are now " + Fore.GREEN + "saved" + Style.RESET_ALL + ".")
            return False
        else:
            print("Only " + Fore.GREEN + "yes" + Style.RESET_ALL + " or " + Fore.RED + "no" + Style.RESET_ALL + " answers are allowed, my friend.")
            time.sleep(1)

# Main program loop
def main():
    welcome_message()
    while True:
        question = get_question()
        choice_a, choice_b, choice_c, choice_d = get_options()
        correct = get_correct_answer()
        save_to_file(question, choice_a, choice_b, choice_c, choice_d, correct)
        if not ask_continue():
            break

# Start the program
if __name__ == "__main__":
    main()
