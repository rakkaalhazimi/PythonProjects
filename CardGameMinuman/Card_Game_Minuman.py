'''
Minuman Card Game Algorithm:

1. The number of the cards is 52 (stack type).

2. Before starting the game, the cards must be shuffled.

3. After it get shuffled, each player will get 4 cards "sequentially" from the stack of cards.

4. When all the players got the cards. Take 1 more card that will be used as "reference card".

5. Now, each player must take out the card that match the type of "reference card" (spades, hearts, diamonds or clubs).

6. If the player don't have the same type card like "reference card". The player MUST take the card from the stack
   one by one until the player get the required card.

7. When all the players have thrown the card, the system will compare each of the card value.

8. Whoever has the card with the highest value (except reference_card) will have the privilege to get the first turn in
    the next round.

9. Repeat step number 5 - 8 until the "stack got depleted" and the player deck is empty.

10.  Game Over #1: If one player deck is empty, it will become the winner.
10.1 Game Over #2: If the stack got depleted, the winner will be determined by the ones who has the least card in the deck.
'''
# Import particular modules
from CardGameMinuman.Deck_Card import IndoDeck
from CardGameMinuman.Stack import Stack
import random

# Generate players
class Player:
    def __init__(self, player):
        self.player = player
        self.deck = []

player1 = Player('Player 1')
computer = Player('A.I')

# Generate cards
cardDeck = IndoDeck()
cardStack = Stack()

reference_card = None
player1_card = None
comp_card = None

for i in cardDeck:
    cardStack.push(i)

# Shuffle the cards
def shuffle():
    random.shuffle(cardStack.items)

# Generate each player initial deck (default= 4) and generate the reference_card.
def give_card():
    global reference_card

    for i in range(1,10):
        if i < 9 and i % 2 != 0:
            player1.deck.append(cardStack.pop())
        if i % 2 == 0:
            computer.deck.append(cardStack.pop())
        if i == 9:
            reference_card = cardStack.pop()
            return reference_card

# Define each card value
def card_value(card):
    value = 0
    if card[0] in ['1','2','3','4','5','6','7','8','9','10'] :
        value = int(card[0])
    else:
        if card[0] == 'J':
            value = 11
        if card[0] == 'Q':
            value = 12
        if card[0] == 'K':
            value = 13
        if card[0] == 'A':
            value = 14

    return value

# Configuring player's move algorithm
def player_move():
    global reference_card, player1_card
    run = True

    while run:
        player1_deck_types = [y for x, y in player1.deck]
        if len(player1.deck) > 0:
            if reference_card[1] in player1_deck_types:
                print('\n','\n','\n')
                print('==============================================================================')
                print('Current Reference Card: ', reference_card)
                print('Your decks are:\n', player1.deck)
                print('==============================================================================')

                try:
                    choose = int(input("Which index of the cards, that will be called ?(start from 0) : "))
                    print('\n', '\n', '\n')

                    if choose < len(player1.deck) and reference_card[1] in player1_deck_types[choose]:
                        run = False
                        player1_card = player1.deck.pop(choose)
                        return player1_card
                    else:
                        print("You haven't that much card or Your card didn't matches the reference card")
                        continue

                except:
                    print("Please enter the valid index :)")

            else:
                if cardStack.is_empty():
                    run = False
                else: # When the player's card didn't match the reference card.
                    print("You don't have any required card, take card: {} from the stack".format(cardStack.peek()))
                    player1.deck.append(cardStack.pop())
        if player1.deck == []:
            run = False
            return player_iswin()

# Confiuring A.I's move algorithm
def comp_move():
    global comp_card, reference_card
    print("Computer's Turn")
    print("Computer's Deck: {}".format(computer.deck))
    run = True
    while run:
        comp_deck_types = [y for x, y in computer.deck]
        position = None
        for x,y in enumerate(comp_deck_types):
            if y == reference_card[1]:
                position = x

        if len(computer.deck) > 0:
            if reference_card[1] in comp_deck_types:
                run = False

                comp_card = computer.deck.pop(position)
                print("Computer has thrown {}".format(comp_card))
                return comp_card
            else:
                if cardStack.is_empty():
                    run = False
                    print("Error Found")
                else:
                    print("Computer draw {} from the stack.".format(cardStack.peek()))
                    computer.deck.append(cardStack.pop())
        else:
            run = False
            return comp_iswin()

# Player state of winning
def player_iswin():
    if player1.deck == []:
        return True
    else:
        return False

# A.I state of winning
def comp_iswin():
   if computer.deck == []:
       return True
   else:
       return False

def main():
    global player1_card, comp_card, reference_card

    print("Welcome to the Card Game Minuman, your main objective is throw any of your card that matches the reference card \n"
          "until your deck card is empty. Good Luck and Have Fun.")
    shuffle()
    give_card()

    player_move()
    comp_move()
    while not player_iswin() and not comp_iswin():

        if card_value(player1_card) > card_value(comp_card):
            if cardStack.is_empty():
                break
            if player_iswin() or comp_iswin():
                break
            else:
                reference_card = cardStack.pop()
                player_move()
                if not player_iswin():
                    comp_move()

        if card_value(player1_card) < card_value(comp_card):
            if cardStack.is_empty():
                break
            if player_iswin() or comp_iswin():
                break
            else:
                reference_card = cardStack.pop()
                comp_move()
                if not comp_iswin():
                    player_move()

    if cardStack.is_empty():
        print("Through this func")
        print(len(player1.deck))
        print(len(computer.deck))
        if len(player1.deck) < len(computer.deck):
            return player_iswin()
        if len(player1.deck) == len(computer.deck):
            print("Tie Game")
        if len(computer.deck) > len(player1.deck):
            return comp_iswin()

    if player_iswin():
        print("Congratulation, You win the game. Kick the A.I back to home !")
    if comp_iswin():
        print("A.I have just beaten you, try again in the next time !")


main()









