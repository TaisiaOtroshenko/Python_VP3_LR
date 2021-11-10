# 10.11.2021
# задача1. С клавиатуры в одной строке вводится произвольное количество вещественных чисел. 
# Запишите их в файл, расположив каждое число на отдельной строке.

# задача2. Дан файл, полученный на выходе задачи №1:
# загрузите список чисел;
# вычислите их сумму и максимум и допишите их в файл.
# Выполнив программу несколько раз, убедитесь, что новые значения учитываются при подсчете.

with open("D:\git_repos\Python_VP3_LR\seminar\mas_f_sum_max.txt", "w") as f:
    f.write(input("Введите строку вещественных чисел: ").replace(" ", "\n"))

def addSumMax():
    with open("D:\git_repos\Python_VP3_LR\seminar\mas_f_sum_max.txt", "r") as f:
        l = [float(it) for it in f.readlines()]
        with open("D:\git_repos\Python_VP3_LR\seminar\mas_f_sum_max.txt", "a") as fadd:
            fadd.write("\n"+"%.2f" % sum(l)+"\n"+"%.2f" % max(l))

addSumMax()
addSumMax()
addSumMax()
