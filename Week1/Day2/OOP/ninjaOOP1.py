class Ninja:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def displayStats(self):
        print("Name:" + self.name)
        print("Health:" + str(self.health))
        return self

    def eatStrawberry(self):
        self.health += 10
        
# Predict the Output (if there are any errors,
# try to predict what it will say, and then fix it.)
hikusake = Ninja("Hikusake", 60)
print(hikusake.name)
kikomo = Ninja("Kikomo")
kikomo.displayStats()
kikomo.eatStrawberry()
kikomo.displayStats()
