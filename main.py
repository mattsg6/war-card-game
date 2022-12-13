from player import Player
from card import Card
from game import *
import random

def main() -> None:
    # Make a deck of cards
    suits: list = ["Spades", "Clubs", "Diamonds", "Hearts"]
    names: list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    "Jack", "Queen", "King", "Ace"]
    deck = list()

    for name in names:
        for suit in suits:
            deck.append(Card(f"{name} of {suit}", names.index(name), suit))

    # Shuffle deck
    random.shuffle(deck)

    # Make players
    player1 = Player("player1")
    player2 = Player("player2")

    # Deal cards
    for i in range(0,len(deck)):
        if(i % 2 == 0):
            player1.addCard(deck[i])
        else:
            player2.addCard(deck[i])

    # Make table
    table = Table(player1, player2)

    while(player1.total > 0 and player2.total > 0):
        print("..........\n\nA Battle!\n")

        winner = battle(player1, player2, table)

        if(winner):
            print(f"\n{player1.name} won the battle!")
        else:
            print(f"\n{player2.name} won the battle!")

        player1.checkAndSwap()
        player2.checkAndSwap()

        if(input("\nDisplay cards (y/n): ") == "y"):
            player1.displayCards()
            player2.displayCards()

        input("\nPress enter to continue")

    if(player1.total > 0):
        print(f"{player1.name} won!")
    else:
        print(f"{player2.name} won!")

if __name__ == "__main__":
    main()
else:
    print(__name__)