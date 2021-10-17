# need to create two players: player and house 
# alternate games 
# begin game with an open card 
# the one with 21 or closest to it without going over wins

import random

# card deck array 
card_deck = ["Ace","Ace","Ace","Ace","King","King","King","King","Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen",
"Club","Club","Club","Club",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9]

# pulling a card
def card_selected(card_deck):
    rand_card = random.randint(0,len(card_deck)-1)
    card = card_deck[rand_card]
    return card 

# defining card value, factoring in dealer standard rules and ace dynamic values 
# also factors in current score and allows the player to hit 
def card_value(card,current_score,player):
    value = 0
    if card == "Queen":
        value = 10
    elif card == "King":
        value = 10
    elif card == "Jack":
        value = 10
    elif card == "Club":
        value = 10
    elif card == "Ace" and player == "dealer":
        if current_score <= 6:
            value = 11
        else: 
            value = 1
    elif card == "Ace" and player == "player":
        player_choice = eval(input(f"You have a {current_score}. Would you like your Ace to be a 1 or 11? "))
        value = player_choice
    else: 
        value = card
    return value
    
# one function for the entire game since the array is mutable 
def play_blackjack(card_deck):
    current_player = "dealer"
    dealer_score = 0
    dealer_open = card_selected(card_deck)
    dealer_value = card_value(dealer_open,dealer_score,current_player)
    dealer_score += int(dealer_value)
    while dealer_score < 17:
        dealer_count = 0
        new_dealer_card = card_selected(card_deck)
        card_deck.remove(new_dealer_card)
        new_dealer_card_converted = card_value(new_dealer_card,dealer_score,current_player)
        print(len(card_deck))
        dealer_score += int(new_dealer_card_converted)
        if dealer_count == 0:
            print(f"The dealer is showing a {dealer_open} and the current dealer score is {dealer_score}. ")
        else:
            print(f"The current dealer score is {dealer_score}.") 
        dealer_count += 1 

    if dealer_score > 21:
        print("The dealer is bust. ")
        print("Player wins. ")
        quit()
    elif dealer_score == 21:
        print("The dealer wins. \nGame over.")
        quit()
    player = "player"
    player_score = 0
    player_open = card_selected(card_deck)
    card_deck.remove(player_open)
    player_value = card_value(player_open,player_score,player)
    player_score += player_value
    while player_score < 21:
        if player_score > dealer_score:
                print(f"The player wins with {player_score}.")
                quit()
        next_play = input(f"Your score is {player_score}. Would you like hit or stand? ")
        if next_play.upper() == "HIT":
            next_card = card_selected(card_deck)    
            next_card_value = card_value(next_card,player_score,player)
            player_score += next_card_value
        elif player_score > 21:
            print(f"Player busts with a score of {player_score}. \nGame over. ")
            quit()
        else:
            if player_score > dealer_score:
                print(f"The player wins with {player_score}.")
                quit()
            elif player_score == dealer_score:
                print("There was a tie. ")
                quit()
            else: 
                print("The dealer wins. ")
                quit()


play_blackjack(card_deck)
