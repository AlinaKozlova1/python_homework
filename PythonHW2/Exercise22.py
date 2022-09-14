# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений 
# (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial ():
    try:
        num = int(input("Enter a number: "))
        prodacts = []
        fac = 1
        if num == 0:
            print(f"factorial = {1}")
        elif num < 0:
            print("Your number must be positive" )
        else:
            for i in range(1, num+1):
                fac *= i
                prodacts.append(fac)
            print(f"The prodactd of factorial({num}) ---> {prodacts}")
    except ValueError:
        num = print("You don't trick me! \nEnter a number~ ")

factorial()