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
            self.hand.append(deck.drawCard())
            
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
                    "You've crashed the entire game, casino security are coming."
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
    play2_score = abs(player2_hand.count_value() - 21)
    
    if play1_score > play2_score:
        print("You lose")
    
    elif play2_score > play1_score:
        print("You win!")
        
    elif play2_score == play1_score:
        play1_handsize = player1_hand.decksize()
        play2_handsize = player2_hand.decksize()
        if play1_handsize > play2_handsize:
            print("You lose")
        elif play2_handsize > play1_handsize:
            print("You win!")
        elif play2_handsize == play1_handsize:
            print("It's a draw, all bets are off.")        
    else:
        print("Who the fuck knows.")



no_winner = True
player_notbust = True
opponent_notbust = True
deck = Deck()
deck.shuffle()

player1_hand = Hand(deck, 2)
player2_hand = Hand(deck, 2)

if no_winner:
    player1_hand.show()
    print()

    # Stick or Twist
    if player_notbust:
        player_choice = input("Stick (s) or Twist (t)")
        if player_choice == 't' or player_choice == 'Twist':
            player1_hand.draw_new_card(1)
            player1_hand.show()
            print()
            if player1_hand.count_value() > 21:
                print("Bust!")
                player_bust = False        
        elif player_choice == 's' or player_choice == 'Stick':
            print("Your tally:{}".format(player1_hand.count_value()))
        
    if opponent_notbust:
        opp_choice = opponent_choice(player2_hand.count_value())
        if opp_choice == 't':
            player2_hand.draw_new_card(1)
            if player1_hand.count_value() > 21:
                print("Opponent bust!")
                opponent_notbust = False 
        
    if opp_choice == 's' and player_choice == 's':
        no_winner = False
        
print()        
print("Opponent Hand:")
player2_hand.show()
print("Score = {}".format(player2_hand.count_value()))
player2_hand.count_value()
print()
print("Your Hand:")
player1_hand.show()
print("Score = {}".format(player1_hand.count_value()))


print()
check_winner(player1_hand, player2_hand)  