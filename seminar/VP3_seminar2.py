# 16.11.2021
# необходимо считать список студентов из csv и json файлов
# и найти самого успешного студента группы.
import json
import csv

def mean(a):
    return sum(a)/len(a)

with open("D:\git_repos\Python_VP3_LR\seminar\students.json", "r", encoding="utf-8") as fjson:
    stmas = json.loads(fjson.read())

st = stmas['students']
print ("Все студенты группы:", *st, sep="\n")

most = st[0]
for it in st:
    if (mean(it['marks'])>mean(most['marks'])):
        most = it
print("Самый успешный студент:", most, sep= "\n")

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







