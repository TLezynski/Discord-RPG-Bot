from src.Character import Character


class Tank(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 30)
        Character.setMaxDamae(self, 4)
        Character.setMinDamage(self, 1)

    # TODO
    def levelUp(self):
        return