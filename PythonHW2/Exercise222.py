#Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial():
    try:
        num = int(input("Enter a number: "))
        new_list = []
        prodact = 1
        if num == 0:
            print("[0]")
        elif num < 0:
            print("Your number must be positive" )
        else:
            for i in range(1, num+1):
                prodact *= i
                new_list.append(prodact)
            print(f"The prodacts of ({num}) ---> {new_list}")
    except ValueError:
        print("You don't trick me! \nEnter a number~ ")

factorial()