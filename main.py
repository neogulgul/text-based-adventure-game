import math
import random
import time
from classes import *
import helper
import text

start_time = time.time()

def title_screen():
    helper.clear_screen()
    print(art.TITLE)
    time.sleep(3)

def intro():
    helper.clear_screen()
    helper.typing(f"You are an adventurer on a quest to slay a dragon that has been terrorizing the lands.\nYou have however lost all your equipment to a group of pesky thieves whilst sleeping.\nHowever dire your situation may be you are determined to kill this dragon.")
    time.sleep(3)

def character_creation():
    global player

    while True:
        helper.clear_screen()
        player_name = input("What is your name? -> ")
        if player_name.isalpha() and len(player_name) <= 20:
            while True:
                helper.clear_screen()
                confirmation = input(f"Are you sure you want to be known as {player_name}? [Y/N] -> ").lower()
                if confirmation in ["y", "n"]:
                    break

            if confirmation == "y":
                break

        else:
            print("ERROR: ", end = "", flush = True)
            helper.typing("Only letters from the alphabet are allowed, and no more than 20 characters long.")

    player_health = 10
    player_attack = 1
    player_defence = 0
    player_speed = 10

    player = Player(player_name, player_health, player_attack, player_defence, player_speed)

def adventure():
    while True:
        helper.clear_screen()
        choice = input('What do you want to do? [1. Explore / 2. Inventory] (Type "info" for further information) -> ').lower()

        if choice in ["explore", "1"]:
            if explore():
                continue

            else: # THE PLAYER HAS DIED
                break

        elif choice in ["inventory", "2"]:
            check_inventory()
            continue

        elif choice == "info":
            if info():
                continue

            else: # THE PLAYER CHOSE TO QUIT THE GAME
                break

def explore():
    rooms = [combat, combat, combat, trap, treasure, treasure, bonfire]

    while True:
        helper.clear_screen()
        direction = input("Which way do you go? [1. North / 2. West / 3. East] -> ").lower()

        if direction in ["north", "1"]:
            helper.typing(f"You go north.")
            random.choice(rooms)()
            break

        elif direction in ["west", "2"]:
            helper.typing(f"You go west.")
            random.choice(rooms)()
            break

        elif direction in ["east", "3"]:
            helper.typing(f"You go east.")
            random.choice(rooms)()
            break

    if player.health <= 0:
        helper.typing(f"You have died. Game Over.")
        helper.typing(f"In your playthrough you visited {game_info.room_count} rooms, defeated {game_info.enemy_count} enemies, and reached level {player.level}.")
        return False

    game_info.plus_room_count()
    return True

