from src.Character import Character


class Wizard(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        self.max_damage = 10
        self.min_damage = 5
        Character.setMaxHP(self, 15)
