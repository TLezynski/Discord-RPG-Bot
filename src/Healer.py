from src.Character import Character


class Healer(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 10)
        Character.setMaxDamage(self, 4)
        Character.setMinDamage(self, 1)
        Character.setMaxHeal(self, 10)
        Character.setMinHeal(self, 5)
        Character.setRole(self, "Healer")

    def levelUp(self):
        minDamage = Character.getMinDamage(self)
        maxDamage = Character.getMaxDamage(self)
        maxHP = Character.getMaxHP(self)
        level = Character.getLevel(self)
        maxHeal = Character.getMaxHeal(self)
        minHeal = Character.getMaxHeal(self)

        Character.setMinDamage(self, minDamage + 1)
        Character.setMaxDamage(self, maxDamage + 1)
        Character.setMaxHP(self, maxHP + 5)
        Character.setMaxHeal(self, maxHeal + level)
        Character.setMinHeal(self, minHeal + level)