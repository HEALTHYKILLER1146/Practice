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
        self.playing = True


    def is_busted(self):
        if self.score > 21:
            print("you busted")
            self.playing = False
        else:
            print(self.score)
            print("you are still in the game")


    def draw(self, card):
        self.hand.append(card)
        self.score += card
        self.is_busted()

    def show_hand(self):
        print(self.hand)
        
class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.hand = []
        self.score = 0
        self.playing = True

    def is_busted(self):
        if self.score > 21:
            print("dealer busted")
            self.playing = False
        else:
            print(self.score)
            print("dealer is still in the game")

    def player_busted(self):
        if self.player.playing == False:
            self.playing = False
    
    def play(self):
        while self.playing:
            if self.score < 15:
                self.draw_card()
            if self.player.score < 15:
                self.give_card()
        print("Dealer score:")
        print(self.score)
        print("Player score:")
        print(self.player.score)

    def draw_card(self):
        card = self.deck.deal_card()
        self.hand.append(card)
        self.score += card
        self.is_busted()
        
    def give_card(self):
        card = self.deck.deal_card()
        self.player.draw(card)
        self.player_busted()
#3.init
dealer = Dealer()
dealer.play()
