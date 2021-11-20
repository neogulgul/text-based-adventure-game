class Player:
    def __init__(self, name, HP, ATK, DEF, SPD):
        self.name = name
        self.health = HP
        self.max_health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD

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
skeleton = Enemy("Skeleton", 5, 1, 1, 6)
gnome = Enemy("Gnome", 4, 1, 0, 12)

list_of_enemies = [slime, goblin, skeleton, gnome]

'''
Item creation with the use of the Item class and defining attributes for each unique item.

item = Item(name, description, use)
'''

health_potion = Item("Health Potion", "A potion flask filled with a bright red liquid. Used to heal your wounds.", None) # will be able to heal the player
rock = Item("Rock", "You can throw it at your foes.", None) # will be able to be thrown at the enemy
loot_items = [health_potion, rock]

# weapons
loot_weapons = []

# armour
loot_armour = []

inventory_items = []