class Player:
    def __init__(self, name, HP, ATK, DEF, SPD):
        self.name = name
        self.health = HP
        self.max_health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD
        self.level = 1
        self.experience = 0
        self.weapon = None
        self.weapon_stat = [0, 0]
        self.armour = None
        self.armour_stat = [0, 0]

    def set_health(self, new_health):
        self.health = new_health

class Enemy:
    def __init__(self, name, HP, ATK, DEF, SPD, EXP):
        self.name = name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD
        self.experience = EXP

class Item:
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

'''
Enemy creation with the use of the Enemy class and defining attributes for each unique enemy.

enemy = Enemy(name, health, attack, defence, speed, experience)
'''

slime = Enemy("Slime", 3, 1, 0, 10, 55)
goblin = Enemy("Goblin", 6, 1, 0, 8, 75)
skeleton = Enemy("Skeleton", 8, 1, 1, 8, 65)
gnome = Enemy("Gnome", 4, 1, 0, 12, 85)

list_of_enemies = [slime, goblin, skeleton, gnome]

'''
Item creation with the use of the Item class and defining attributes for each unique item.

item = Item(name, description, use)
'''

# Items (item = Item(name, description, value))
health_potion = Item("Health Potion", "A flask filled with a bright red liquid. Use it to heal your wounds.", 5)
rock = Item("Rock", "You can throw it at your foes.", 3)
smoke_bomb = Item("Smoke Bomb", "Can get you out of trouble in a pinch.", None)
loot_items = [health_potion, rock, smoke_bomb]

# Weapons (weapon = Item(name, description, [attack, speed]))
wooden_club = Item("Wooden Club", "It reeks of troll.", [3, -1])
iron_sword = Item("Iron Sword", "A common weapon amongst travelers.", [2, 0])
steel_dagger = Item("Steel Dagger", "An assassin's best friend.", [1, 2])
elven_bow = Item("Elven Bow", "Smithed by the wise elves.", [2, 2])
orc_mace = Item("Orc Mace", "Orcs have a knack for forging deadly weapons.", [4, -2])
loot_weapons = [wooden_club, iron_sword, steel_dagger, elven_bow, orc_mace]

# Armour (armour = Item(name, description, [defence, speed]))
leather_garments = Item("Leather Garments", "A light set commonly worn by thieves.", [1, 0])
iron_armour = Item("Iron Armour", "The most common set of armour worn throughout the lands.", [2, -2])
loot_armour = [leather_garments, iron_armour]

inventory_items = []