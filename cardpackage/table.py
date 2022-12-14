from cardpackage.card import Card
from cardpackage.player import Player

class Table:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1_cards = list()
        self.player2_cards = list()

    def setMultiCards(self, p1_cards: list, p2_cards: list):
        self.player1_cards.extend(p1_cards)
        self.player2_cards.extend(p2_cards)

    def setTwoCards(self, p1_card: Card, p2_card: Card):
        self.player1_cards.append(p1_card)
        self.player2_cards.append(p2_card)

    def clearTable(self):
        self.player1_cards.clear()
        self.player2_cards.clear()

    def __str__(self):
        p1_names = list()
        p2_names = list()
        for n in self.player1_cards:
            p1_names.append(n.getName())
        for n in self.player2_cards:
            p2_names.append(n.getName())
        return f"{self.player1.name} cards: {p1_names}\n{self.player2.name} cards: {p2_names}"