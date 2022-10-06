# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# string[: : -1]}
#n = int(input())
# print('{0:b}'.format(n))

# S.zfill(width)
# Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями

def make_binary(num, binary_list): 
        if num//2 == 0:
            binary_list.append(num % 2)
            binary_list.reverse()
            binary_num = "".join(map(str, binary_list))
            print("\033[42m {}".format(binary_num))
        else:
            binary_list.append(num % 2)
            num //= 2
            make_binary(num, binary_list)
        
keep_going = True
while keep_going:
    number = int(input("Enter a number to make it binary: "))
    my_list = []
    make_binary(number, my_list)
    answer = input("Enter 'stop' to stop or press any key to continue: ")
    keep_going = answer!="stop"

