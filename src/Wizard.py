from src.Character import Character


class Wizard(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 15)
        Character.setMaxDamae(self, 10)
        Character.setMinDamage(self, 5)

    # TODO
    def levelUp(self):
        return