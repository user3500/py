class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name = "No name", age = 54):
        self.name = name #attributes
        self.age = age

    def run(self):
        print(f"Hello, my name is {self.name}, I am {self.age}.")



player1 = PlayerCharacter("pog", 12)
player2 = PlayerCharacter()
player1.attack = 50
player1.run()
player2.run()
print(player1.attack)
