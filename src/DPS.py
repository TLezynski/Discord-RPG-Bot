from src.Character import Character


class DPS(Character):

    def __init__(self, name):
        Character.__init__(self, name)
        Character.setMaxHP(self, 15)
        Character.setCurrHP(self, Character.getMaxHP(self))
        Character.setMaxDamage(self, 10)
        Character.setMinDamage(self, 5)
        Character.setRole(self, "DPS")

    def levelUp(self):
        minDamage = Character.getMinDamage(self)
        maxDamage = Character.getMaxDamage(self)
        maxHP = Character.getMaxHP(self)
        level = Character.getLevel(self)

        Character.setMinDamage(self, minDamage + level)
        Character.setMaxDamage(self, maxDamage + level)
        Character.setMaxHP(self, maxHP + 5)