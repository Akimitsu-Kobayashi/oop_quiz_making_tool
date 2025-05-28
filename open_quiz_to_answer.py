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
