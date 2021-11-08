import math


print("\t\tВП3_ЛР1 Вариант 4\n\tЗадание 1:")

print("Введите k")
k=int(input())
print("Введите l")
l=int(input())
print("Введите x")
x=float(input())

A=k+l/(k**2+abs(x**2/(k+l**3/3)))
B=1+math.tan(x/2)**2

print("A= ","%.2f" % A)
print("B= ","%.2f" % B)


print("\tЗадание 2:")
#принадлежность плоскости
print("Введите х точки")
x=float(input())
print("Введите у точки")
y=float(input())
isinarea=bool(((y>x-1)and(y>-x-1)and(y<x+1)and(y<-x+1)))
print(isinarea)


print("\tЗадание 3:")

print("Введите четырехзначное число")
olddig=int(input())
newdig =(olddig//1000%10)+(olddig//100%10)+(olddig//10%10)+olddig%10
print("Сумма цифр числа","%.0f" % newdig)