def check_inventory():
    if player.weapon != None:
        ATK_buff = f"(+{player.weapon_stat[0]} from {player.weapon})"

    else:
        ATK_buff = ""

    if player.armour != None:
        DEF_buff = f"(+{player.armour_stat[0]} from {player.armour})"

    else:
        DEF_buff = ""

    if player.weapon_stat[1] == 0 and player.armour_stat[1] == 0:
        SPD_buff = ""

    else:
        if player.weapon_stat[1] != 0 and player.armour_stat[1] == 0:
            if player.weapon_stat[1] > 0:
                SPD_buff = f"(+{player.weapon_stat[1]} from {player.weapon})"

            else:
                SPD_buff = f"({player.weapon_stat[1]} from {player.weapon})"

        elif player.weapon_stat[1] == 0 and player.armour_stat[1] != 0:
            if player.armour_stat[1] > 0:
                SPD_buff = f"(+{player.armour_stat[1]} from {player.armour})"

            else:
                SPD_buff = f"({player.armour_stat[1]} from {player.armour})"

        else:
            if player.weapon_stat[1] + player.armour_stat[1] > 0:
                SPD_buff = f"(+{player.weapon_stat[1] + player.armour_stat[1]} from {player.weapon} and {player.armour})"

            else:
                SPD_buff = f"({player.weapon_stat[1] + player.armour_stat[1]} from {player.weapon} and {player.armour})"

    level_up_exp = player.level * 100
    if player.level == 10:
        player.experience = "MAX"
        level_up_exp = "MAX"

    if len(inventory_items) == 3:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, inventory_items[1].name, inventory_items[2].name

    elif len(inventory_items) == 2:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, inventory_items[1].name, None

    elif len(inventory_items) == 1:
        item_slot_1, item_slot_2, item_slot_3 = inventory_items[0].name, None, None

    else:
        item_slot_1, item_slot_2, item_slot_3 = None, None, None

    while True:
        helper.clear_screen()

        print(f'''
    {player.name}'s Stats & Inventory
    {"‾" * (len(player.name) + len("'s Stats & Inventory"))}
    Name: {player.name}
    LV: {player.level}
    EXP: {player.experience}/{level_up_exp}
    HP: {player.health}/{player.max_health}
    ATK: {player.attack + player.weapon_stat[0]} {ATK_buff}
    DEF: {player.defence + player.armour_stat[0]} {DEF_buff}
    SPD: {player.speed + player.weapon_stat[1] + player.armour_stat[1]} {SPD_buff}

    Weapon: {player.weapon}
    Armour: {player.armour}
    Item slot 1: {item_slot_1}
    Item slot 2: {item_slot_2}
    Item slot 3: {item_slot_3}
''')

        player_input = input('Type "back" to go back. -> ').lower()

        if player_input == "back":
            break

def info():
    while True:
        helper.clear_screen()

        play_time = math.floor(time.time() - start_time)

        if play_time >= 3600:
            hours = math.floor(play_time / 3600)
            minutes = math.floor(play_time / 60) - hours * 60
            seconds = math.floor(play_time) - hours * 3600 - minutes * 60
            play_time = f"{hours} h {minutes} min {seconds} sec"

        elif play_time >= 60:
            minutes = math.floor(play_time / 60)
            seconds = math.floor(play_time) - minutes * 60
            play_time = f"{minutes} min {seconds} sec"

        else:
            play_time = f"{play_time} sec"

        boss_1 = "???: ALIVE"
        boss_2 = "???: ALIVE"

        if ogre.alive == False:
            boss_1 = "Ogre: DEAD"

        if dragon.alive == False:
            boss_2 = "Dragon: DEAD"

        print(f'''The goal of this game is to kill a dragon that has been terrorizing the lands.
If your HP goes below zero you die and lose all of your progress.

If you are wondering what some of the stats mean, here is a list of them all.

    • LV (Level) - After leveling up you get to choose one stat of yours to increase. Your health is also restored to full.

    • EXP (Experience Points) - Your character's experience points determine how close you are to leveling up.

    • HP (Hit Points) - The amount of hit points, or health, your character has.

    • ATK (Attack) - This stat determines how much damage you do.
    Can be influenced by weapons.

    • DEF (Defence) - This stat determines how well you can defend against enemy attacks.
    Can be influenced by armour.

    • SPD (Speed) - This stat determines who goes first in battle, you or your opponent, depending on who has the higher speed stat.
    If you both have an equal speed stat, then it is random who goes first.
    Can be influenced by both weapons and armour.

Rooms Visited: {game_info.room_count}
Enemies Defeated: {game_info.enemy_count}
Play Time: {play_time}

Bosses:
‾‾‾‾‾‾‾
{boss_1}
{boss_2}

PRO TIP: It is faster to type only the number in front of a given input (if it has one) instead of the whole word.
''')

        player_input = input('Type "back" to go back or "quit" to quit the game. -> ').lower()

        if player_input == "back":
            return True

        elif player_input == "quit":
            return False

