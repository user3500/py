class User():
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self. power = power

    def attack(self):
        print(f"Wizard {self.name} attacked with {self.power} power!")

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"Archer {self.name} attacked with {self.arrows} arrows")

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

    def attack(self):
        print(f"Hybrid {self.name} attacked with {self.power} power and {self.arrows} arrows")


merl = Wizard("Mer", 10)
arch = Archer("Matt", 40)
borg = Hybrid("wock", 20, 60)

merl.attack()
arch.attack()
borg.sign_in()
borg.attack()
