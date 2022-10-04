# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

array = [1.1, 1.2, 3.1, 10.01]


def min_max_difference(arr):
    min_num = round(arr[0]%1, 2)
    max_num = round(arr[0]%1, 2)
    for i in range(1, len(arr)):
        element = round(arr[i]%1, 2)
        if max_num < element:
            max_num = element
            print("max -", max_num) 
        if min_num > element:
            min_num = element
            print("min -", min_num)
    difference = max_num - min_num
    print(f"Difference between max and min elemens is equel to {difference}.")

min_max_difference(array)

# print(round(23.19%1, 2))
