import random
import csv

print("\t\tВП3_ЛР4 Вариант 4")
print("\tЗадание 1:")
# Определить количество чисел, меньших среднего арифметического в файле
with open("D:\git_repos\Python_VP3_LR\LR4\mas.txt", "w") as ftxt:
    mas=[(str(round(random.randint(0,99)/random.randint(2,10),2))+"\n") for i in range(20)]
    ftxt.writelines(mas)
with open("D:\git_repos\Python_VP3_LR\LR4\mas.txt", "r") as ftxt:
    count = 0 
    mean = 0
    for it in [float(it) for it in ftxt.read().strip().split('\n')]:
        mean += it
        count+=1
    mean/=count
    count = 0
    ftxt.seek(0)
    for it in [float(it) for it in ftxt.read().strip().split('\n')]:
        if it < mean:
            count+=1
print("Количество чисел, меньших среднего арифметического", count)

print("\tЗадание 2:")
# Считать файл, вывести в файл название книг, изданных не позже 1990 года
books = [["Повелитель мух", "1954"], ["Мор, ученик смерти", "1987"], ["Дюна", "1965"], ["Вечера на хуторе близ Диканьки", "1831"], ["Обломов", "1859"], ["Отцы и дети", "1860"], ["Фауст", "1808"], ["Три мушкетёра", "1844"], ["Мастер и Маргарита", "1966"], ["Благие знамения", "1990"], ["Книжный вор", "2005"]]
with open("book.csv", "w", encoding="utf-8", newline="") as fcsv:
    writer = csv.writer(fcsv)
    writer.writerows(books)
with open("book.csv", "r", encoding="utf-8", newline="") as fcsv:
    reader = csv.reader(fcsv)
    rbook = list(reader)
    with open("k.csv", "w", encoding="utf-8", newline="") as k:
        for book in rbook:
            if int(book[1])>1990:
                writer = csv.writer(k)
                writer.writerow(book)
        print("Успешно")
            
print("\tЗадание 3:")
# Вывести данные с файла на консоль с использованием кортежа
with open("D:\git_repos\Python_VP3_LR\LR4\str.txt", "r") as f:
    for line in f:
        t = tuple(line.strip().split(", "))
        print(t)
    print("Second method")
    f.seek(0)
    names  = tuple(f.readline().strip().split(", "))
    surnames = tuple(f.readline().strip().split(", "))
    groups = tuple(f.readline().strip().split(", "))
    print(names, surnames, groups, sep="\n")
