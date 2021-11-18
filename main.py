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
    clear_screen()
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
                confirmation = input(f"Are you sure you want to be known as {player_name}? [Y/N] -> ").lower()
                if confirmation in ["y", "n"]:
                    break

                else:
                    print("Invalid input. Y for Yes or N for No.")
                    continue

            if confirmation == "y":
                break

            elif confirmation == "n":
                continue

        else:
            print("Invalid input. Use only letters.")
    
    player_health = 10
    player_attack = 1
    player_defence = 0

    player = Player(player_name, player_health, player_attack, player_defence)

def adventure():
    pass

def combat():
    battle = True

    player_health = player.get_health()
    player_attack = player.attack

    enemy = random.choice(enemy_list)
    enemy_health = enemy.get_health()
    enemy_attack = enemy.attack

    print(f"{enemy.name} HP: {enemy_health}")

    while battle:
        player_action = input("Choose action [Attack/Defend/Rest] -> ").lower()
        enemy_action = random.choice(["attack", "attack", "attack", "defend"])

        if player_action == "attack":
            hit = random.randint(1, 5)
            if hit == 1:
                print("You missed.")
            
            else:
                if enemy_action == "defend":
                    enemy_health -= player_attack - enemy.defence
                
                else:
                    enemy_health -= player_attack
                    if enemy_health > 0:
                        print(f"{enemy.name} took {player_attack} damage. {enemy.name} HP: {enemy_health}")
                    
                    else:
                        print(f"You have slain {enemy.name}.")
                        alive = True
                        battle = False

        if enemy_action == "attack":
            if battle == True:
                hit = random.randint(1, 5)
                if hit == 1:
                    print(f"{enemy.name} missed.")
                
                else:
                    if player_action == "defend":
                        defend = random.randint(1, 2)
                        if defend == 1:
                            print(f"You failed in defending against the attack and took {enemy.attack} damage.")
                            player_health -= enemy_attack

                        else:
                            print(f"You succesfully defended against the attack.")
                            player_health -= enemy_attack - player.defence
                    
                    else:
                        player_health -= enemy_attack
                        print(f"You took {enemy_attack} damage. {player.name} HP: {player_health}")
                    
                    if player_health < 0:
                        print(f"{player.name} has been slain by {enemy.name}. Game Over.")
                        alive = False
                        battle = False
        
        elif player_action == "defend" and enemy_action == "defend":
            pass

        else:
            print("Invalid input.")
            continue
    
    player.set_health(player_health)

    return alive

def help():
    print('''
This goal of this game is to kill enemies and get as big of a highscore as possible.
If your HP goes below zero you die and lose all of your progress.
''')