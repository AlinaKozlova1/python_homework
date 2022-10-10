# 5. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.

def open_polinominal():
    path = open("polinominal_file.txt", "r")
    polinominal_list = [i.split("= 0") for i in path]
    polinominal_list = [polinominal_list.pop(polinominal_list[i][-1] for i in range(len(polinominal_list)))]
    print(polinominal_list)
    # print(polinominal_list[0][1])

    #polinominal_list = [i for i in polinominal_list ]
    print(f"poli_list --> {polinominal_list}")
    return polinominal_list
open_polinominal()