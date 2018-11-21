
class CharacterDB:

    def __init__(self):
        self.database = {}

    def addToDB(self, character):
        self.database[character.name] = character

    def isInDB(self, characterName):
        return characterName in self.database

    def removeFromDB(self, characterName):
        if(self.isInDB(characterName)):
            self.database.pop(characterName)
            return True
        else:
            return False

    def updateName(self, characterName, newName):
        char = self.database[characterName]
        char.setName(newName)
        self.database.pop(characterName)
        self.database[newName] = char