def g(b): # создаём функцию, чтобы проверять что есть чередование четных и нечётных цифр
    k = 1
    for i in range(len(str(b))-1):
        if ((str(b)[i] in '13579') and (str(b)[i+1] in '02468')) + ((str(b)[i] in '02468') and (str(b)[i+1] in '13579')) == 1:
            k += 1
    if k == len(str(b)):
        return True
    else: return False

t = open('172.txt') # открываем
a = [int(x) for x in t] # добавляем числа в наш массив
k = 0 # счётчик удовлетворяющих троек
masr = 0 # создаём максимум, только минимальный, чтобы потом его обновлять
for i in range(len(a)-2):
    a1 = a[i]
    a2 = a[i+1]
    a3 = a[i+2]
    sa = a1 + a2 + a3
    if ((a3/a2) == (a2/a1)) and (g(sa)) and a1 != a2 and a2 != a3:
        k += 1
        masr = max(masr,(a1+a2+a3)/3)
print(k,'%.2f'%masr)