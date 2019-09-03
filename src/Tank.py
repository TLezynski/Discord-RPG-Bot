from src.Character import Character


class Tank(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 30)
        Character.heal(self, self.getMaxHP())
        Character.setMaxDamage(self, 4)
        Character.setMinDamage(self, 1)
        Character.setRole(self, "Tank")

    def levelUp(self):
        minDamage = Character.getMinDamage(self)
        maxDamage = Character.getMaxDamage(self)
        maxHP = Character.getMaxHP(self)
        level = Character.getLevel(self)

        Character.setMinDamage(self, minDamage + 1)
        Character.setMaxDamage(self, maxDamage + 2)
        Character.setMaxHP(self, maxHP + (2 * level))