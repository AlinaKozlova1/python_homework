#Для натурального n создать словарь индекс-значение,
#  состоящий из элементов последовательности 3n + 1.
#Пример:
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def n_dictionary():
    try: 
        number = int(input("Enter a number: "))
        new_dict = {i: 3*i + 1 for i in range(number)}
        print(new_dict)
    except ValueError:
        print("Nope, you must enter a number. Pls, try again:)")
    
n_dictionary()