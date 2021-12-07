import art

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
rat = Enemy("Rat", 2, 1, 0, 11)

red_slime = Enemy("Red Slime", 6, 2, 0, 10)
goblin = Enemy("Goblin", 7, 2, 1, 8)
skeleton = Enemy("Skeleton", 6, 2, 2, 8)

blue_slime = Enemy("Blue Slime", 9, 3, 0, 10)
golem = Enemy("Golem", 10, 3, 5, 8)
mimic = Enemy("Mimic", 6, 3, 3, 12)

draugr = Enemy("Draugr", 12, 3, 2, 8)
hobgoblin = Enemy("Hobgoblin", 14, 4, 2, 9)
phoenix = Enemy("Phoenix", 10, 3, 1, 15)

baby_dragon = Enemy("Baby Dragon", 15, 4, 1, 10)
troll = Enemy("Troll", 18, 4, 4, 7)
wraith = Enemy("Wraith", 12, 4, 0, 14)


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

ogre = Boss("Ogre", 35, 3, 6, ogre_hammer, art.OGRE) # First Boss (after player reaches lvl 5)
dragon = Boss("Dragon", 75, 5, 15, dragonscale_armour, art.DRAGON) # Last Boss (after player reaches lvl 10)

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
iron_dagger = Item("Iron Dagger", "Makes stabbing feel great.", [1, 1])
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

inventory_items = [] # The player's inventory of usable items