class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def print_card(self):
        print(f"{self.rank} of {self.suit}")
        
    def get_value(self):
        val = self.rank
        return val
        
import random
class Deck():
    
    def __init__(self):
        suits = ['\u2666', '\u2665', '\u2663', '\u2660']
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
        self.deck = []
        self.build(suits, ranks)
    
    def build(self, suits, ranks):
        for r in ranks:
            for s in suits:
                self.deck.append(Card(s,r))
                
    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0,i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
            
    def drawCard(self):
        return self.deck.pop()
    
    def decksize(self):
        return len(self.deck)
        
    def show(self):
        for c in self.deck:
            c.print_card()

class Hand(Deck):
    def __init__(self, deck, num):
        super().__init__()
        self.hand = []
        self.deal_hand(deck, num)
        
    def deal_hand(self, deck, num):
        for i in range(num):
            self.hand.append(deck.drawCard())
            
    def show(self):
        for c in self.hand:
            c.print_card() 
            
    def draw_new_card(self, num):
        for i in range(num):
            self.hand.append(self.drawCard())
            
    def count_value(self):
        valuelist = []
        for c in self.hand:
            val = c.get_value() 
            if val == "K" or val == "Q" or val == "J":
                valuelist.append(10)
            elif val == 'A':
                ace = input("Is Ace high or low (11 or 1)")
                if ace == 'high' or ace == 11:
                    valuelist.append(11)
                elif ace == 'low' or ace == 1:
                    valuelist.append(1)
                else:
                    "That was neither 1 nor 11 you cheater, casino security are coming."
            else:
                val = int(val)
                valuelist.append(val)
            
            #valuelist.append(c.get_value())
        return sum(valuelist)

    def count_value_house(self):
        """At the moment the AI always chooses ace to be low. Needs refining."""
        valuelist = []
        for c in self.hand:
            val = c.get_value() 
            if val == "K" or val == "Q" or val == "J":
                valuelist.append(10)
            elif val == 'A':
                valuelist.append(1)
            else:
                val = int(val)
                valuelist.append(val)            
            #valuelist.append(c.get_value())
        return sum(valuelist)

def opponent_choice(score):
    if score > 16:
        opp_choice = 's'
    else:
        opp_choice = 't'
    return opp_choice

def check_winner(player1_hand, player2_hand):
    play1_score = abs(player1_hand.count_value() - 21)
    play2_score = abs(player2_hand.count_value_house() - 21)
    
    if play1_score > play2_score:
        print("Your score: {}. House's score {}. You lose!".format(play1_score, play2_score))
    
    elif play2_score > play1_score:
        print("Your score: {}. House's score {}. You win!".format(play1_score, play2_score))
        
    elif play2_score == play1_score:
        play1_handsize = player1_hand.decksize()
        play2_handsize = player2_hand.decksize()
        if play1_handsize > play2_handsize:
            print("The house has a smaller hand than yours: You lose!")
        elif play2_handsize > play1_handsize:
            print("You have a smaller hand than the house: You win!")
        elif play2_handsize == play1_handsize:
            print("It's a draw, all bets are off.")        
    else:
        print("Who the fuck knows.")