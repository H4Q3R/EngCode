from time import sleep
import random
import sys
from playsound import playsound
from colorama import Fore, Back, Style
import os
# DEF
def _app_():
    words = Fore.RED + "WELCOME TO ENGCODE"
    words_2 = Fore.GREEN + "Coding made easy for kids"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(0.5)
    for char in words_2:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(Style.RESET_ALL)
    sleep(1)
    while True:
        inp_cmd = input("EngCode@Console> ")
        if inp_cmd == 'quit' or inp_cmd == 'close' or inp_cmd == 'exit':
            exit_word = 'Quiting...'
            for char in exit_word:
                sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(1)
            quit()
        if inp_cmd == 'say':
            say_cmd = input("EngCode@Console:Say> ")
            print(say_cmd)
        if inp_cmd == 'ask':
            ask_cmd = input("EngCode@Console:Ask> ")
            input(ask_cmd)
        if inp_cmd == 'calculator':
            os.system("cls")
            x = input("EngCode@Console:Calculator> Enter the first number: ")
            y = input("EngCode@Console:Calculator> Enter the second number: ")
            op = input("EngCode@Console:Calculator> Enter the opration: ")
            if op == '+':
                print(int(x) + int(y))
            if op == '-':
                print(int(x) - int(y))
            if op == '*':
                print(int(x) * int(y))
            if op == '/':
                print(int(x) / int(y))
        if inp_cmd == 'turtle':
            os.system("python betterturtle.py")
            
_app_()