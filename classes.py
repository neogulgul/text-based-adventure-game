import art
import helper

class Player:
    def __init__(self, name, role, HP, ATK, DEF, SPD):
        self.name = name
        self.role = role
        self.health = HP
        self.max_health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.weapon = None
        self.weapon_stat = [0, 0]
        self.armour = None
        self.armour_stat = [0, 0]

    def set_health(self, new_health):
        self.health = new_health

    def check_inventory(self):
        ATK_buff = ""
        DEF_buff = ""
        SPD_buff = ""

        if self.weapon != None:
            ATK_buff = f"(+{self.weapon_stat[0]} from {self.weapon})"

        if self.armour != None:
            DEF_buff = f"(+{self.armour_stat[0]} from {self.armour})"

        if self.weapon_stat[1] != 0 and self.armour_stat[1] != 0:
            if self.weapon_stat[1] != 0 and self.armour_stat[1] == 0:
                if self.weapon_stat[1] > 0:
                    SPD_buff = f"(+{self.weapon_stat[1]} from {self.weapon})"

                else:
                    SPD_buff = f"({self.weapon_stat[1]} from {self.weapon})"

            elif self.weapon_stat[1] == 0 and self.armour_stat[1] != 0:
                if self.armour_stat[1] > 0:
                    SPD_buff = f"(+{self.armour_stat[1]} from {self.armour})"

                else:
                    SPD_buff = f"({self.armour_stat[1]} from {self.armour})"

            else:
                if self.weapon_stat[1] + self.armour_stat[1] > 0:
                    SPD_buff = f"(+{self.weapon_stat[1] + self.armour_stat[1]} from {self.weapon} and {self.armour})"

                else:
                    SPD_buff = f"({self.weapon_stat[1] + self.armour_stat[1]} from {self.weapon} and {self.armour})"

        level_up_exp = self.level * 100
        if self.level == 10:
            self.experience = "MAX"
            level_up_exp = "MAX"

        if len(self.inventory) == 3:
            item_slot_1, item_slot_2, item_slot_3 = self.inventory[0].name, self.inventory[1].name, self.inventory[2].name
        elif len(self.inventory) == 2:
            item_slot_1, item_slot_2, item_slot_3 = self.inventory[0].name, self.inventory[1].name, None
        elif len(self.inventory) == 1:
            item_slot_1, item_slot_2, item_slot_3 = self.inventory[0].name, None, None
        else:
            item_slot_1, item_slot_2, item_slot_3 = None, None, None

        while True:
            helper.clear_screen()

            print(f'''
        {self.name} the {self.role} 
        {"‾" * len(f"{self.name} the {self.role}")}
        Name: {self.name}
        LV: {self.level}
        EXP: {self.experience}/{level_up_exp}
        HP: {self.health}/{self.max_health}
        ATK: {self.attack + self.weapon_stat[0]} {ATK_buff}
        DEF: {self.defence + self.armour_stat[0]} {DEF_buff}
        SPD: {self.speed + self.weapon_stat[1] + self.armour_stat[1]} {SPD_buff}

        Weapon: {self.weapon}
        Armour: {self.armour}
        Item slot 1: {item_slot_1}
        Item slot 2: {item_slot_2}
        Item slot 3: {item_slot_3}
    ''')

            player_input = input('Type "back" to go back. -> ').lower()

            if player_input == "back":
                break

def see_player_inventory(self):
        player_inventory = []
        for item in self.inventory:
            player_inventory.append(item.name)

        if len(player_inventory) == 3:
            player_inventory = f"[1. {player_inventory[0]} / 2. {player_inventory[1]} / 3. {player_inventory[2]}]"

        elif len(player_inventory) == 2:
            player_inventory = f"[1. {player_inventory[0]} / 2. {player_inventory[1]}]"

        else:
            player_inventory = f"[1. {player_inventory[0]}]"

        return player_inventory

class Enemy:
    def __init__(self, name, HP, ATK, DEF, SPD):
        self.name = name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD

class Boss:
    def __init__(self, name, HP, ATK, DEF, drop, art):
        self.name = name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.drop = drop
        self.art = art
        self.alive = True

class Item:
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

class Game_Info:
    def __init__(self):
        self.room_count = 0
        self.enemy_count = 0

    def plus_room_count(self):
        self.room_count += 1

    def plus_enemy_count(self):
        self.enemy_count += 1

game_info = Game_Info()

'''
Enemy creation with the use of the Enemy class and defining attributes for each unique enemy.

enemy = Enemy(name, health, attack, defence, speed)
'''
green_slime = Enemy("Green Slime", 3, 1, 0, 10)
gnome = Enemy("Gnome", 2, 1, 0, 12)
rat = Enemy("Rat", 2, 2, 1, 10)

red_slime = Enemy("Red Slime", 6, 2, 0, 10)
goblin = Enemy("Goblin", 7, 3, 2, 9)
skeleton = Enemy("Skeleton", 7, 2, 3, 8)

blue_slime = Enemy("Blue Slime", 9, 3, 0, 10)
golem = Enemy("Golem", 10, 3, 5, 5)
mimic = Enemy("Mimic", 8, 4, 3, 12)

draugr = Enemy("Draugr", 13, 3, 4, 7)
hobgoblin = Enemy("Hobgoblin", 12, 3, 3, 9)
phoenix = Enemy("Phoenix", 10, 4, 1, 14)

baby_dragon = Enemy("Baby Dragon", 15, 3, 3, 10)
troll = Enemy("Troll", 18, 4, 4, 6)
wraith = Enemy("Wraith", 10, 5, 0, 13)


