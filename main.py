import os
import sys
import random
import time
from classes import *
from art import *
from text import *

def clear_screen():
    os.system('cls')

def typing(message):
    for char in message:
        time.sleep(random.choice([0.02, 0.04, 0.06, 0.08, 0.10]))
        sys.stdout.write(char)
        sys.stdout.flush()

def title_screen():
    clear_screen()
    print(TITLE)
    time.sleep(1)

def intro():
    clear_screen()
    typing("Welcome to the dungeon.")
    time.sleep(1)

def character_creation():
    global player

    clear_screen()

    while True:
        player_name = input("What is your name? -> ")
        if player_name.isalpha() and len(player_name) <= 20:
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
            print("Invalid input. Use only letters. Can not be more than 20 characters long.")
    
    player_health = 10
    player_attack = 2
    player_defence = 0
    player_speed = 10

    player = Player(player_name, player_health, player_attack, player_defence, player_speed)

def adventure():
    clear_screen()

    while True:
        choice = input('What do you want to do? [Explore/Inventory] (Type "-help" for further information) -> ').lower()

        if choice == "explore":
            if choose_door():
                continue

            else: # THE PLAYER HAS DIED
                break

        elif choice == "inventory":
            check_inventory()
            continue

        elif choice == "-help":
            if help():
                continue

            else: # THE PLAYER CHOSE TO QUIT THE GAME
                break

        else:
            print("Invalid input.")
            continue

def check_inventory():
    clear_screen()
    if len(inventory_items) == 3:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, inventory_items[1].name, inventory_items[2].name

    elif len(inventory_items) == 2:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, inventory_items[1].name, None

    elif len(inventory_items) == 1:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, None, None

    else:
        item_slot_1, item_slot_2, item_slot_3 = None, None, None

    print(f'''----- {player.name}'s Stats -----
    Name: {player.name}
    HP: {player.health}/{player.max_health}
    ATK: {player.attack}
    DEF: {player.defence}
    SPD: {player.speed}
    Headgear: {None}
    Chestpiece: {None}
    Leggings: {None}
    Item slot 1: {item_slot_1}
    Item slot 2: {item_slot_2}
    Item slot 3: {item_slot_3}
    ''')

def choose_door():
    while True:
        direction = input("What door do you go into? [North/West/East] -> ").lower()

        if direction in ["north", "west", "east"]:
            print(f"You go through the {direction} door.")
            random.choice([combat, combat, combat, trap, treasure, bonfire])()
            break

        else:
            print("Invalid input.")
            continue
    
    if player.health <= 0:
        return False

    return True

def combat():
    clear_screen()

    battle = True

    player_name = player.name
    player_HP = player.health
    player_ATK = player.attack
    player_DEF = player.defence
    player_SPD = player.speed

    enemy = random.choice(list_of_enemies)
    enemy_name = enemy.name
    enemy_HP = enemy.health
    enemy_ATK = enemy.attack
    enemy_DEF = enemy.defence
    enemy_SPD = enemy.speed

    print(f"You have encountered a {enemy_name} with {enemy_HP} HP.")

    while battle:
        print(f"{player_name} HP: {player_HP}\n{enemy_name} HP: {enemy_HP}")

        player_action = input("What do you choose to do? [Attack/Defend/Item] -> ").lower()

        if player_action == "defend" and player_DEF == 0:
            print("You have 0 defence and therefore can't defend.")
            continue

        if enemy_DEF == 0:
            enemy_action = "attack"
        
        else:
            enemy_action = random.choice(["attack", "attack", "attack", "defend"])

        if player_action not in ["attack", "defend", "item"]:
            print("Invalid input.")
            continue

        elif player_action == "item":
            if len(inventory_items) == 0:
                print("You have no items.")
                continue
            
            else:
                use_item()

        elif player_action == "defend" and enemy_action == "defend":
            print("You both chose to defend and nothing happened.")

        if player_SPD > enemy_SPD:
            enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF)
            if enemy_HP <= 0:
                print(f"You have slain {enemy_name}.")
                battle = False
            
            else:
                player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK)
                if player_HP <= 0:
                    print(f"{player_name} has been slain. Game Over.")
                    battle = False

        elif player_SPD < enemy_SPD:
            player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK)
            if player_HP <= 0:
                print(f"{player_name} has been slain. Game Over.")
                battle = False
            
            else:
                enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF)
                if enemy_HP <= 0:
                    print(f"You have slain {enemy_name}.")
                    battle = False

        elif player_SPD == enemy_SPD:
            who_goes_first = random.choice(["player", "enemy"])

            if who_goes_first == "player":
                enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF)
                if enemy_HP <= 0:
                    print(f"You have slain {enemy_name}.")
                    battle = False
                
                else:
                    player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK)
                    if player_HP <= 0:
                        print(f"{player_name} has been slain. Game Over.")
                        battle = False

            elif who_goes_first == "enemy":
                player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK)
                if player_HP <= 0:
                    print(f"{player_name} has been slain. Game Over.")
                    battle = False
                
                else:
                    enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF)
                    if enemy_HP <= 0:
                        print(f"You have slain {enemy_name}.")
                        battle = False
    
    player.set_health(player_HP)

