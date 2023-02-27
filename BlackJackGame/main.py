# This is the highest level file from which the main programme runs, grabbing other scripts only as needed
# It contains the main runtime logic

from Game_Components import Deck, Hand, opponent_choice, check_winner

print()
player1 = input('Welcome to the Casino! What is you name?')

deck = Deck()
print()
print('Welcome {}. I am shuffling the deck'.format(player1))
deck.shuffle()

print()
print('Dealing cards')

no_winner = True
player_notbust = True
opponent_notbust = True
deck = Deck()
deck.shuffle()

player1_hand = Hand(deck, 2)
player2_hand = Hand(deck, 2)


# Game Engine
"""
I tried to place this game engine into a seperate script and call it from the main.py file, but had problems calling it. I think I still don't fully understand 
the use of self in classes and properly accessing functions defined within those classes
"""
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
        opp_choice = opponent_choice(player2_hand.count_value_house())
        if opp_choice == 't':
            player2_hand.draw_new_card(1)
            if player1_hand.count_value() > 21:
                print("House is bust! You win!")
                opponent_notbust = False 
        
    if opp_choice == 's' and player_choice == 's':
        no_winner = False


        
print()        
print("House's Hand:")
print()
player2_hand.show()
print("Score = {}".format(player2_hand.count_value_house()))
#player2_hand.count_value_house()
print()
print("Your Hand:")
print()
player1_hand.show()
print("Score = {}".format(player1_hand.count_value()))


print()
check_winner(player1_hand, player2_hand)    


