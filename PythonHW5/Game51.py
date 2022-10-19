from random import *

def game():
    player_1, player_2 = input(
        "Player 1, what's your name? - "), input("Player 2, what's your name? - ")
    current_player = randint(1, 2)
    print(current_player, " - current player")
    if current_player == 2:
        current_player = player_1
    else:
        current_player = player_2
    sweets_quantity = 2021
    while sweets_quantity > 0:
        print("\033[33m{}{}".format("sweets quantity = ", sweets_quantity))
        print("\033[37m".format())
        answer = 0
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1
        while answer < 1 or answer > 28:
            answer = int(input(f"{current_player}, enter a number from 1 to 28: "))
        sweets_quantity -= answer

    print(f"{current_player} wins!")


    