#Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

def out_red(text):
    print("\033[1m\033[31m{}".format(text))

def n_sequence():
    try:
        num = int(input("Enter a finil number of the sequence: "))
        
        new_array = [round((1 + (1/i))**i, 2) for i in range(1, num + 1)]
        list_sum = sum(new_array)
        print(f"Your list --> {new_array}\nSum of your list elements --> {list_sum}")
    except ValueError:
        out_red("It is not a number/integer!")

n_sequence()


#https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
#как красить текст