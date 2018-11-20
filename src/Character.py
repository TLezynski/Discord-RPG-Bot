levels = {1:0, 2:300, 3:600, 4:1200, 5:2400, 6:4800,
          7:9600, 8:19200, 9:38400, 10:76800}

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
        if(self.level == 10):
            return False

        next_level_xp = levels[self.level + 1]
        tmp = n
        lvls_gained = 0
        while((tmp + self.xp) - next_level_xp >= 0):
            tmp -= next_level_xp
            if(self.level + lvls_gained >= 10):
                break
            else:
                lvls_gained += 1
                next_level_xp = levels[self.level + lvls_gained + 1]

        if(lvls_gained > 0):
            self.level += lvls_gained
            return True
        else:
            return False

    def addXP(self, n):
        self.goingToLevelUp(n)
        self.xp += n

if __name__ == "__main__":
    tim = Character("time")
    tim.addXP(50)
    print('Tims XP = ', tim.getXP())
    print('Adding 250 xp')
    tim.addXP(250)
    print('Tims XP = ', tim.getXP())
    print('Adding 800 xp')
    tim.addXP(800)
    print('Tims XP = ', tim.getXP())
    print('Adding 100 xp')
    tim.addXP(100)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())

