import random
#1.deck
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
        if self.score >= 22:
            print("you busted")
            self.playing = False
        else:
            print("you are still in the game")


    def draw(self, card):
        self.hand.append(card)
        self.score += card
        self.is_busted()

    def show_hand(self):
        print(self.hand)

class Dealer:
    def __init__(self):
        self.turns = 0
        self.deck = Deck()
        self.player = Player()
        self.hand = []
        self.score = 0
        self.playing = True

    def is_busted(self):
        if self.score >= 22:
            print("dealer busted")
            self.playing = False
        else:
            print("dealer is still in the game")

    def player_busted(self):
        if self.player.playing == False:
            self.playing = False

    def play(self):
        while self.playing:
            self.turns += 1
            if self.score < 15:
                self.draw_card()
            self.compare_scores()
            self.player_choice()
            
    def player_choice(self):
        answer = raw_input("hit? y/n ")
        if str(answer) == "y":
            self.give_card()
        elif str(answer) == "n":
            if self.turns > 5:
                print("game over house wins")
                self.player.playing = False
                self.player_busted()
            else:
                print("game continues")
        else:
            print("that is not an option")
            self.player_choice()

    def compare_scores(self):
        print('TURN;')
        print(self.turns)
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
