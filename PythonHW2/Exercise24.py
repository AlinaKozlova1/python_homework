# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime
#  (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
from datetime import *


def random(min, max):
    rand_list = [int(i) for i in range(min, max)]
    today = datetime.now()
    rand_i = today.microsecond
    while rand_i > len(rand_list):
        rand_i //= 10
    return rand_list[rand_i]


keep_going = True
while keep_going:
    try:
        print("---------------------------------------")
        print("We need bounds for your random number!")
        max_num = int(input("Enter a max number: "))
        min_num = int(input("Enter a min number: "))
        print("Your random number is... ")
        random_num = random(min_num, max_num)
        print(f"---> {random_num} <---")
        answer = input("Do you wanna more random numbers?:)\
        \nEnter yes or no: ")
        keep_going = (answer != "no")
    except ValueError:
        print("It is not a number! Try again")
    except IndexError:
        print("Min number must be less than max!")




