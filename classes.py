from art import *

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

'''
Enemy creation with the use of the Enemy class and defining attributes for each unique enemy.

enemy = Enemy(name, health, attack, defence, speed, experience)
'''
green_slime = Enemy("Green Slime", 3, 1, 0, 10, 50)
gnome = Enemy("Gnome", 2, 1, 0, 12, 50)
goblin = Enemy("Goblin", 6, 2, 1, 9, 100)
skeleton = Enemy("Skeleton", 4, 2, 2, 8, 100)
red_slime = Enemy("Red Slime", 9, 3, 0, 10, 150)
evil_mushroom = Enemy("Evil Mushroom", 11, 3, 1, 6, 150)
treant = Enemy("Treant", 15, 4, 5, 5, 200)
forest_elemental = Enemy("Forest Elemental", 12, 3, 3, 12, 200)
blue_slime = Enemy("Blue Slime", 15, 5, 0, 10, 250)
water_elemental = Enemy("Water Elemental", 12, 4, 4, 12, 250)
draugr = Enemy("Draugr", 15, 5, 3, 9, None)
troll = Enemy("Troll", 20, 5, 5, 7, None)

enemies_list_0 = [green_slime, gnome] # player lvl. 1-2
enemies_list_1 = [goblin, skeleton] # player lvl. 3-4
enemies_list_2 = [red_slime, evil_mushroom] # player lvl. 5-6
enemies_list_3 = [treant, forest_elemental] # player lvl. 7-8
enemies_list_4 = [blue_slime, water_elemental] # player lvl. 9-10
enemies_list_5 = [draugr, troll] # player lvl. 10+

'''
Boss creation with the use of the Boss class and defining attrbiutes for each unique boss.

boss = Boss(name, health, attack, defence, item drop, ascii art)
'''
# Boss Drops (special items that can only be dropped by bosses)
ogre_hammer = Item("Ogre Hammer", "A heavy hammer wielded by ogres.", [5, -3]) # Weapon
dragonscale_armour = Item("Dragonscale Armour", "Crafted with the scales from a dragon.", [10, 0]) # Armour

ogre = Boss("Ogre", 30, 3, 6, ogre_hammer, OGRE) # First Boss (after player reaches lvl 5)
dragon = Boss("Dragon", 80, 5, 20, dragonscale_armour, DRAGON) # Last Boss (after player reaches lvl 10)

'''
Item creation with the use of the Item class and defining attributes for each unique item.

item = Item(name, description, use)
'''
# Items - item = Item(name, description, value)
lesser_health_potion = Item("Lesser Health Potion", "A flask filled with a bright red liquid. Restores 5 HP. ", 5)
health_potion = Item("Health Potion", "A flask filled with a bright red liquid. Restores 10 HP.", 10)
plentiful_health_potion = Item("Plentiful Health Potion", "A flask filled with a bright red liquid. Restores 15 HP.", 15)
pebble = Item("Pebble", "You can throw it at your foes.", 3)
rock = Item("Rock", "You can throw it at your foes.", 6)
mage_scroll = Item("Mage Scroll", "You are unable to decipher what is written on the scroll.", 12)
smoke_bomb = Item("Smoke Bomb", "Can get you out of trouble in a pinch.", None)
godify = Item("Godify", "Makes you a God.", None)

loot_items = [lesser_health_potion, health_potion, plentiful_health_potion, pebble, rock, mage_scroll, smoke_bomb]

# Weapons - weapon = Item(name, description, [attack, speed])
wooden_sword = Item("Wooden Sword", "LOREM IPSUM", [2, 0])
iron_sword = Item("Iron Sword", "A common weapon amongst travelers.", [3, 0])
steel_sword = Item("Steel Sword", "LOREM IPSUM", [4, 0])
iron_dagger = Item("Iron Dagger", "LOREM IPSUM", [1, 1])
steel_dagger = Item("Steel Dagger", "An assasin's best friend.", [3, 2])
elven_dagger = Item("Elven Dagger", "LOREM IPSUM", [3, 4])
rusty_mace = Item("Rusty Mace", "LOREM IPSUM", [3, -1])
troll_club = Item("Troll Club", "It reeks of troll.", [4, -1])
orcish_mace = Item("Orcish Mace", "Orcs are known for their craftsmanship.", [6, -2])
ancient_nordic_shortsword = Item("Ancient Nordic Shortsword", "LOREM IPSUM", [5, 2])
ancient_nordic_greatsword = Item("Ancient Nordic Greatsword", "LOREM IPSUM", [8, -1])

loot_weapons = [wooden_sword, iron_sword, steel_sword, iron_dagger, steel_dagger, elven_dagger, rusty_mace, troll_club, orcish_mace, ancient_nordic_shortsword, ancient_nordic_greatsword, ogre_hammer]

# Armour - armour = Item(name, description, [defence, speed])
# "light armour"
hide_armour = Item("Hide Armour", "LOREM IPSUM", [1, 0])
fur_armour = Item("Fur Armour", "LOREM IPSUM", [2, 0])
leather_armour = Item("Leather Armour", "LOREM IPSUM", [3, 0])
elven_armour = Item("Elven Armour", "LOREM IPSUM", [4, 3])
shrouded_armour = Item("Shrouded Armour", "LOREM IPSUM", [5, 4])
# "heavy armour"
rusty_armour = Item("Rusty Armour", "LOREM IPSUM", [2, -2])
iron_armour = Item("Iron Armour", "The most common set of armour worn throughout the lands.", [4, -2])
chitin_armour = Item("Chitin Armour", "LOREM IPSUM", [5, -1])
orcish_armour = Item("Orchish Armour", "LOREM IPSUM", [6, -3])
ancient_nordic_armour = Item("Ancient Nordic Armour", "LOREM IPSUM", [8, -2])

loot_armour = [hide_armour, fur_armour, leather_armour, elven_armour, shrouded_armour, rusty_armour, iron_armour, chitin_armour, orcish_armour, ancient_nordic_armour, dragonscale_armour]

# (items, weapons, armour)
loot_pool_0 = [lesser_health_potion, pebble, wooden_sword, iron_dagger, rusty_mace, hide_armour, rusty_armour] # player lvl. 1-2
loot_pool_1 = [lesser_health_potion, rock, smoke_bomb, iron_sword, troll_club, fur_armour, iron_armour] # player lvl. 3-4
loot_pool_2 = [health_potion, rock, smoke_bomb, steel_sword, steel_dagger, leather_armour, chitin_armour] # player lvl. 5-6
loot_pool_3 = [health_potion, smoke_bomb, elven_dagger, orcish_mace, elven_armour, orcish_armour] # player lvl. 7-8
loot_pool_4 = [plentiful_health_potion, smoke_bomb, mage_scroll, ancient_nordic_shortsword, ancient_nordic_greatsword, shrouded_armour, ancient_nordic_armour] # player lvl. 9-10
loot_pool_5 = [godify] # player lvl. 10+

inventory_items = [] # This list represents the player's inventory of usable items