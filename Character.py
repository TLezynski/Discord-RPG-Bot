class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getXP(self):
        return self.xp

    def addXP(self, n):
        self.xp += n