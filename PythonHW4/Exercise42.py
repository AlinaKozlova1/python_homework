# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def make_prime_num(num):
    i = 2
    prime_num_list = []
    while num != 1:
        if num % i == 0:
            num /= i
            prime_num_list.append(i)
        else:
            i+=1
    return prime_num_list

keep_going = True
while keep_going:
    number = int(input("Enter a number: "))
    new_num_list = make_prime_num(number)
    print("\033[33m{}{}{}".format(number, " = ", new_num_list))
    print("\033[37m{}".format(" "))
    answer = input("Enter 'stop' to stop or press any key to continue: ")
    keep_going = answer != "stop"

