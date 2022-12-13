from card import Card


"""Tracker for player items"""
class Player:

    def __init__(self, name: str):
        self.name = name
        self.war_cards: list = list()
        self.stack_cards: list = list()
        self.total: int = 26

    def addCard(self, card: Card):
        self.war_cards.append(card)
        self.total = len(self.war_cards) + len(self.stack_cards)

    def nextCard(self):
        self.total = len(self.war_cards) - 1 + len(self.stack_cards)
        return self.war_cards.pop(len(self.war_cards) - 1)

    def stackToWar(self):
        self.war_cards = self.stack_cards.reverse()
        self.stack_cards.clear()

    def addStack(self, card: Card):
        self.stack_cards.append(card)
        self.total = len(self.war_cards) + len(self.stack_cards)

    def extendStack(self, cards):
        self.stack_cards.extend(cards)
        self.total = len(self.war_cards) + len(self.stack_cards)

    def showTopStack(self):
        if(len(self.stack_cards) > 0):
            return self.stack_cards[(len(self.stack_cards) - 1)]
        else:
            return None

    def checkAndSwap(self):
        if(len(self.war_cards) == 0 and len(self.stack_cards) != 0):
            self.stackToWar()

    def displayCards(self):
        name_stack = list()
        name_war_cards = list()

        for card in self.stack_cards:
            name_stack.append(card.getName())

        for card in self.war_cards:
            name_war_cards.append(card.getName())

        print(f"\n{self.name}\nWar Cards: {name_war_cards}\nStack: {name_stack}")