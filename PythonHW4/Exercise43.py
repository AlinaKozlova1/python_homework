# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.
from random import randint


def move_different_digits():
    lst = [randint(0, 10) for i in range(10)]
    print(lst)
    new_list = []
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count == 1:
            new_list.append(lst[i])
    print(new_list)


move_different_digits()
