from .basic import BasicWeapon


class Spear(BasicWeapon):

    def __init__(self):
        super().__init__(name="basic spear", damage=5, hands=2, range=0,
                         ammo=0, cost=20)


class Sword(BasicWeapon):

    def __init__(self):
        super().__init__(name="basic sword", damage=2, hands=1, range=0,
                         ammo=0, cost=20)

