#Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
import math



keep_going = True
while keep_going:
    number = int(input("How many numbers behind decimal point do you want? - "))
    if 1 <= number <=10:
        print("\033[36m{}".format(round(math.pi, number)))
        print("\033[37m{}".format(" "))
    else:
        print("\033[31m{}".format("Your number must be from 1 to 10!"))
        print("\033[37m{}".format(" "))
    answer = input("Enter 'stop' to stop or press any key to continue: ")
    keep_going = answer!="stop"



