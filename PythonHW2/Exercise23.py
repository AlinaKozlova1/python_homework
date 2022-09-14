# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: 
# "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны
#  читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и 
# проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

#345

def make_palindrome (num):
    
        
    temp_num = num
    reflected_num = 0
    while temp_num != 0:
        digit = temp_num % 10
        temp_num //= 10
        reflected_num *= 10
        reflected_num += digit
    if num == reflected_num:
        print(f"--> {num} <-- \n{num} is a palindrome!")
        return num
        
    else:
        print(f"--> {num} <-- \n{num} is not a palindrome \
            \nThen we sum {num} and {reflected_num}")
        return make_palindrome(num + reflected_num)
            
    

try:
    number = int(input("Enter a number: "))
    make_palindrome(number)
except ValueError:
        print("Nope, you must enter an integer.")



#print(345//1000)