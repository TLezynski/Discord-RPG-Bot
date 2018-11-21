from src.Character import Character


class Wizard(Character):

    def __init__(self, name):
        Character.__init__(self, name)

        Character.setMaxHP(self, 15)
        Character.set