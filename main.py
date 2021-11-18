import os
import sys
import random
import time
from art import *
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
    print(TITLE)
    time.sleep(5)

def character_creation():
    global player

    clear_screen()

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
    clear_screen()

    while True:
        choice = input('What do you want to go? [Explore/Inventory]    Type "-help" for further information.\n -> ').lower()

        if choice == "explore":
            choose_door()
            if choose_door():
                continue

            else: # THE PLAYER HAS DIED
                break

        elif choice == "inventory":
            inventory()
            continue

        elif choice == "-help":
            help()
            continue

        elif choice == "-quit":
            break

        else:
            print("Invalid input.")
            continue

def combat():
    clear_screen()

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
            if battle == True:
                hit = random.randint(1, 5)
                if hit == 1:
                    print(f"You missed.")
                
                else:
                    if enemy_action == "defend":
                        defend = random.randint(1, 2)
                        if defend == 1:
                            enemy_health -= player_attack
                            print(f"{enemy.name} failed in defending against your attack and took {player.attack} damage. {enemy.name} HP: {enemy_health}")

                        else:
                            enemy_health -= player_attack - enemy.defence
                            print(f"{enemy.name} succesfully defended against the attack. {enemy.name} HP: {enemy_health}")
                    
                    else:
                        enemy_health -= player_attack
                        print(f"{enemy.name} took {player_attack} damage. {enemy.name} HP: {enemy_health}")
                    
            if enemy_health <= 0:
                print(f"{enemy.name} has been slain.")
                alive = True
                battle = False

        elif player_action == "defend":
            if enemy_action == "attack":
                if battle == True:
                    hit = random.randint(1, 5)
                    if hit == 1:
                        print(f"{enemy.name} missed.")
                    
                    else:
                        if player_action == "defend":
                            defend = random.randint(1, 2)
                            if defend == 1:
                                player_health -= enemy_attack
                                print(f"You failed in defending against the attack and took {enemy.attack} damage. {player.name} HP: {player_health}")

                            else:
                                player_health -= enemy_attack - player.defence
                                print(f"You succesfully defended against the attack. {player.name} HP: {player_health}")
                        
                        else:
                            player_health -= enemy_attack
                            print(f"You took {enemy_attack} damage. {player.name} HP: {player_health}")
                        
                if player_health <= 0:
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
    clear_screen()

    print('''
The goal of this game is to kill enemies and get as high of a highscore as possible.
If your HP goes below zero you die and lose all of your progress.
Whenever you are faced with an input you should type one of the actions inside these brackets [].

If you want to quit the game type "-quit" (this only works in the pick-a-door room).
''')

def inventory():
    pass