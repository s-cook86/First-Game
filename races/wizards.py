from .living_entity import LivingEntity


class Wizard(LivingEntity):

    def __init__(self, magic, magic_level, regen_amount):
        super().__init__()
        self.magic = magic
        self.magic_level = magic_level
        self.regen_amount = regen_amount

        self.spells = {
            "fire blast": [20, 5],
            "heal": [-20, 10]

        }

    def cast_spell(self, spell, target_hp):
        """
        casts spell which does instant effect but is expensive
        :param spell: type of spell used
        :param target_hp: target character hp
        :return: the result of the target's HP  after the spell
        """
        if spell[1] > self.magic:
            return target_hp
        else:
            self.magic = self.magic - spell[1]
            return target_hp - spell[0]

    def rest(self):
        self.magic += self.regen_amount

"""
This is how you can define a wizard but don't use this as it will be inherited by a character class

player_one = Wizard(magic=50, magic_level=1)

player_one.cast_spell(spell=player_one.spells["fire blast"], target_hp=100)
player_one.rest()
"""
