#ДЗ-4 Уварова Романа 2035-ПБ-2/3-213

#Задача №5
N=int(input("Введите число: "))
Nr=N
n=0
while N>0.1:
    n*=10
    n+=N%10
    N=N//10
if Nr==n:
    print(Nr, "является палиндромом")
else:
    print(Nr, "не является палиндромом")

#Задача №6
g=0
G=int(1)
while G!=0:
    G=int(input("Введите число: "))
    g+=G
print("Сумма введёных вами чисел равна", g)

Задача №7
s=int(input("Введите начальное число диапазона: "))
e=int(input("Введите конечное число диапазона: "))
if s>=e:
    print("Ошибка: Начальное число больше конечного")
else:
    if s<2 and e>=2:
        s=2
    else:
        pass
    for i in range(s, e+1):
        I=2
        a=True
        while a==True:
            if i==2:
                print(i)
                a=False
            elif I!=i and i%I==0:
                a=False
            elif I!=i:
                I=I+1
            else:
                print(i)
                a=False

#Задача №8
f=int(input("Введите количество чисел Фибоначчи, которые нужно вывести: "))
num1=1
num2=1
if f<=0:
    print("Ошибка: Было введено не натуральное число")
elif f==1:
    print(num1)
elif f==2:
    print(num1)
    print(num2)
elif f>2 and f%2==0:
    print(num1)
    print(num2)
    for h in range(round(f/2-1)):
        num1=num1+num2
        print(num1)
        num2=num1+num2
        print(num2)
        h+=1
else:
    print(num1)
    for h in range(round((f-1)/2)):
        print(num2)
        num1=num1+num2
        num2=num1+num2
        print(num1)
        h+=1

#Задача №9
H=int(input("Введите высоту треугольника: "))
if H<2:
    print("Ошибка: Некорректное значение высоты")
else:
    for l in range(H):
        print(" "*(H-l), "*"*(2*l+1))