# Задача 4. Требуется реализовать часть виртуальной машины языка Brainfuck: 
# список из объектов-операций, имеющих метод .execute(), 
# принимающий по ссылке массив памяти и номер активной ячейки. Операции в BF:
# 1.	'>' — перейти к следующей ячейке;
# 2.	'<' — перейти к предыдущей ячейке;
# 3.	'+' — увеличить значение в текущей ячейке на 1;
# 4.	'-' — уменьшить значение в текущей ячейке на 1;
# 5.	'.' — напечатать значение из текущей ячейки,
# 6.	',' — ввести значение и сохранить в текущей ячейке;
# 7.	'[' — если значение текущей ячейки ноль, перейти вперёд по тексту программы 
#               на ячейку, следующую за соответствующей ']' (с учётом вложенности);
# 8.	']' — если значение текущей ячейки не нуль, перейти назад по тексту программы 
#               на символ '[' (с учётом вложенности).
# Применить абстрактный класс для задания операции.

from abc import ABC, abstractmethod, abstractstaticmethod

CODE = [0]
DATE = [0 for i in range(100)]
I = 0
M = 0

#methods
class BF (ABC):
    @abstractstaticmethod
    def execute(self, mass, i):
        pass

class next(BF):
    def execute(self, mass, i):
        i+=1
        return i

class prew(BF):
    def execute(self, mass, i):
        i-=1
        return i

class inc(BF):
    def execute(self, mass, i):
        mass[i]+=1

class dec(BF):
    def execute(self, mass, i):
        mass[i]-=1

class prt(BF):
    def execute(self, mass, i):
        i1 = i
        r1 = mass[i]
        print(chr(mass[i]), end="")

class inp(BF):
    def execute(self, mass, i):
        mass[i] = input("Введите символ: ")[0].encode("utf-8")

class whl(BF):
    def execute(self, mass, i, code, m):
        if(mass[i]==0):
            # перейти вперёд по тексту программы на ячейку, следующую за соответствующей ']' (с учётом вложенности);
            isinside=1
            while(isinside):
                m+=1
                if(code[m] == '['):
                    isinside+=1
                if(code[m] == ']'):
                    isinside-=1
        return m

class whr(BF):
    def execute(self, mass, i, code, m):
        if (mass[i]!=0):
            # перейти назад по тексту программы на символ '[' (с учётом вложенности)
            isinside=1
            while(isinside):
                m-=1
                if(code[m] == ']'):
                    isinside+=1
                if(code[m] == '['):
                    isinside-=1
        return m



# create Hello world in bf code
strch = "Hello world\n"
strint = strch.encode("utf-8")
strplus = [['+'for i in range(el)] for el in strint]
strcode = ""
for it in strplus:
    strcode += "".join(it)+">"
out = "".join([".>"for i in range(len(strch))])
back = "".join(["<"for i in range(len(strch))])
CODE = strcode+"+++++"+"["+back+out+"-]"

CODE = ",>,>,.<.<."


# execution bf code
while (M <len(CODE)):
    if(CODE[M]=='>'):
        I = next().execute(DATE, I)
    elif(CODE[M]=='<'):
        I = prew().execute(DATE, I)
    elif(CODE[M]=="+"):
        inc().execute(DATE, I)
    elif(CODE[M]=='-'):
        dec().execute(DATE, I)
    elif(CODE[M]=='.'):
        prt().execute(DATE, I)
    elif(CODE[M]==','):
        inp().execute(DATE, I)
    elif(CODE[M]=='['):
        M = whl().execute(DATE, I, CODE, M)
    elif(CODE[M]==']'):
        M = whr().execute(DATE, I, CODE, M)
    M+=1
