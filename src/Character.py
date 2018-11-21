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
        # Getter for the name
        return self.name

    def getLevel(self):
        # Getter for the level
        return self.level

    def getXP(self):
        # Getter for the xp
        return self.xp

    def getMaxHP(self):
        # Getter for the Max HP
        return self.max_hp

    def getCurrHP(self):
        # Getter for the Current HP
        return self.curr_hp

    def setMaxHP(self, n):
        # Setter for Max HP
        self.max_hp = n

    def goingToLevelUp(self, n):
        # Function that returns true or false if you're going to level up
        # based on amount of xp you are gaining

        # If you're already level 10 you can't level up
        if(self.level == 10):
            return False

        # Get the value for the next level from the dictionary
        next_level_xp = levels[self.level + 1]
        tmp = n
        lvls_gained = 0

        # While the xp you're gaining + your current xp is greater than or equal to
        # the xp required to level up, subtract the next level's xp, and add a level gained
        while((tmp + self.xp) >= next_level_xp):
            tmp -= next_level_xp
            lvls_gained += 1
            if(self.level + lvls_gained >= 10):
                break
            else:
                next_level_xp = levels[self.level + lvls_gained + 1]

        # if we've gained levels, add the levels we've gained
        if(lvls_gained > 0):
            return True, lvls_gained
        else:
            return False, lvls_gained

    def addXP(self, n):
        # Add XP and level up if needed
        lvls_gained = self.goingToLevelUp(n)[1]
        self.level += lvls_gained
        self.xp += n

    def setHP(self, n):
        # Set the max HP and current HP to n
        self.max_hp = n
        self.curr_hp = n

    def takeDamage(self, n):
        # Subtract n from the current HP
        self.curr_hp -= n

    def heal(self, n):
        # Add n to the current hp, limited by the max
        if(n + self.curr_hp > self.max_hp):
            self.curr_hp = self.max_hp
        else:
            self.curr_hp += n

if __name__ == "__main__":
    tim = Character("Tim")
    tim.addXP(50)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())

    print('Adding 250 xp')
    tim.addXP(250)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())

    print('Adding 800 xp')
    tim.addXP(800)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())

    print('Adding 100 xp')
    tim.addXP(100)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())

    print('Adding 1,000,000 xp')
    tim.addXP(1000000)
    print('Tims XP = ', tim.getXP())
    print('Tim is now level: ', tim.getLevel())
