import math
from random import *


def answer_bot(count_of_sweets):
    if math.ceil(count_of_sweets/28) % 2 == 1: #нечётное количество операций = победа 
        return 28
    else: 
        full_sweet_bunches = count_of_sweets//28 
        balance = (count_of_sweets - full_sweet_bunches*28)//2
        if balance == 0:
            return 1
        else:
            return balance






def game_with_bot():
    player = input("What's your name? - ")
    bot = "bot"
    current_player = randint(1, 2)
    print(current_player, " - current player")
    if current_player == 2:
        current_player = player
    else:
        current_player = bot
    sweets_quantity = 2021

    while sweets_quantity > 0:
        if current_player == player:
            current_player = bot
        else:
            current_player = player
        print("\033[33m{}{}".format("sweets quantity = ", sweets_quantity))
        print("\033[37m".format())
        answer = 0
        if current_player == "bot":
            answer = answer_bot(sweets_quantity)
            print(f"bot's number: {answer}")
        else:
            while answer < 1 or answer > 28:
                answer = int(input(f"{current_player}, enter a number from 1 to 28: "))
        sweets_quantity -= answer

    print(f"{current_player} wins!")
