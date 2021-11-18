class Player:
    def __init__(self, Name, HP, ATK, DEF):
        self.name = Name
        self.health = HP
        self.attack = ATK
        self.defence = DEF

    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def get_defence(self):
        return self.defence

    def set_health(self, new_health):
        self.health = new_health
    def set_attack(self, new_attack):
        self.attack = new_attack
    def set_defence(self, new_defence):
        self.defence = new_defence

class Enemy:
    def __init__(self, Name, HP, ATK, DEF):
        self.name = Name
        self.health = HP
        self.attack = ATK
        self.defence = DEF

    def get_health(self):
        return self.health

goblin = Enemy("Goblin", 5, 1, 0)

slime = Enemy("Slime", 2, 1, 0)

enemy_list = [goblin, slime]

#saeghseifjseiof