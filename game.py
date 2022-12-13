from card import Card
from player import Player
from table import Table

def battle(player1: Player, player2: Player, table: Table):
    """Returns TRUE if player1 wins and FALSE otherwise"""

    # Get cards that will battle
    card1: Card = player1.nextCard()
    print(f"{player1.name} card: {card1} ({card1.rank})")
    card2: Card = player2.nextCard()
    print(f"{player2.name} card: {card2} ({card2.rank})")

    # Set the table with the battling cards
    table.setTwoCards(card1, card2)

    # Card1 wins
    if(card1.rank > card2.rank):
        # Check to see if stack can be stolen
        if(card1 == player2.showTopStack()):
            # Steal the stack
            print(f"{player1.name} has stolen!")
            stealStack(player1, player2)

        # Add cards to winner's stack ensuring winning card is on top
        player1.extendStack(table.player2_cards)
        player1.extendStack(table.player1_cards)

        # Clear the table
        table.clearTable()

        # Indicate that player1 won the battle
        return True

    # Card2 wins
    elif(card2.rank > card1.rank):
        # Check to see if stack can be stolen
        if(card2 == player1.showTopStack()):
            print(f"{player2.name} has stolen!")
            # Steal the stack
            stealStack(player2, player1)

        # Add cards to winner's stack ensuring winning card is on top
        player2.extendStack(table.player1_cards)
        player2.extendStack(table.player2_cards)

        # Clear the table
        table.clearTable()

        # Indicate that player2 won the battle
        return False

    # Cards are equal go to war
    else:
        print("\nA war!\n")
        return war(player1, player2, table)

    return "ERROR"


def war(player1: Player, player2: Player, table: Table):
    """Complete a war"""
    # Find the most number of cards that can contribute to a war
    war_num: int = 1
    if(player1.total >= 4 and player2.total >= 4):
        war_num = 4
    elif(player1.total >= 3 and player2.total >= 3):
        war_num = 3
    elif(player1.total >= 2 and player2.total >= 2):
        war_num = 2

    # Get war cards
    p1_cards = list()
    p2_cards = list()
    for i in range(war_num - 1):
        player1.checkAndSwap()
        player2.checkAndSwap()
        p1_cards.append(player1.nextCard())
        p2_cards.append(player2.nextCard())

    player1.checkAndSwap()
    player2.checkAndSwap()
    # Set table
    table.setMultiCards(p1_cards, p2_cards)
    print(table)
        
    # Do battle again
    return battle(player1, player2, table)

def stealStack(thief: Player, victim: Player):
    """Steal opponent's stack"""
    thief.stack_cards.extend(victim.stack_cards)
    