def player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF):
    if player_action == "attack":
        hit = random.randint(1, 5)
        if hit == 1:
            print("You missed.")
        
        else:
            if enemy_action == "defend":
                success = random.randint(1, 4)
                if success == 1:
                    dmg = player_ATK
                    print(f"{enemy_name} failed in defending against your attack and took {dmg} points of damage.")
                    enemy_HP -= dmg
                
                else:
                    dmg = player_ATK - enemy_DEF
                    if dmg <= 0:
                        print(f"{enemy_name} successfully defended against the attack and took 0 points of damage.")

                    else:
                        print(f"{enemy_name} successfully defended against your attack and only took {dmg} points of damage.")
                        enemy_HP -= dmg

            else:
                dmg = player_ATK
                print(f"You hit {enemy_name} for {dmg} points of damage.")
                enemy_HP -= dmg
    
    return enemy_HP

def enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK):
    if enemy_action == "attack":
        hit = random.randint(1, 5)
        if hit == 1:
            print(f"{enemy_name} missed whilst performing an attack.")

        else:
            if player_action == "defend":
                success = random.randint(1, 4)
                if success == 1:
                    dmg = enemy_ATK
                    print(f"You failed in defending against {enemy_name} attack and took {dmg} points of damage.")
                    player_HP - dmg

                else:
                    dmg = enemy_ATK - player_DEF
                    if dmg <= 0:
                        print(f"You successfully defended against the and took 0 points of damage.")
                    
                    else:
                        print(f"You successfully defended against the attack and only took {dmg} points of damage")
                        player_HP -= dmg

            else:
                dmg = enemy_ATK
                print(f"{enemy_name} hit you for {dmg} points of damage.")
                player_HP -= dmg

    return player_HP

def use_item():
    while True:
        item_chosen = input(f"What item do you want to use? {see_inventory_items()} -> ").lower()
        for item in inventory_items:
            if item.name.lower() == item_chosen:
                print(f"You chose {item.name}.")
                item_chosen = item
        
        if item_chosen not in inventory_items:
            print("Invalid input.")
            continue

        item_chosen.use
        break

def see_inventory_items():
    inventory_items_names = []
    for item in inventory_items:
        inventory_items_names.append(item.name)

    return inventory_items_names

def trap():
    trap_message = random.choice(list_trap_messages)
    print(trap_message)
    dmg = random.randint(1, 3)
    print(f"You took {dmg} points of damage.")
    player.health -= dmg

def treasure():
    print("You find a treasure chest! Let's take a look at what's inside.")
    loot()

def loot():
    loot_table = random.choice(["item"]) # ["item", "weapon", "armour"]
    if loot_table == "item":
        loot = random.choice(loot_items)
        print(f"You found a {loot.name}.")
        add_to_items(loot)

    elif loot_table == "weapon":
        loot = random.choice(loot_weapons)
        print(f"You found a {loot.name}.")
        equip()

    elif loot_table == "armour":
        loot = random.choice(loot_armour)
        print(f"You found a {loot.name}.")
        equip()

def add_to_items(loot):
    if len(inventory_items) >= 3:
        print(f"You pockets are full, you'd have to throw something away if you want to keep {loot.name}.")
        while True:
            throw_or_keep = input(f"Do you want to throw something away and keep {loot.name}? [Y/N] -> ").lower()

            if throw_or_keep == "y":
                while True:
                    discard = input(f"What do you want to throw away? {see_inventory_items()} -> ").lower()

                    for item in inventory_items:
                        if item.name.lower() == discard:
                            discard = item

                    if discard not in inventory_items:
                        print("Invalid input.")
                        continue

                    else:
                        inventory_items.remove(discard)
                        inventory_items.append(loot)
                        break
                break

            elif throw_or_keep == "n":
                print(f"You threw away {loot.name}.")
                break

            else:
                print("Invalid input.")
                continue

    else:
        print(f"You put {loot.name} in your pocket.")
        inventory_items.append(loot)

def equip():
    pass

def bonfire():
    while True:
        rest = input("You find yourself in a room with a bonfire. Do you choose to rest here? [Y/N] -> ").lower()
        if rest == "y":
            # something should happen here
            break

        elif rest == "n":
            break

        else:
            print("Invalid input.")

def help():
    clear_screen()
    print("The goal of this game is to kill enemies in order increase your score and get as high of a highscore as possible.\nIf your HP goes below zero you die and lose all of your progress.")

    while True:
        player_input = input('Type "-back" to go back or "-quit" to quit the game. -> ')

        if player_input == "-back":
            return True

        elif player_input == "-quit":
            return False
        
        else:
            print("Invalid input.")
            continue