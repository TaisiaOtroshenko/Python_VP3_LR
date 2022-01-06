# Считать данные из CSV файла в структуру DataFrame.
# Добавить еще один столбец, в котором содержится разница (по модулю)
# между средним возрастом и возрастом каждого из покупателей.
# Определить ID покупательницы, не моложе 40 лет, которая имеет самый большой доход.
# Построить график зависимости дохода покупателя от его возраста.
# Вывести результаты для 5 покупателей с самым большим доходом и 5 с самым маленьким.
# Построить трехмерную поверхность – прямоугольный параллелепипед (параметры параллелепипеда задать произвольно).

import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, savefig, rc
from mpl_toolkits.mplot3d import Axes3D

# считываем CSV файл с данными
apps = pd.read_csv('D:\git_repos\Python_VP3_LR\DR2\data.csv', delimiter=",")
# добавляем столбец разности от среднего возраста
delta = pd.Series([int(abs(apps[['age']].mean()-apps['age'].to_list()[i])) for i in range(len(apps))], index=apps.index)
apps = apps.assign(delta=delta.values)
# поиск самой старой и богатой
tmp = apps.sort_values(['income'], ascending=False)
for index, row in tmp.iterrows():
    if row['age'] >= 40 and row['gender'] == 'female':
        print("ID самой богатой пожилой покупательницы -", index)
        break
# получение 5 наибольших и наименьших значений
largest = apps.nlargest(5, 'income').sort_values(['age'])
smallest = apps.nsmallest(5, 'income').sort_values(['age'])
# построение графиков с помощью pandas.plot() и сохранение в pdf-файл
rc('font', size=90)

largest.plot(x='age', y='income', figsize=(100, 100), fontsize=90, linewidth=10.0, title="Зависимость дохода от возраста для людей с самым низким доходом")
savefig('largest.pdf')

smallest.plot(x='age', y='income', figsize=(100, 100), fontsize=90, linewidth=10.0, title="Зависимость дохода от возраста для людей с самым высоким доходом")
savefig('smallest.pdf')

# параметры прямоугольного параллелепипеда
a = 5
b = 4
c = 7
X = np.arange(0, a, 0.05)
Y = np.arange(0, b, 0.05)
Z = np.arange(0, c, 0.05)
# построение прямоугольного параллелепипеда с помощью matplotlib
rc('font', size=10)
fig = figure()
ax = Axes3D(fig)
# z
U, V = np.meshgrid(X, Y)
ax.plot_surface(U, V, U*0, linewidth=1)
ax.plot_surface(U, V, U*0+c, linewidth=1)
# y
U, V = np.meshgrid(X, Z)
ax.plot_surface(U, U*0, V, linewidth=1)
ax.plot_surface(U, U*0+b, V, linewidth=1)
# x
U, V = np.meshgrid(Y, Z)
ax.plot_surface(U*0, U, V, linewidth=1)
ax.plot_surface(U*0+a, U, V, linewidth=1)

savefig("parallelepiped.pdf")
