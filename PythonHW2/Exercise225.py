#5) Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
#[1,2,3,4,5,6,7]
from datetime import *

def random(max):
    if max == 0:
        return 0
    else:
        rand_i = datetime.now().microsecond % 10
        while rand_i > max:
            rand_i -= max 
        return rand_i
     
def shuffle_list():
    new_list = input("Enter something: ")
    new_list = [i for i in new_list]
    print(f"Your initial list --> {new_list}")
    rand_list = []
    for i in range(len(new_list)):
        j = random(len(new_list)-1)
        rand_list.append(new_list[j])
        new_list.pop(j)
    print("\033[33m{}".format(f"Random list --> {rand_list}"))

shuffle_list()  
