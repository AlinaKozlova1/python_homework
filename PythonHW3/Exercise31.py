# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def not_even_nums_sum():
    try:
        new_list = input("Enter numbers without spaces: ")
        new_list = [int(i) for i in new_list]
        print("\033[32m{}".format(f"list --> {new_list}"))
        sum = 0
        for i in range(len(new_list)):
            if i%2 != 0:
                sum += new_list[i]
        print("\033[1m\033[32m{}".format(f"sum --> {sum}"))
    except ValueError:
        print("\033[1m\033[31m{}".format("You must enter an integer!"))



not_even_nums_sum()