enemies_list_0 = [green_slime, gnome, rat] # player lvl. 1-2
enemies_list_1 = [red_slime, goblin, skeleton] # player lvl. 3-4
enemies_list_2 = [blue_slime, golem, mimic] # player lvl. 5-6
enemies_list_3 = [draugr, hobgoblin, phoenix] # player lvl. 7-8
enemies_list_4 = [baby_dragon, troll, wraith] # player lvl. 9+

'''
Boss creation with the use of the Boss class and defining attrbiutes for each unique boss.

boss = Boss(name, health, attack, defence, item drop, ascii art)
'''
# Boss Drops (special items that can only be dropped by bosses)
ogre_hammer = Item("Ogre Hammer", "A heavy hammer wielded by most ogres.", [5, -3]) # Weapon
dragonscale_armour = Item("Dragonscale Armour", "Crafted with scales from a dragon.", [10, 0]) # Armour

ogre = Boss("Ogre", 30, 3, 6, ogre_hammer, art.OGRE) # First Boss (after player reaches lvl 5)
dragon = Boss("Dragon", 60, 5, 15, dragonscale_armour, art.DRAGON) # Last Boss (after player reaches lvl 10)

'''
Item creation with the use of the Item class and defining attributes for each unique item.

item = Item(name, description, use)
'''
# Items - item = Item(name, description, value)
lesser_health_potion = Item("Lesser Health Potion", "A flask filled with a bright red liquid. Restores 5 HP.", 5)
health_potion = Item("Health Potion", "A flask filled with a bright red liquid. Restores 10 HP.", 10)
plentiful_health_potion = Item("Plentiful Health Potion", "A flask filled with a bright red liquid. Restores 15 HP.", 15)
pebble = Item("Pebble", "You can throw it at your foes.", 3)
rock = Item("Rock", "You can throw it at your foes.", 6)
mage_scroll = Item("Mage Scroll", "You are unable to decipher what is written on the scroll.", 12)
smoke_bomb = Item("Smoke Bomb", "Can get you out of trouble in a pinch.", None)

loot_items = [lesser_health_potion, health_potion, plentiful_health_potion, pebble, rock, mage_scroll, smoke_bomb]

# Weapons - weapon = Item(name, description, [attack, speed])
wooden_sword = Item("Wooden Sword", "Better than a stick.", [1, 0])
iron_sword = Item("Iron Sword", "A common weapon amongst travelers.", [2, 0])
steel_sword = Item("Steel Sword", "Hard and tough, perfect for butchering.", [4, 0])
butter_knife = Item("Butter Knife", "Great for making buttered toast.", [0, 3])
iron_dagger = Item("Iron Dagger", "Makes stabbing great.", [1, 1])
steel_dagger = Item("Steel Dagger", "An assasin's best friend.", [2, 2])
elven_dagger = Item("Elven Dagger", "Smithed by the elves.", [3, 4])
rusty_mace = Item("Rusty Mace", "One mans trash is another mans... weapon?", [2, -2])
troll_club = Item("Troll Club", "It reeks of troll.", [3, -1])
orcish_mace = Item("Orcish Mace", "Orcs are known for their craftsmanship.", [5, -2])
ancient_nordic_shortsword = Item("Ancient Nordic Shortsword", "Do not let its size fool you.", [5, 1])
ancient_nordic_greatsword = Item("Ancient Nordic Greatsword", "Now this, is a big sword.", [7, -3])

loot_weapons = [wooden_sword, iron_sword, steel_sword, butter_knife, iron_dagger, steel_dagger, elven_dagger, rusty_mace, troll_club, orcish_mace, ancient_nordic_shortsword, ancient_nordic_greatsword, ogre_hammer]

# Armour - armour = Item(name, description, [defence, speed])
# "light armour"
hide_armour = Item("Hide Armour", "Looks like deer, smells like deer.", [1, 0])
fur_armour = Item("Fur Armour", "Great against the northern cold.", [2, 0])
leather_armour = Item("Leather Armour", "Tough leathery armour.", [3, 0])
elven_armour = Item("Elven Armour", "A light set of armour that provides great mobility.", [4, 2])
shrouded_armour = Item("Shrouded Armour", "Worn by a notorious group of assasins.", [5, 4])
# "heavy armour"
rusty_armour = Item("Rusty Armour", "This armour has seen better days.", [2, -2])
iron_armour = Item("Iron Armour", "The most common set of armour worn throughout the lands.", [3, -2])
steel_armour = Item("Steel Armour", "The prefered set of armour for knights.", [4, -2])
orcish_armour = Item("Orchish Armour", "Smells like orc.", [6, -3])
ancient_nordic_armour = Item("Ancient Nordic Armour", "This armour set was long thought to be a myth.", [8, -2])

loot_armour = [hide_armour, fur_armour, leather_armour, elven_armour, shrouded_armour, rusty_armour, iron_armour, steel_armour, orcish_armour, ancient_nordic_armour, dragonscale_armour]

# (items, weapons, armour)
loot_pool_0 = [lesser_health_potion, pebble, wooden_sword, iron_dagger, rusty_mace, hide_armour, rusty_armour] # player lvl. 1-2
loot_pool_1 = [lesser_health_potion, rock, iron_sword, troll_club, fur_armour, iron_armour] # player lvl. 3-4
loot_pool_2 = [health_potion, smoke_bomb, steel_sword, steel_dagger, leather_armour, steel_armour] # player lvl. 5-6
loot_pool_3 = [health_potion, smoke_bomb, elven_dagger, orcish_mace, elven_armour, orcish_armour] # player lvl. 7-8
loot_pool_4 = [plentiful_health_potion, smoke_bomb, mage_scroll, ancient_nordic_shortsword, ancient_nordic_greatsword, shrouded_armour, ancient_nordic_armour] # player lvl. 9+