def combat():
    battle = True

    player_HP = player.health
    player_ATK = player.attack + player.weapon_stat[0]
    player_DEF = player.defence + player.armour_stat[0]
    player_SPD = player.speed + player.weapon_stat[1] + player.armour_stat[1]

    if player.level == 5 and ogre.alive == True:
        enemy = ogre

    elif player.level == 10 and dragon.alive == True:
        enemy = dragon

    else:
        if player.level > 8:
            enemy = random.choice(enemies_list_4)

        elif player.level > 6:
            enemy = random.choice(enemies_list_3)

        elif player.level > 4:
            enemy = random.choice(enemies_list_2)

        elif player.level > 2:
            enemy = random.choice(enemies_list_1)

        else:
            enemy = random.choice(enemies_list_0)

        enemy_SPD = enemy.speed

    enemy_HP = enemy.health
    enemy_max_HP = enemy.health
    enemy_ATK = enemy.attack
    enemy_DEF = enemy.defence

    if enemy == ogre:
        helper.typing("You encounter a fat Ogre wandering about.")

    elif enemy == dragon:
        helper.typing("You encounter the Dragon!")

    else:
        if enemy == mimic:
            helper.typing("You find a treasure chest! Let us take a look... wait. Wah! *The treasure chest lunges towards you.*")
        helper.typing(f"You encounter {helper.a_or_an(enemy.name)} {enemy.name}.")

    while battle:
        helper.clear_screen()

        print(f"{player.name} HP: {player_HP}/{player.max_health}\n{enemy.name} HP: {enemy_HP}/{enemy_max_HP}")

        if type(enemy) == Boss:
            print(enemy.art)

        if enemy_DEF == 0:
            enemy_action = "attack"

        else:
            enemy_action = random.choice(["attack", "attack", "attack", "defend"])

        player_action = input("What do you choose to do? [1. Attack / 2. Defend / 3. Item] -> ").lower()

        if player_action not in ["attack", "defend", "item", "1", "2", "3"]:
            continue

        elif player_action in ["defend", "2"] and player_DEF == 0:
            helper.typing("You have 0 defence and therefore can not defend.")
            continue

        elif player_action in ["item", "3"]:
            if len(inventory_items) == 0:
                helper.typing("You have no items.")
                continue

            else:
                while True:
                    helper.clear_screen()
                    item_chosen = input(f'What item do you want to use? {see_inventory_items()} (Type "back" to go back) -> ').lower()
                    if item_chosen == "back":
                        break

                    for item in inventory_items:
                        if item.name.lower() == item_chosen:
                            item_chosen = item

                    if item_chosen == "3" and len(inventory_items) == 3:
                        item_chosen = inventory_items[2]

                    elif item_chosen == "2" and len(inventory_items) >= 2:
                        item_chosen = inventory_items[1]

                    elif item_chosen == "1":
                        item_chosen = inventory_items[0]

                    if item_chosen not in inventory_items:
                        continue

                    if item_chosen in [lesser_health_potion, health_potion, plentiful_health_potion]:
                        player_HP += item_chosen.use
                        if player_HP > player.max_health:
                            player_HP = player.max_health
                        helper.typing(f"You used up your {item_chosen.name} and gained {item_chosen.use} HP. {player.name} HP: {player_HP}/{player.max_health}")

                    elif item_chosen == pebble or item_chosen == rock or item_chosen == mage_scroll:
                        enemy_HP -= item_chosen.use

                        if item_chosen == pebble or item_chosen == rock:
                            helper.typing(f"You threw your {item_chosen.name} at the enemy. The {enemy.name} took {item_chosen.use} points of damage.")

                        else:
                            spell = random.choice(["Fireball", "Ice Spike", "Lightning Bolt"])
                            helper.typing(f"You used up your mage scroll and the {enemy.name} was struck by {helper.a_or_an(spell)} {spell}. The {enemy.name} took {item_chosen.use} points of damage.")

                        if enemy_HP <= 0:
                            battle = False

                    elif item_chosen == smoke_bomb:
                        if type(enemy) == Boss:
                            helper.typing("You can not use this item whilst fighting a Boss.")
                            continue

                        helper.typing("You throw the smoke bomb on the ground and flee from battle.")
                        battle = False

                    inventory_items.remove(item_chosen)
                    break

                if item_chosen == "back":
                    continue

        if battle == False:
            break

        if player_action in ["defend", "2"] and enemy_action == "defend":
            helper.typing("You both chose to defend and nothing happened.")
            continue

        if player_action in ["defend", "2"]:
            helper.typing("You chose to defend.")

        if enemy_action == "defend":
            helper.typing(f"The {enemy.name} chose to defend.")

        if type(enemy) == Boss or player_SPD > enemy_SPD:
            enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy.name, enemy_HP, enemy_DEF)
            if enemy_HP <= 0:
                battle = False

            else:
                player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy.name, enemy_ATK)
                if player_HP <= 0:
                    battle = False

        elif player_SPD < enemy_SPD:
            player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy.name, enemy_ATK)
            if player_HP <= 0:
                battle = False

            else:
                enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy.name, enemy_HP, enemy_DEF)
                if enemy_HP <= 0:
                    battle = False

        elif player_SPD == enemy_SPD:
            who_goes_first = random.choice(["player", "enemy"])

            if who_goes_first == "player":
                enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy.name, enemy_HP, enemy_DEF)
                if enemy_HP <= 0:
                    battle = False

                else:
                    player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy.name, enemy_ATK)
                    if player_HP <= 0:
                        battle = False

            elif who_goes_first == "enemy":
                player_HP = enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy.name, enemy_ATK)
                if player_HP <= 0:
                    battle = False

                else:
                    enemy_HP = player_attack(player_action, player_ATK, enemy_action, enemy.name, enemy_HP, enemy_DEF)
                    if enemy_HP <= 0:
                        battle = False

    if player_HP <= 0:
        helper.typing(f"{player.name} has been slain by the {enemy.name}.")

    elif enemy_HP <= 0:
        game_info.plus_enemy_count()
        helper.typing(f"You have slain the {enemy.name}.")

        if type(enemy) == Boss:
            enemy.alive = False
            loot = enemy.drop
            helper.typing(f"The {enemy.name} dropped {loot.name}. {loot.description}")
            equip(loot)

            if enemy == dragon:
                helper.typing("With the dragon now defeated peace will slowly start to return to the lands. However, there will still be enemies left for you to defeat.")
                helper.clear_screen()
                helper.typing("The game is now pretty much over. Thank you for playing! :-)")

        elif type(enemy) != Boss and player.level != 10:
            level_up_exp = player.level * 100
            helper.typing(f"You gain {round(level_up_exp / 2)} experience points.")
            player.experience += round(level_up_exp / 2)
            if player.experience >= level_up_exp:
                player.experience -= level_up_exp
                player.level += 1
                helper.typing(f"You leveled up! You are now level {player.level}.")
                level_up()
                player_HP = player.max_health

    player.set_health(player_HP)

