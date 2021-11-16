class Player:
    def __init__(self, Name, HP, ATK, DEF, SPD, LVL, INV):
        self.name = Name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD
        self.level = LVL
        self.inventory = INV

class Enemy:
    def __init__(self, Name, HP, ATK, DEF, SPD):
        self.name = Name
        self.health = HP
        self.attack = ATK
        self.defence = DEF
        self.speed = SPD

class Item:
    def __init__(self, Name, Bonus):
        self.name = Name
        self.bonus = Bonus