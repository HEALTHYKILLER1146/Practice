import random
#1.deck
#
class Deck:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
        random.shuffle(self.deck)

    def show_deck(self):
        print(self.deck)

    def deal_card(self):
        return self.deck.pop()
#2.player
class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

    def draw(self, card):
        self.hand.append(card)
        self.score += card
        self.is_busted?

    def is_busted?(self):
        if self.score > 21:
            print("you busted")
        else:
            print(self.score)
            print("you are still in the game")

    def show_hand(self):
        print(self.hand)


#3.init
deck = Deck()
deck.show_deck()
