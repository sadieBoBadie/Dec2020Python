# NEW EXCITING CLASS!!!!!
class Sword:
    def __init__(self, swordType):
        self.integrity = 50
        self.type = swordType

class Ninja:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.sword = None # NEW ATTRIBUTE!! 

    def displayStats(self):
        print("Name: ", self.name)
        print("Health: ", self.health)
        # What code would you add if any?

        return self

    def eatStrawberry(self):
        self.health += 10
        return self
    # YOUR CODE HERE:
    def pickUpSword(self, swordType):
        # Add the code to give the ninja a sword
        pass

kikomo = Ninja("Kikomo")
kikomo.displayStats()
kikomo.pickUpSword("katana")
kikomo.eatStrawberry().displayStats()
