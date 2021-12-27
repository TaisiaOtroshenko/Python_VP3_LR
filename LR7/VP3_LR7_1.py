# Задача 1. Создайте матрицу размером 5х5, на границах которой расположены 0, внутри пространство заполнено 1. 
# Определите значение её ранга. 
# Создайте массив, заполненный числами от 6 до 16. “Разверните” массив. 
# Перемножьте значения седьмого элемента массива и ранга матрицы, запишите в переменную numb. 
# Создайте новую матрицу 4х4, заполненную числами от 0 до numb-1. 
# С помощью команды отображения данных матрицы в виде квадратов 
# отобразите значения созданной матрицы.

import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

Z = [[1 if i==4 or i==0 or j==4 or j==0 else 0 for j in range(5)] for i in range(5)]
print(*Z, sep='\n')
rank = np.linalg.matrix_rank(Z)
print("Rank -", rank)

Y = np.arange(6,17)
print(Y)
Y = Y[::-1]
print("Reversed -", Y)

numb = Y[6]*rank
print("Number -", numb)

X = np.random.randint(numb-1, size=(4, 4))
print(X)
plt.colorbar(plt.matshow(X))
plt.show()
