import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

class QuizGame:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename

    def start(self):
        print(Fore.CYAN + "Loading quiz...")
        questions = self.load_questions()
        if not questions:
            print(Fore.RED + "No questions found.")
            return

        random.shuffle(questions)
        score = 0

        for i, (q, choices, correct) in enumerate(questions, 1):
            print(f"\n{Style.BRIGHT}Question {i}: {q}")
            for key, value in choices.items():
                print(f"  {key}. {value}")
            answer = input("Your answer (a/b/c/d): ").lower()
            if answer == correct:
                print(Fore.GREEN + "Correct!")
                score += 1
            else:
                print(Fore.RED + f"Wrong. Correct was {correct}: {choices[correct]}")
            time.sleep(1.5)

        print(f"\nYour final score: {Fore.CYAN}{score}/{len(questions)}{Style.RESET_ALL}")

    def load_questions(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
        except FileNotFoundError:
            return []

        blocks = content.split("=" * 50)
        questions = []

        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue
            question = lines[0][3:].strip()
            choices = {
                'a': lines[1][3:].strip(),
                'b': lines[2][3:].strip(),
                'c': lines[3][3:].strip(),
                'd': lines[4][3:].strip()
            }
            correct = lines[5].split(":")[1].strip().lower()
            questions.append((question, choices, correct))

        return questions
