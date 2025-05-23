import time
from colorama import init, Fore, Style

init(autoreset=True)

class QuestionCreator:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename

    def run(self):
        self.welcome()
        while True:
            question = self.get_question()
            choice_a, choice_b, choice_c, choice_d = self.get_options()
            correct = self.get_correct_answer()
            self.save_to_file(question, choice_a, choice_b, choice_c, choice_d, correct)

            if not self.ask_continue():
                break

    def welcome(self):
        print(Fore.YELLOW + "========" + Style.BRIGHT + " Welcome to Quiz Creator " + Style.RESET_ALL + Fore.YELLOW + "========")
        time.sleep(1)

    def get_question(self):
        print(Fore.YELLOW + "Enter your quiz question:")
        return input(Fore.CYAN + "Q: ")

    def get_options(self):
        print(Fore.YELLOW + "Enter 4 options:")
        choice_a = input("a: ")
        choice_b = input("b: ")
        choice_c = input("c: ")
        choice_d = input("d: ")
        return choice_a, choice_b, choice_c, choice_d

    def get_correct_answer(self):
        while True:
            answer = input("Correct answer (a/b/c/d): ").lower()
            if answer in ['a', 'b', 'c', 'd']:
                print(Fore.YELLOW + "Saving the question...")
                time.sleep(1)
                return answer
            print(Fore.RED + "Invalid input.")

    def save_to_file(self, q, a, b, c, d, correct):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"Q: {q}\n")
            file.write(f"a. {a}\n")
            file.write(f"b. {b}\n")
            file.write(f"c. {c}\n")
            file.write(f"d. {d}\n")
            file.write(f"Correct Answer: {correct}\n\n")
            file.write("=" * 50 + "\n\n")

    def ask_continue(self):
        while True:
            answer = input("Add another question? (yes/no): ").lower()
            if answer == 'yes':
                return True
            elif answer == 'no':
                print(Fore.GREEN + "Questions saved!")
                return False
            print(Fore.RED + "Please enter 'yes' or 'no'.")
