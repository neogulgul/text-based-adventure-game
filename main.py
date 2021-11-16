import os
import time

def clear_screen():
    os.system('cls')

def main():
    clear_screen()
    title_screen()
    character_creation()

def title_screen():
    print('''
                        LOREM IPSUM
    ''')
    time.sleep(1)

def character_creation():
    while True:
        clear_screen()
        player_name = input("What is your name? -> ")
        if player_name.isalpha():
            print()