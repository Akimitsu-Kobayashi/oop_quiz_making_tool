import time
import os
import pyfiglet
from termcolor import colored

class Quiz_Tool:
    
    def __init__(self,):
        self.base_name = input("File name of quiz: ").strip()
        self.time_stamp = time.strftime("%d%m%Y_%H%M%S")
        self.file_name = f"{self.base_name}_{self.time_stamp}.txt"
        self.question_number = 1
        self.questions_made = 0

        title = pyfiglet.figlet_format("Welcome to \n QUIZ MAKER")
        print(colored(title, "blue"))

Quiz_Tool()