# 16.11.2021
# необходимо считать список студентов из csv и json файлов
# и найти самого успешного студента группы.
import json

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







