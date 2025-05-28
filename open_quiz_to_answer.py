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

QuizAnswerTool().find_text_files()

