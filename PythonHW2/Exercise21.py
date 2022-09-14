# 1 - Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

def digit_sum():
    try:
        summa = 0
        number_list = list(input("Enter a number: "))
        number_list = (int(i) for i in number_list if i != ".")
        summa += sum(number_list)

        print(f"Your digits sum = {summa} ")
    except ValueError:
        print("It must be a number! >:( ")
    
digit_sum()


