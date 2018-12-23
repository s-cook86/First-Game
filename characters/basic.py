from races.wizards import Wizard
from races.humans import Human
from races.orcs import Orc


class BasicWizard(Wizard):

    def __init__(self, name):
        super().__init__(magic=5, magic_level=1)
        self.name = name
        self.hp = 10
        self.cost = 30


class BasicHumanSoldier(Human):

    def __init__(self, name):
        super().__init__(citerzenship=10, strength=10)
        self.name = name
        self.hp = 20
        self.cost = 20


class BasicHumanSargent(Human):

    def __init__(self, name):
        super().__init__(citerzenship=20, strength=15)
        self.name = name
        self.hp = 30
        self.cost = 50

    def award_medal(self, soldier):
        """
        increases a soldier's citerzenship
        :param soldier: soldier recieving the medal
        :return: altered score
        """
        if soldier.citerzenship < self.citerzenship:
            soldier.citerzenship += 5
        else:
            pass


class BasicOrc(Orc):

    def __init__(self, name):
        super().__init__(aggression=10)
        self.name = name
        self.hp = 20
        self.cost = 20


class BasicOrcSargent(Orc):

    def __init__(self, name):
        super().__init__(aggression=20)
        self.name = name
        self.hp = 30
        self.cost = 50

