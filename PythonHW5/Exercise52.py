# 2 Создайте программу для игры в ""Крестики-нолики"".

import GameFunctions52
from random import *


# create a table
table_A = {a: " . " for a in range(1, 10)}
win = 0


# change players| symbols
player_1, player_2 = input(
    "Player 1, what's your name? - "), input("Player 2, what's your name? - ")
current_player = randint(1, 2)
print(current_player, " - current player")
char = " x "
current_player = player_1 if current_player == 1 else player_2


# fill the desk
GameFunctions52.print_table(table_A)
while win == 0:
    try:
        block_num = int(input(f"{current_player}, enter a number of block position: "))
    except ValueError:
        print("\033[33m{}".format("Invalid Input! Try Again"))
        print("\033[37m".format())
        continue
    if block_num < 1 or block_num > 9:
        print("\033[33m{}".format("Invalid Input! Try Again"))
        print("\033[37m".format())
        continue
    if table_A[block_num] != " . ":
        print("\033[33m{}".format("This block is occupied! Try Again"))
        print("\033[37m".format())
        continue
    table_A[block_num] = char
    GameFunctions52.print_table(table_A)
    win = win + GameFunctions52.check_tie(table_A)
    win = win + GameFunctions52.check_victory(table_A)
    if win > 0:
        break
    char = GameFunctions52.switch_symbol(char)
    current_player = player_2 if current_player == player_1 else player_1
if win == 1 or win == 3:
    print(f"{current_player} won!")
else:
    print("Game tied~")
