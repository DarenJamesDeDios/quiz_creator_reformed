#Modules imported
import time

filename = "quiz_questions.txt"

def welcome_message():
    print("\033[33m========\033[1mWelcome to Quiz Creator\033[0m\033[33m=========\033[0m")
    time.sleep(2)

def get_question():
    print("\033[33mPlease enter your quiz question.\033[0m")
    return input("\033[33mQ\033[0m: ")

def get_options():
    print("\033[33mPlease input the 4 possible answers.\033[0m")
    choice_a = input("For letter a: ")
    choice_b = input("For letter b: ")
    choice_c = input("For letter c: ")
    choice_d = input("For letter d: ")
    return choice_a, choice_b, choice_c, choice_d

def get_correct_answer():
    while True:
        answer = input("The correct answer? (a, b, c, or d): ").lower()
        if answer in ['a', 'b', 'c', 'd']:
            print("\033[33mSaving the question and answer...\033[0m")
            time.sleep(3)
            print("\033[32mDone!\033[0m")
            time.sleep(1)
            return answer
        else:
            print("\033[31mInvalid input, please choose only a, b, c, or d\033[0m")
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
        print("\033[33mDo you want to add another quiz question?\033[0m")
        response = input("\033[32myes\033[0m or \033[31mno\033[0m?: ").lower()
        if response == 'yes':
            return True
        elif response == 'no':
            print("\033[33mExiting...\033[0m")
            time.sleep(3)
            print("Your quiz questions are now \033[32msaved\033[0m.")
            return False
        else:
            print("Only \033[32myes\033[0m or \033[31mno\033[0m answers are allowed, my friend.")
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
main()
