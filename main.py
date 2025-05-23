#Planning to put the main menu here 
#Where the user could make the choice of having to create the quiz or run the quiz  
from quiz_create_questions import QuestionCreator
from quiz_game import QuizGame
import time
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n======= Main Menu =======")
        print(Fore.YELLOW + "1. Create Quiz Questions")
        print(Fore.GREEN + "2. Play the Quiz")
        print(Fore.RED + "3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            creator = QuestionCreator()
            creator.run()
        elif choice == '2':
            game = QuizGame()
            game.start()
        elif choice == '3':
            print("Goodbye!")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
