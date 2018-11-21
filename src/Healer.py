from src.Character import Character


class Healer(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 10)
        Character.setMaxDamae(self, 4)
        Character.setMinDamage(self, 1)
        Character.setMaxHeal(self, 10)
        Character.setMinHeal(self, 5)

    # TODO
    def levelUp(self):
        return