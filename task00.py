# Напишите программу, которая на вход принимает два числа A и B,
#  и возводит число А в целую степень B с помощью рекурсии. >


num1 = int(input('Введите первое число -> '))
num2 = int(input('Введите второе число -> '))



def exponentiation(a, b):
    if b == 0:
        return 1
    else:
        return a * exponentiation(a, b - 1) 
            
print(f' Число {num1} в степени {num2} -> ', end='')
print(exponentiation(num1, num2))