#4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# with open("file.txt", "a") as data:
#     data.write("-1\n3\n1\n")

def out_blue(text):
    print("\033[1m\033[36m{}".format(text))

def fill_list():
    n = int(input("Enter a number: "))
    numbers_list = [i for i in range(-n, n + 1)]
    print(f"list --> {numbers_list}")
    return numbers_list

def open_index():
    path = open("file.txt", "r")
    index_list = [int(i) for i in path]
    print(f"indexes --> {index_list}")
    return index_list

def count_prodact():
    array = fill_list()
    indexes = open_index()
    prodact = array[indexes[0]]
    try:
        for i in range(1, len(indexes)):
            prodact *= array[indexes[i]]
        out_blue(f"---prodact---\n{prodact}")
    except IndexError:
        print("\033[31m{}".format("Your number is too small!"))




count_prodact()

# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных