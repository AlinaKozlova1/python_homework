# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#else return Fibonacci(n-1) + Fibonacci(n-2);

def fibonacci(num):
    fibonacci_list = []
    if num == 2 or num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
        #fibonacci_list.append(num)
    #print (fibonacci_list)

fibonacci(5)

for i in range(5):
    print(fibonacci(i))


#Аналог из С#
# double Fibonacci(int n)
# {
#     if(n==1||n==2) return 1;
#     else return Fibonacci(n-1) + Fibonacci(n-2);
# }

# for (int i = 1; i < 50; i++)
# {
#     Console.WriteLine($"(f{i}) = {Fibonacci(i)}");
# }

#def fib(k):
#     if k > 1:
#         return fib(k - 1) + fib(k - 2)
#     else:
#         if k == 1:
#             return 1
#         if k == 0:
#             return 0
# n = int(input('Введите натуральное число n = '))
# array_fib = [0] *(2*n + 1)
# for i in range(2*n + 1):
#     if i < n:
#         array_fib[i] = ((-1)**(i+1)) * fib(n - i)
#     elif i > n: array_fib[i] = fib(i - n)
# print(array_fib)
