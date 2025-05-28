import os
import random
import pyfiglet
from termcolor import colored

class QuizAnswerTool:
    def __init__(self):
        self.title = pyfiglet.figlet_format("Welcome to \n Answer Quiz")
        print(colored(self.title, "blue"))

        self.text_files = []
        self.each_line = []
        self.total_score = 0
    
    def find_text_files(self):
        # Find text files in the current directory
        for files_name in os.listdir("."):
            if files_name.endswith(".txt"):
                self.text_files.append(files_name)
        # print the found text files
        number_counter = 0
        for files in self.text_files:
            print(f"{str(number_counter + 1)}) {files}")
            number_counter += 1

    def select_file(self):
        while True:
            try:
                selected_file = int(input("Enter which file you want to open: "))
                if 0 < selected_file <= len(self.text_files):
                    break
                else:
                    print(colored("Error: Number Out of Range", "red"))
            except:
                print(colored("Error: The Input is not a number", "red"))

        with open(self.text_files[selected_file - 1] , 'r') as quiz_file:
            for lines in quiz_file:
                self.each_line.append(lines)
        #each question is composed of 6 lines
        self.number_of_questions = len(self.each_line) // 6 

    def ask_questions(self):
        #randomize questions
        randomizer = random.sample(range(1, self.number_of_questions + 1), self.number_of_questions)

        for random_number in randomizer:
            index = (random_number - 1) * 6
            current_question = self.each_line[index:index + 5]

            for lines in current_question:
                print(lines, end = '')
            #get users answer
            while True:
                try:
                    answer = input("\nEnter Your Answer: ")
                    if answer.lower().strip() not in ['a', 'b', 'c', 'd']:
                        print(colored("Invalid Input possible answers are only (a/b/c/d)", "red"))
                    else:
                        break
                except:
                    print(colored("Invalid Input possible answers are only (a/b/c/d)", "red"))
            #show if answer is correct
            current_answer = self.each_line[index+5][16:].strip().lower()
            if answer.lower().strip() == current_answer:
                print(colored("correct\n", "green"))
                total_score += 1

            else:
                print(colored("incorrect\n", "red"))

    def display_score(self):
        #show red if failed and green if pass
        grade = round((self.total_score / self.number_of_questions) * 100, 2)

        print("Average Score: ", end = '')

        if 25 <= grade <= 70:
            print(colored(grade, "yellow"))
        elif 0 == grade < 25:
            print(colored(grade, "red")) 
        else:
            print(colored(grade, "green"))

    def run(self):
        self.find_text_files()
        self.select_file()
        print("\n")
        self.ask_questions()
        self.display_score()
