class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.max_hp = 0
        self.curr_hp = 0

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getXP(self):
        return self.xp

    def setMaxHP(self, n):
        self.max_hp = n

    def heal(self, n):
        if(self.curr_hp + n > self.max_hp):
            self.curr_hp = self.max_hp
        else:
            self.curr_hp += n

    def goingToLevelUp(self, n):
        if(self.xp + n > 1000*self.level):
            return True
        else:
            return False

    def addXP(self, n):
        if(self.goingToLevelUp(self, n)):
            self.level += 1
        else:
            self.xp += n
