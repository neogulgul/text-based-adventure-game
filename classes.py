class Player:
    def __init__(self, name, HP, ATK, DEF, SPD, weapon, weapon_stat, armour, armour_stat):
        self.name = name
        self.health = HP
        self.max_health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD
        self.weapon = weapon
        self.weapon_stat = weapon_stat
        self.armour = armour
        self.armour_stat = armour_stat

    def set_health(self, new_health):
        self.health = new_health
    def set_max_health(self, new_max_health):
        self.max_health = new_max_health
    def set_attack(self, new_attack):
        self.attack = new_attack
    def set_defence(self, new_defence):
        self.defence = new_defence
    def set_speed(self, new_speed):
        self.speed = new_speed

class Enemy:
    def __init__(self, name, HP, ATK, DEF, SPD):
        self.name = name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD

class Item:
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

'''
Enemy creation with the use of the Enemy class and defining attributes for each unique enemy.

enemy = Enemy(name, health, attack, defence, speed)
'''

slime = Enemy("Slime", 3, 1, 0, 10)
goblin = Enemy("Goblin", 6, 1, 0, 8)
skeleton = Enemy("Skeleton", 5, 1, 1, 8)
gnome = Enemy("Gnome", 4, 1, 0, 12)

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