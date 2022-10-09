# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0
# 5. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

from random import randint

power = int(input("Enter 'k': "))


def make_polinominal(k):
    rand_rate = [randint(0, 101) for i in range(k+1)]
    polinominal_list = [str(i) for i in rand_rate]
    for i in range(len(polinominal_list)-1):
        polinominal_list[i] = polinominal_list[i] + "x"
    count = 0
    while k != 1:
        temp_k = str(k)
        polinominal_list[count] = polinominal_list[count] + "^" + temp_k
        k -= 1
        count += 1

    polinominal_list = " + ".join(polinominal_list) + " = 0"
    return polinominal_list





with open("polinominal_file.txt", "a") as data:
     data.write("\n" + make_polinominal(power))


# aaa = [2,3,4,5]
# aaa = [str(i) for i in aaa]
# for i in range(len(aaa)):
#     aaa[i] = aaa[i] + "x"
# print(aaa)
