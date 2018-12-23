

class LivingEntity:

    def __init__(self):
        self.alive = True
        self.weapons = {}
        self.weapons_used = {}
        self.hands = 2
        self.bravery = 10
        self.scared = False
        self.poisoned = False
        self.stunned = False

    def pick_up_weapon(self, weapon):
        self.weapons[weapon.name] = weapon

    def assign_weapon(self, weapon):
        if weapon.hands <= self.hands:
            self.weapons_used[weapon.name] = weapon
