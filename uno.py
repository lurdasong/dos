import random
import os
from unittest import skip

COLORS = ["R", "G", "B", "Y"]

def generate_cards():
    cards = []
    for c in COLORS : # cards in all the colors
        for x in range(1, 10): # cards from 1 to 9
            cards.append(f"{c}{x}") 
            cards.append(f"{c}{x}")
        cards.append(f"{c}0") # 4 zeroes
        cards.append(f"{c}S") # 4 skip
        cards.append(f"{c}S") # 4 skip
        #cards.append(f"{c}R") # 4 reverse
        #cards.append(f"{c}R") # 4 reverse
        cards.append(f"{c}D") # 4 draw 2
        cards.append(f"{c}D") # 4 draw 2
    #for x in range(4):
        cards.append("WC") # 4 wild cards
        cards.append("WD") # 4 wild draw cards 
    return cards


def give_cards(cards):
    starting_card_count = 2
    player1 = cards[:starting_card_count] # give player1 7 cards from the top
    cards = cards[starting_card_count:] # remove first 7 cards
    player2 = cards[:starting_card_count] # give player2 7 cards from the top
    cards = cards[starting_card_count:] # remove first 7 cards
    which_card_to_put_on_table = 0
    while not cards[which_card_to_put_on_table][1].isnumeric():
        which_card_to_put_on_table += 1
    table = []
    table.append(cards.pop(which_card_to_put_on_table)) # take 1 cards from the top and remove 1 card from the top
    return (table, player1, player2, cards)

# not used
def give_cards_n(cards, how_many_players):
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
    table, player1, player2, cards = give_cards(cards) # gives cards to player1, player2 and table
    return (table, player1, player2, cards)

def reshuffle_cards(table, cards):
    while (len(table) > 1):
        cards.append(table.pop(0))

    # cards = table[:-1]
    # table = table[-1:]
    random.shuffle(cards)
    return (table, cards)

def turn_loop(state, player, which_player, cards): #act a turn
    (table, new_color, skipped_turn, draw_count) = state
    if table[-1][1] == "S" and not skipped_turn:
        return ""
    
    while (True):
        print("Table:", table[-1]) # prints the current table
        if table[-1][0] == "W":
            print(f"New color is {new_color}")
        print(f"Player {which_player} - here are your cards:", player) # player is cards
        player_played = input("Which card do you want to play? (D to draw instead) ")

        if player_played.upper() == "D":
            if draw_count == 0:
                draw_count = 1
            for n in range(draw_count):
                if len(cards) == 0:
                    print(f"Deck before: {cards}")
                    reshuffle_cards(table, cards)
                    print(f"Deck after: {cards}")
                    print(f"Table: {table}")
                if len(cards) == 0:
                    # if table 1 card, deck 0 cards, all cards in hands, this crashes
                    raise Exception("Players are retarded, game over.")
                player.append(cards.pop())
            draw_count = 0
            return ""

        if player_played not in player:
            print("You do not have this card. Pick another one.")
            continue
        
        if not can_card_be_played(state, player_played):
            print("You cannot play this card. Pick another one.")
            continue
        else:
            break

    return player_played

def color_change(player_played):
    new_color = player_played[0]

    if player_played[0] == "W":
        new_color = input(f"Choose a color: {COLORS} ")
        while new_color not in COLORS:
            new_color = input(f"Wrong choice. Choose a color: {COLORS} ")
    
    return new_color


def play_turn(state, player, which_player, cards):
    (table, new_color, skipped_turn, draw_count) = state
    os.system('clear')
    player_played = turn_loop(state, player, which_player, cards)
    if player_played == '':
        return (table, new_color, True, draw_count)
    if player_played[1] == "D":
        draw_count += 4 if player_played[0] == 'W' else 2

    new_color = color_change(player_played)
    
    player.remove(player_played) # isimam is zaidejo rankos korta
    table.append(player_played) # add card to top of table
    return (table, new_color, False, draw_count)
    
    
def can_card_be_played(state, played_card):
    (table, new_color, skipped_turn, draw_count) = state

    table_color = table[-1][0]
    table_number = table[-1][1]
    played_color = played_card[0]
    played_number = played_card[1]

    # on table:
    # if card is skip
        # check color
    # if card is wild
        # check color
    # if card is draw 2
        # if skipped_turn = False, can play only +2
        # if skipped_turn = True, check color
    # if card is draw 4
        # if skipped_turn = False, can play only +4
        # if skipped_turn = True, check color
    # if card is normal
        # check color
        # check number

    
    if table[-1][1] == "S":
        if played_card[0] == new_color or played_card[0] == "W":# color check
            return True

    if table[-1][0] == "W":
        if played_card[0] == new_color or played_card[0] == "W":# color check
            return True

    if table[-1][1] == "D":
        if skipped_turn:
            if played_card[0] == new_color or played_card[0] == "W": # color check
                return True
        if not skipped_turn:
            if table[-1][0] == "W":
                if played_card == "WD":
                    return True
            else:
                if played_card[0] != 'W' and played_card[1] == "D":
                    return True

    if (table[-1][0] in COLORS) and (table[-1][1].isnumeric()):
        if table[-1][1] == played_card[1] or played_card[0] == "W": # number check
            return True

        if played_card[0] == new_color or played_card[0] == "W":# color check
            return True

    return False
    

def run_game_loop(table, player1, player2, cards):
    players = [player1, player2]
    new_color = table[-1][0]
    skipped_turn = False
    draw_count = 0
    while True:
        for id, player in enumerate(players):
            (table, new_color, skipped_turn, draw_count) = play_turn((table, new_color, skipped_turn, draw_count), player, id+1, cards)
            if not player:
                print(f"You won, player {id+1}")
                return
                
                

def run_game():
    table, player1, player2, cards = initialize_game()
    run_game_loop(table, player1, player2, cards)
    

if __name__ == "__main__":
    run_game()


# the first card, as in table
# check if player has the card he wants to play
# game logics:
## can card be played
## skip
## wild card
## draw (2, 4, if you don't have)
# the end

# if (player has card he wants to play):
    # run a loop to check if the player has any cards he can play
        # if True
            # if (card is playable):
                #remove
                # if card is skip
                    # skips
                # if card is wild
                    # changes color
                # if card is draw 2
                    # adds 2 cards from 'cards'
                # if card is draw 4
                    # adds 4 cards from 'cards' and changes color
            # else if it's not playable:
                # tell him to pick another one
        # else if False
            # add 1 cards from 'cards'
# else:
    # print - player has no such card

#if (player has no cards in his hand):
    # player wins
    # game closes (return to meniu?)














