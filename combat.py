from main import *

def player_attack(player_action, player_ATK, enemy_action, enemy_name, enemy_HP, enemy_DEF):
    if player_action in ["attack", "1"]:
        hit = random.randint(1, 5)
        if hit == 1:
            helper.typing("You missed.")
        
        else:
            if enemy_action == "defend":
                success = random.randint(1, 4)
                if success == 1:
                    dmg = player_ATK
                    helper.typing(f"The {enemy_name} failed in defending against your attack and took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                    enemy_HP -= dmg
                
                else:
                    dmg = player_ATK - enemy_DEF
                    if dmg <= 0:
                        helper.typing(f"The {enemy_name} successfully defended against your attack and took 0 points of damage.")

                    else:
                        helper.typing(f"The {enemy_name} successfully defended against your attack and only took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                        enemy_HP -= dmg

            else:
                dmg = player_ATK
                helper.typing(f"You hit the {enemy_name} for {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                enemy_HP -= dmg

    return enemy_HP

def enemy_attack(player_action, player_HP, player_DEF, enemy_action, enemy_name, enemy_ATK):
    if enemy_action == "attack":
        hit = random.randint(1, 5)
        if hit == 1:
            helper.typing(f"The {enemy_name} missed whilst performing an attack.")

        else:
            if player_action in ["defend", "2"]:
                success = random.randint(1, 4)
                if success == 1:
                    dmg = enemy_ATK
                    helper.typing(f"You failed in defending against the {enemy_name} attack and took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                    player_HP - dmg

                else:
                    dmg = enemy_ATK - player_DEF
                    if dmg <= 0:
                        helper.typing(f"You successfully defended against the enemy attack and took 0 points of damage.")
                    
                    else:
                        helper.typing(f"You successfully defended against the enemy attack and only took {dmg} point{helper.s_or_no_s(dmg)} of damage.")
                        player_HP -= dmg

            else:
                dmg = enemy_ATK
                helper.typing(f"The {enemy_name} hit you for {dmg} point{helper.s_or_no_s(dmg)} of damage.")
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