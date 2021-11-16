import os
import sys
import random
import time
from classes import *

def clear_screen():
    os.system('cls')

def typewriter(message):
    for char in message:
        time.sleep(random.choice([0.02, 0.04, 0.06, 0.08, 0.10]))
        sys.stdout.write(char)
        sys.stdout.flush()

def title_screen():
    print(f'''
__________________________________________________________________________________________________________________
|                                                                                                                |
|                     ______   ______     __         __         ______     __  __     ______                     |
|                    /\  ___\ /\  __ \   /\ \       /\ \       /\  __ \   /\ \/\ \   /\__  _\                    |
|                    \ \  __\ \ \  __ \  \ \ \____  \ \ \____  \ \ \/\ \  \ \ \_\ \  \/_/\ \/                    |
|                     \ \_\    \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\    \ \_\                    |
|                      \/_/     \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/     \/_/                    |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
|                                                BY NEO AND VIGGO                                                |
|                                                                                                                |
|                                                                                                                |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ''')

def character_creation():
    global player

    while True:
        player_name = input("What is your name? -> ")
        if player_name.isalpha():
            while True:
                confirmation = input(f"Are you sure you want to be known as {player_name}? [Y/N] -> ").upper()
                if confirmation in ["Y", "N"]:
                    break

                else:
                    print("Invalid input. Y for Yes or N for No.")
                    continue

            if confirmation == "Y":
                break

            elif confirmation == "N":
                continue

        else:
            print("Invalid input. Use only letters.")
    
    player_health = 10
    player_attack = 1
    player_defence = 0

    player = Player(player_name, player_health, player_attack, player_defence)

# def adventure():
#     while True:
#         action = input("What do you want to do? [Explore/Inventory] -> ").lower()
#         if action == "explore":
#             explore()
# 
#         elif action == "inventory":
#             inventory()
# 
#         else:
#             print("Invalid input.")
#             continue
# 
# def explore():
#     pass
# 
# def inventory():
#     pass

def combat():
    battle = True

    enemy = random.choice(enemy_list)
    enemy_health = enemy.get_health()

    print(f"{enemy.name} HP: {enemy_health}")

    while battle:
        action = input("Choose action [Attack/Defend/Rest] -> ").lower()
        if action == "attack":
            hit = random.randint(1, 5)
            if hit == 1:
                print("You missed.")
            else:
                enemy_health -= player.get_attack()
                if enemy_health > 0:
                    print(f"{enemy.name} took {player.get_attack()} damage. HP: {enemy_health}")
                else:
                    print(f"You have slain {enemy.name}.")
                    battle = False

        elif action == "defend":
            pass

        elif action == "rest":
            pass

        else:
            print("Invalid input.")
            continue