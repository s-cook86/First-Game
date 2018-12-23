from .living_entity import LivingEntity


class Human(LivingEntity):

    def __init__(self, citerzenship, strength):
        super().__init__()
        self.citerzenship = citerzenship
        self.strength = strength

    def produce_papers(self, level_of_clearance):
        """
        to be fired if asked to produce papers in the city
        :param level_of_clearance: 0-100 depending on importance/ quests achieved
        :return: True is passed, False is failed
        """
        if level_of_clearance > self.citerzenship:
            return False
        else:
            return True
