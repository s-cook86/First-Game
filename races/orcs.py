from .living_entity import LivingEntity


class Orc(LivingEntity):

    def __init__(self, aggression):
        super().__init__()
        self.aggression = aggression

    def induce_fear(self, target):
        if self.aggression >= target.bravery:
            target.scared = True
