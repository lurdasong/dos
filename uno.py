import random
import os

def generate_cards():
    cards = []
    for c in ["R", "G", "B", "Y"]: # cards in all the colors
        for x in range(1, 10): # cards from 1 to 9
            cards.append(f"{c}{x}") 
            cards.append(f"{c}{x}")
        cards.append(f"{c}0") # 4 zeroes
        cards.append(f"{c}S") # 4 skip
        cards.append(f"{c}S") # 4 skip
        cards.append(f"{c}R") # 4 reverse
        cards.append(f"{c}R") # 4 reverse
        cards.append(f"{c}D") # 4 draw 2
        cards.append(f"{c}D") # 4 draw 2
    #for x in range(4):
        cards.append("WC") # 4 wild cards
        cards.append("WD") # 4 wild draw cards 
    return cards


def give_cards(cards):
    player1 = cards[:7] # give player1 7 cards from the top
    cards = cards[7:] # remove first 7 cards
    player2 = cards[:7] # give player1 7 cards from the top
    cards = cards[7:] # remove first 7 cards
    table = cards[0] # take 1 cards from the top
    cards = cards[1:] # remove 1 card from the top
    return (table, player1, player2)

# not used
#def give_cards_n(cards, how_many_players):
    players = []
    for i in range(how_many_players):
        player = cards[:7]
        cards = cards[7:]
        players.append(player)

    table = cards[0]
    cards = cards[1:]
    return (table, players)


def initialize_game():
    cards = generate_cards()
    random.shuffle(cards) # shuffle cards
    table, player1, player2 = give_cards(cards) # gives cards to player1, player2 and table
    return (table, player1, player2)


def play_turn(table, player, which_player):
    print("Table:", table) # prints the current table
    print(f"Player {which_player} - here are your cards:", player) # player is cards
    player_played = input("Which card do you want to play? ")
    player.remove(player_played)
    os.system('clear')


def run_game_loop(table, player1, player2):
    while True:
        play_turn(table, player1, 1)
        play_turn(table, player2, 2)


def run_game():
    table, player1, player2 = initialize_game()
    run_game_loop(table, player1, player2)


#run_game()

# the first card, as in table
# check if player has the card he wants to play
# game logics ( aloooot.....)
## can card be played
## special cards
# add draw (2, 4, if you don't have)
# the end















