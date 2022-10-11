class Animal:
    def __init__(self) -> None:
        self.type = "sss"
        self.sound = ""
    def setName(self, type):
        self.type = type
    def setSound(self, sound):
        self.sound = sound
    def printSound(self):
        print(self.sound)

    
        