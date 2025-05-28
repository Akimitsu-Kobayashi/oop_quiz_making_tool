from quiz_generator import QuizTool
from open_quiz_to_answer import QuizAnswerTool
from termcolor import colored

if __name__ == "__main__":
    quiz_tool = QuizTool()
    quiz_answer_tool = QuizAnswerTool()

    while True:
        try:
            print("\n1) Create Quiz\n2) Answer Quiz\n3) Exit")
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                quiz_tool.menu()
            elif choice == 2:
                quiz_answer_tool.run()
            elif choice == 3:
                print(colored("Exiting the tool. Goodbye!", "blue"))
                break
            else:
                print(colored("Invalid choice. Please try again.", "red"))
        except:
            print("Invalid Input, please try again.")