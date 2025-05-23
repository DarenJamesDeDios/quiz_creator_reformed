#Planning to put the main menu here 
#Where the user could make the choice of having to create the quiz or run the quiz  
from quiz_create_questions import QuestionCreator
from quiz_game import QuizGame
import time
from colorama import init, Fore, Style

init(autoreset=True)

class QuizMain:
    def __init__(self):
        self.running = True

    def display_menu(self):
        print(Fore.BLUE + Style.BRIGHT + "\n======= Main Menu =======")
        print(Fore.YELLOW + "1. Create Quiz Questions")
        print(Fore.GREEN + "2. Play the Quiz")
        print(Fore.RED + "3. Exit")

    def handle_choice(self, choice):
        if choice == '1':
            creator = QuestionCreator()
            creator.run()
        elif choice == '2':
            game = QuizGame()
            game.start()
        elif choice == '3':
            print("Goodbye!")
            time.sleep(1)
            self.running = False
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Enter your choice (1/2/3): ").strip()
            self.handle_choice(choice)

if __name__ == "__main__":
    main = QuizMain()
    main.run()
