# 2 Создайте программу для игры в ""Крестики-нолики"".


from random import *
# create a table
table_A = {a: " . " for a in range(1, 10)}


def print_table(dict_):
    for i in range(1, 10):
        print(dict_[i], end=" ")
        if not i % 3:
            print("\t")


# check win / tie
win = 0


def check_victory(A):
    win_array = tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                 [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    
    for i in win_array:
        for j in range(len(i)-2):
            if A[i[j]] == A[i[j + 1]] == A[i[j + 2]] != " . ":
                return 1
    return 0


def check_tie(A):
    for i in A:
        if A[i] == " . ":
            return 0
    return 2


# change players| symbols
player_1, player_2 = input(
    "Player 1, what's your name? - "), input("Player 2, what's your name? - ")
current_player = randint(1, 2)
print(current_player, " - current player")
char = " x "
if current_player == 1:
    current_player = player_1
else:
    current_player = player_2
    


def switch_symbol(symbol):
    symbol = " o " if symbol == " x " else " x "
    return symbol


# fill the desk
print_table(table_A)
while win == 0:    
    try:
    
        block_num = int(input(f"{current_player}, enter a position: ")) 
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
    print_table(table_A)
    win = win + check_tie(table_A)
    win = win + check_victory(table_A)
    if win > 0:
        break
    char = switch_symbol(char)
    current_player = player_2 if current_player == player_1 else player_1
if win == 1 or win == 3:
    print(f"{current_player} won!")
else:
    print("Game tied~")
