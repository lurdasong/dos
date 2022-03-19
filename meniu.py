import os
from uno import run_game

print("---------------------------")
print("-    Welcome to Dos       -")
print("---------------------------")
print("- 1 - Play game           -")
print("- 2 - About the author    -")
print("- 3 - The rules           -")
print("- 4 - Quit                -")
print("---------------------------")
number = int(input("What do you want to do? "))

if number == 1:
    os.system('clear')
    run_game

if number == 2:
    os.system('clear')
    print("Hi, it's me")

if number == 3:
    os.system('clear')
    print("How do you not know how to play uno?")

if number == 4:
    os.system('clear')
    quit()
