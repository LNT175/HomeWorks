#ДЗ-3 Уварова Романа 2035-ПБ-2/3-213
#Задача №5
try:
    a = int(input("Введите число: "))
except ValueError:
    print("Вы некорректно ввели число, попробуйте заново")

#Задача №6
try:
    b, c = int(input("Введите делимое число: ")), int(input("Введите делитель: "))
    print("Результат их деления равен", round(b/c, 3))
except ZeroDivisionError:
    print("Ошибка: деление на ноль")

#Задача №7
from math import pow
class NegativeNumberError(Exception):
    pass
try:
    x = int(input("Введите положительное число: "))
    if x<=0:
       raise NegativeNumberError 
    else:
       print(x**2)
except NegativeNumberError:
   print("Ошибка: Введёное число не было положительным")