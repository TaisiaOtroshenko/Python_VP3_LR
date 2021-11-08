import array
import random
import math

print("\t\tВП3_ЛР2 Вариант 4")
print("\tЗадание 1:")
#Заполние матрицы значениями столбцов элемента
size1=10
size2=20
ls=[[j+1 for j in range(size2)] for i in range(size1)]
for i in range(size1):
    for j in range(size2):
        print(ls[i][j],end = '  ')
    print()

print("\tЗадание 2:")
# Значения функции для промежутка х и у
f=[[0 for y in range(0,4)] for x in range(0,8)]
print ("\t\tх=0.2\tх=0.3\tх=0.4\tх=0.5")
y = 0.0
for i in range(0,8):
    print ("для y =","%.2f" % y, end='\t')
    x = 0.2
    for j in range(0,4):
        if x>=y:
            f[i][j]=math.log(abs(x/(1+y)))
        else:
            f[i][j]=((1+x)/(1+y))*math.e**-abs(x+y)
        print("%.3f" % f[i][j],end = '\t')
        x=x+0.1
    print()
    y = y +0.05

print("\tЗадание 3:")
# Сформировать массив случайных чисел от 3 до 42, посчитать сумму кратных 8
print("Введите количество элементов массива")
n=int(input())
sum = 0
im=[0 for i in range(n)]
for i in range(n):
    im[i]=random.randint(3,42)
    print (im[i], end="\t")
    if im[i]%8==0:
        sum = sum + im[i]
print ("\nСумма числел кратных 8 =", sum)

print("\tЗадание 4:")
# Найти соседние числа с минимальной разницей
print("Введите количество элементов массива")
n2=int(input())
a=[0 for i in range(n2)]
for i in range(n2):
    a[i]=random.randint(0,99)
    print("A [",i,"]","=",a[i])
index = 0
for i in range(1,n2-1):
    if abs(a[i+1] - a[i])<abs(a[index+1] - a[index]):
        index=i
print("Близкорасположенные числа -",a[index],'и',a[index+1])

print("\tЗадание 5:")
# Сформировать массив 1, 100, 2, 99, 3, 98,  … , 50, 51
mas = [ 0 for i in range(100)]
for i in range(100):
    if i%2==0:
        mas[i] = i//2 +1
    else:
        mas[i] = 100-i//2
    print (mas[i], end=" ")
print()

print("\tЗадание 6:")
# НОД по алгоритму Евклида
nod = 0
big = int(input("Введите первое число "))
small = int(input("Введите второе число "))
while big!=small:
    if big>small:
        big= big - small
    else:
        small = small - big
print ("НОД чисел -", big)

print("\tЗадание 7:")
# Числа Фибоначчи
mas5 = [ 0 for i in range(100)]
print ("Исходный массив:")
for i in range(100):
    if i%2==0:
        mas5[i] = i//2 +1
    else:
        mas5[i] = 100-i//2
    print (mas5[i], end=" ")
print ("\nЧисла Фибоначчи в нем:")
for i in range(100):
        if (5*(mas5[i]**2)-4)**0.5%1 == 0 or (5*(mas5[i]**2)+4)**0.5%1 == 0:
            print (mas5[i], end=" ")
print()

print("\tЗадание 8:")
# Взаимное расположение прямых
print ("Задайте коэффициенты уравнения прямой типа A*x + B*y = C")
A = int(input ("A = "))
B = int(input ("B = "))
C = int(input ("C = "))
A1 =int(input ("A1 = "))
B1 =int(input ("B1 = "))
C1 =int(input ("C1 = "))
if (A1/B1) == (A/B):
    print ("Прямые параллельны")
else:
    x = (C*B1-C1*B)/(A*B1-A1*B)
    y = (C - A*x)/B
    print ("Точка пересечения  х =", "%.1f" % x, "y =", "%.1f" % y)

print("\tЗадание 9:")
# Значения функции для промежутка х и у
f2=[0 for i in range(0,14)]
x2 = -0.8
for i in range(0,14):
    print ("для х =","%.1f" % x2, end='\t')
    if x2<-0.2:
       f2[i]=math.log(1+abs(x2))
    else:
      f2[i]=math.e**(-1+x2)
    print("f =", "%.3f" % f2[i])
    x2=x2+0.1

print("\tЗадание 10:")
# Сформировать квадратную матрицу
size = 12
sq=[[0 for j in range(size)] for i in range(size)]
for i in range(size):
    for j in range(size):
        if i<=j:
            sq[i][j] = abs(i-j)+1
        print(sq[i][j],end = '  ')
    print()



# print("Введите количество элементов массива")
# n=int(input())
# print("Введите границу массива")
# upp=int(input())
# a=[0 for i in range(n)]
# for i in range(n):
#     a[i]=random.randint(0,upp)
#     print("A[",i,"]","=",a[i],"\n")
# for i in range(n-1):
#     if (abs(a[i+1] - a[i])<abs(a[index+1] - a[index])):
#         index=i
# print("Близкорасположенные числа ",a[index],' ',a[index+1])


# print("a b c f1 f2 f3")
# for a in range(0,2):
#     for b in range(0,2):
#         for c in range(0,2):
#             f1 = a*b
#             f2 = 1 - f1
#             f3 = f2 +(a^c)
#             if (f3==2):
#                 f3=1
#             print("%d"%a,"%d"%b,"%d "%c,"%d "%f1,"%d "%f2,"%d"%f3)
