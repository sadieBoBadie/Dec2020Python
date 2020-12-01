
#

class Card:

    def __init__(self, val, suit):
        # Attributes
        self.value = val
        self.suit = suit
        self.played = False

class Deck:
    
    def __init__(self):
        self.cards = []
        self.buildDeck()

    def buildDeck(self):
        first_card = Card(1, "Hearts")
        self.cards.append(first_card)
        second_card = Card(2, "Diamonds")
        self.cards.append(second_card)

    def shuffle(self):
        # fisher-yates
        pass
    
    def show(self):
        for card in self.cards:
            print(f"{card.value} of {card.suit}")

newDeck = Deck()
newDeck.show()

# player1 = input("Type player 1's name:")
# player2 = input("Type player 2's name:")
