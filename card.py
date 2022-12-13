"""Card information"""

class Card:

    def __init__(self, name: str, rank: int, suit: str):
        self.name = name
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.name

    def getName(self):
        return self.name