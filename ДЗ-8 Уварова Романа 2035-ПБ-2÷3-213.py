#ДЗ-8 Уварова Романа 2035-ПБ-2/3-213
#Задание №3
def sum_range(s=1,e=100):
    if s>e:
        s,e=e,s
    g=0
    for i in range(s, e+1):
        g+=i
    print(g)
try:
    s=int(input())
    e=int(input())
    sum_range(s,e)
except ValueError:
    try:
        sum_range(s)
    except NameError or ValueError:
        sum_range()