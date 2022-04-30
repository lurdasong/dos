import os
from uno import run_game

def call():
    meniu()
    number = input("> ")
    part(number)

def meniu():
    os.system('clear')
    print("---------------------------")
    print("-    Welcome to Dos       -")
    print("---------------------------")
    print("- 1 - Play game           -")
    print("- 2 - About the author    -")
    print("- 3 - The rules           -")
    print("- 4 - Quit                -")
    print("---------------------------")
   




def part(number):
    if number == "1":
        os.system('clear')
        input("Press enter to start game...")
        #call()
        run_game()
    elif number == "2":
        os.system('clear')
        print("""
        Hello, my name is Lurda Songailaite. I live in Lithuania. I study at LSMU gymansiun, II gynasium class A. 
        This is my end of the year programming project, called 'Dos'. Why is it called like that? So i won't get copyright issues. 
        Anyways, have fun!""")
        input("Press enter to continue...")
        call()
    elif number == "3":
        os.system('clear')
        print("""
        The game is really simple. First, do you know how to play 'Uno'? If you do, that's wonderful, because this game is really similar. 
        Actually, it's the same, but i called it 'Dos', because i needed a new name. 
        If you don't know how to play 'Uno', I'm going to quicly explain it to you. You start the game with seven cards and a table card in the middle. 
        There are four colors of the cards - red, yellow, green and blue. Or in this game - R, Y, G, B. Also there are numbers on those cards - from 0 to 9.
        There are also special cards. Skip (S) makes the other player skip their turn and draw 2 (D) makes the other player draw 2+ cards. There are also
        wild cards. The normal wild card (WC) have the ability to change the table color and wild draw card (WD) can change color and make the other player draw 4+ cards. 
        The game is played until one of the players has no cards left - that player wins. You can only discard cards that match the color or number or action (special card)
        of the table card. If you don't have a card that you can play - you draw one from the deck. Pretty easy, isn't it? Now go try play it!
        """)
        input("Press enter to continue...")
        call()
    elif number == "4":
        os.system('clear')
        quit()
    else:
        os.system('clear')
        print(f"What...? I don't understant what {number} means. Try again")
        input("Press enter to continue...")
        call()

call()