def player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF):
    if player_action in ["attack", "1"]:
        hit = random.randint(1, 10)
        if hit <= 2:
            helper.typing("You missed.")

        else:
            crit = ""
            dmg = player_ATK
            if hit == 10:
                crit = "A critical hit! "
                dmg = player_ATK * 2

            if enemy_action == "defend":
                success = random.randint(1, 4)
                if success == 1:
                    helper.typing(f"{crit}The {enemy_name} failed in defending against your attack and took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                    enemy_HP -= dmg

                else: # If the enemy successfully defends then the player can not deal critical damage
                    dmg = player_ATK - enemy_DEF
                    if dmg <= 0:
                        helper.typing(f"The {enemy_name} successfully defended against your attack and took 0 points of damage.")

                    else:
                        helper.typing(f"The {enemy_name} successfully defended against your attack and only took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                        enemy_HP -= dmg

            else:
                helper.typing(f"{crit}You hit the {enemy_name} for {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                enemy_HP -= dmg

    return enemy_HP

def enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK):
    if enemy_action == "attack":
        hit = random.randint(1, 10)
        if hit <= 2:
            helper.typing(f"The {enemy_name} missed whilst performing an attack.")

        else:
            crit = ""
            dmg = enemy_ATK
            if hit == 10:
                crit = "A critical hit! "
                dmg = enemy_ATK * 2

            if player_action in ["defend", "2"]:
                success = random.randint(1, 4)
                if success == 1:
                    helper.typing(f"{crit}You failed in defending against the {enemy_name} attack and took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                    player_HP - dmg

                else: # If the player successfully defends then the enemy can not deal critical damage
                    dmg = enemy_ATK - player_DEF
                    if dmg <= 0:
                        helper.typing(f"You successfully defended against the enemy attack and took 0 points of damage.")

                    else:
                        helper.typing(f"You successfully defended against the enemy attack and only took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                        player_HP -= dmg

            else:
                helper.typing(f"{crit}The {enemy_name} hit you for {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                player_HP -= dmg

    return player_HP

def see_inventory_items():
    see_inventory_items = []
    for item in inventory_items:
        see_inventory_items.append(item.name)

    if len(see_inventory_items) == 3:
        see_inventory_items = f"[1. {see_inventory_items[0]} / 2. {see_inventory_items[1]} / 3. {see_inventory_items[2]}]"

    elif len(see_inventory_items) == 2:
        see_inventory_items = f"[1. {see_inventory_items[0]} / 2. {see_inventory_items[1]}]"

    else:
        see_inventory_items = f"[1. {see_inventory_items[0]}]"

    return see_inventory_items

def level_up():
    while True:
        helper.clear_screen()

        print(f'''You get to choose one stat of yours to increase.

    HP: {player.health}/{player.max_health}
    ATK: {player.attack}
    DEF: {player.defence}
    SPD: {player.speed}
''')

        attribute = input(f"Which attribute do you want to increase? [1. HP / 2. ATK / 3. DEF / 4. SPD] -> ").upper()

        if attribute in ["HP", "1"]:
            player.max_health += 5
            helper.typing("Your max HP increased by 5 points.")
            break

        elif attribute in ["ATK", "2"]:
            player.attack += 1
            helper.typing("Your ATK increased by 1 point.")
            break

        elif attribute in ["DEF", "3"]:
            player.defence += 1
            helper.typing("Your DEF increased by 1 point.")
            break

        elif attribute in ["SPD", "4"]:
            player.speed += 1
            helper.typing("Your SPD increased by 1 point.")
            break

def trap():
    helper.clear_screen()
    helper.typing(random.choice(text.trap_messages))
    dmg = random.randint(1, 2)
    player.health -= dmg
    helper.typing(f"You take {dmg} point{helper.s_or_no_s(dmg)} of damage.")

def treasure():
    helper.typing("You find a treasure chest! Let us take a look at what is inside.")
    helper.clear_screen()

    if player.level > 8:
        loot = random.choice(loot_pool_4)

    elif player.level > 6:
        loot = random.choice(loot_pool_3)

    elif player.level > 4:
        loot = random.choice(loot_pool_2)

    elif player.level > 2:
        loot = random.choice(loot_pool_1)

    else:
        loot = random.choice(loot_pool_0)

    if loot in loot_items:
        helper.typing(f"You found {helper.a_or_an(loot.name)} {loot.name}. {loot.description}")
        add_to_items(loot)

    elif loot in loot_weapons:
        helper.typing(f"You found {helper.a_or_an(loot.name)} {loot.name}. {loot.description}")
        equip(loot)

    elif loot in loot_armour:
        helper.typing(f"You found {loot.name}. {loot.description}")
        equip(loot)

def add_to_items(loot):
    if len(inventory_items) >= 3:
        helper.typing(f"Your pockets are full, you would have to throw something away if you want to keep the {loot.name}.")
        while True:
            helper.clear_screen()
            throw_or_keep = input(f"Do you want to throw something away and keep the {loot.name}? [Y/N] -> ").lower()

            if throw_or_keep == "y":
                while True:
                    helper.clear_screen()
                    discard = input(f'What do you want to throw away? {see_inventory_items()} (Type "back" to go back) -> ').lower()
                    if discard == "back":
                        break

                    for item in inventory_items:
                        if item.name.lower() == discard:
                            discard = item

                    if discard == "3" and len(inventory_items) == 3:
                        discard = inventory_items[2]

                    elif discard == "2" and len(inventory_items) >= 2:
                        discard = inventory_items[1]

                    elif discard == "1":
                        discard = inventory_items[0]

                    if discard in inventory_items:
                        helper.typing(f"You threw away your {discard.name} and kept the {loot.name}.")
                        inventory_items.remove(discard)
                        inventory_items.append(loot)
                        break

                if discard == "back":
                    continue

                break

            elif throw_or_keep == "n":
                helper.typing(f"You threw away the {loot.name}.")
                break

    else:
        helper.typing(f"You put the {loot.name} in your pocket.")
        inventory_items.append(loot)

def equip(loot):
    if loot in loot_weapons:
        if player.weapon == None:
            player.weapon = loot.name
            player.weapon_stat = loot.use
            helper.typing(f"You equip the {loot.name}.")

        else:
            if player.weapon == loot.name:
                helper.typing(f"You already have {helper.a_or_an(loot.name)} {loot.name} equipped, so you decide to leave it behind.")

            else:
                while True:
                    helper.clear_screen()
                    change_or_keep = input(f"Do you want to switch from your {player.weapon} [ATK: {player.weapon_stat[0]}, SPD: {player.weapon_stat[1]}] to the {loot.name} [ATK: {loot.use[0]}, SPD: {loot.use[1]}]? [Y/N] -> ").lower()
                    if change_or_keep == "y":
                        helper.typing(f"You decide to leave your {player.weapon} behind and switch to {helper.a_or_an(loot.name)} {loot.name}.")
                        player.weapon = loot.name
                        player.weapon_stat = loot.use
                        break

                    elif change_or_keep == "n":
                        helper.typing(f"You decide to keep your {player.weapon}.")
                        break

    elif loot in loot_armour:
        if player.armour == None:
            player.armour = loot.name
            player.armour_stat = loot.use
            helper.typing(f"You equip the {loot.name}.")

        else:
            if player.armour == loot.name:
                helper.typing(f"You already have {loot.name} equipped, so you decide to leave it behind.")

            else:
                while True:
                    helper.clear_screen()
                    change_or_keep = input(f"Do you want to change from your {player.armour} [DEF: {player.armour_stat[0]}, SPD: {player.armour_stat[1]}] to {loot.name} [DEF: {loot.use[0]}, SPD: {loot.use[1]}]? [Y/N] -> ").lower()
                    if change_or_keep == "y":
                        helper.typing(f"You decide to leave your {player.armour} behind and switch to {loot.name}.")
                        player.armour = loot.name
                        player.armour_stat = loot.use
                        break

                    elif change_or_keep == "n":
                        helper.typing(f"You decide to keep your {player.armour}.")
                        break

def bonfire():
    while True:
        helper.clear_screen()
        rest = input("You find yourself in a room with a bonfire. Do you choose to rest here? [Y/N] -> ").lower()
        if rest == "y":
            if player.health == player.max_health:
                helper.typing("You change your mind. You do not feel like resting at the moment.")
                break

            else:
                while True:
                    helper.clear_screen()
                    try:
                        hours = int(input("For how long do you wish to rest? (the amount of hours, between 1-10) -> "))
                    except:
                        continue

                    if hours >= 1 and hours <= 10:
                        for hour in range(hours):
                            if random.randint(1, 100) < (hour + 1) * 5:
                                helper.typing(random.choice(text.disturb_messages))
                                combat()
                                break

                            else:
                                player.health += 1
                                print("+1 HP")
                                time.sleep(0.3)
                                if player.health == player.max_health:
                                    helper.typing("You are now at full HP.")
                                    break
                        break
                break

        elif rest == "n":
            break