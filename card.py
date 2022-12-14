"""Card information"""

class Card:

    def __init__(self, name: str, rank: int, suit: str, symbol: str):
        self.name = name
        self.rank = rank
        self.suit = suit
        self.symbol = symbol

    def __str__(self):
        if(self.name == "10"):
            return f"""
        ┌─────────┐
        |{self.name}       |
        |         |
        |         |
        |    {self.symbol}    |
        |         |
        |         |
        |       {self.name}|
        └─────────┘
        """
        return f"""
        ┌─────────┐
        |{self.name}        |
        |         |
        |         |
        |    {self.symbol}    |
        |         |
        |         |
        |        {self.name}|
        └─────────┘
        """

    def getName(self):
        return self.name