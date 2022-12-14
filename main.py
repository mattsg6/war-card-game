from player import Player
from card import Card
from game import *
import random

def main() -> None:
    # Game intro sequence
    gameIntro()

    # Make a deck of cards
    suits: list = ["Spades", "Diamonds", "Hearts", "Clubs"]
    names: list = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"]
    symbols: list = ['♠', '♦', '♥', '♣']
    deck = list()

    for name in names:
        for suit in suits:
            deck.append(Card(name, names.index(name), suit, symbols[suits.index(suit)]))

    # Shuffle deck
    random.shuffle(deck)

    # Get player name
    player_name = input("\nEnter your name and press enter: ")

    # Make players
    player1 = Player(player_name)
    player2 = Player("Computer")

    # Deal cards
    for i in range(0,len(deck)):
        if(i % 2 == 0):
            player1.addCard(deck[i])
        else:
            player2.addCard(deck[i])

    # Make table
    table = Table(player1, player2)

    # Begin game
    initiate()

    # Keep track of which battle is being fought
    battle_counter = 1

    # Variable to track if the user wants the in game pauses
    pause = True

    # Menu option
    menu = False

    # The game
    while(player1.total > 0 and player2.total > 0):
        time.sleep(1)
        print("""\n
▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░
        \n""")
        print(f"Battle {battle_counter}\n")

        winner = battle(player1, player2, table, pause)

        if(winner):
            print(f"\n{player1.name} won the battle!")
        else:
            print(f"\n{player2.name} won the battle!")
            
        player1.checkAndSwap()
        player2.checkAndSwap()

        if(pause):
            option = input("\nEnter 'o' to see options and any other key to continue... ").lower()

        if(option == "o"):
            menu = True

        question = ""
        if(pause and menu):
            question = input("\nEnter 'g' to view game stats.\nEnter 'q' to quit.\nEnter 'c' for the rest of the game to be played without interuption.\nPress any other key to continue... ").lower()

        if(question == "g"):
            player1.gameStats()
            player2.gameStats()
        elif(question == "q"):
            exit()
        elif(question == "c"):
            pause = False
            menu = False


        battle_counter+=1

    if(player1.total > 0):
        print(f"\n{player1.name} won!")
    else:
        print(f"\n{player2.name} won!")

    gameOver()


if __name__ == "__main__":
    main()
else:
    print(__name__)