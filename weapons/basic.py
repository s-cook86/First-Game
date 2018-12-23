

class BasicWeapon:

    def __init__(self, name, damage, hands, range, ammo, cost):
        self.name = name
        self.damage = damage
        self.hands = hands
        self.range = range
        self.ammo = ammo
        self.cost = cost

    def hand_attack(self, target):
        target.hp -= self.damage

    def ranged_attack(self, distance, target):
        if self.range < distance:
            pass
        else:
            target.hp -= self.damage


"""
This is how you can use the weapons

weapon = BasicWeapon(name="axe", damage=20, hands=2, range=0, ammo=0)

weapon.raged_attack(distance=20, target_hp=100)
weapon.hand_attack(target_hp=100)

"""
