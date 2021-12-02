from main import *

def add_to_items(loot):
    if len(inventory_items) >= 3:
        helper.typing(f"Your pockets are full, you would have to throw something away if you want to keep the {loot.name}.")
        while True:
            helper.clear_screen()
            throw_or_keep = input(f"Do you want to throw something away and keep the {loot.name}? [Y/N] -> ").lower()

            if throw_or_keep == "y":
                while True:
                    helper.clear_screen()
                    discard = input(f'What do you want to throw away? {combat.see_inventory_items()} (Type "back" to go back) -> ').lower()
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