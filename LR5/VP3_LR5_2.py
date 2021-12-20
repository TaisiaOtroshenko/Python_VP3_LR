# Задача 2. Создать 3 класса (базовый) и 2 предка, 
# которые описывают некоторых работников с почасовой оплатой (один из предков) 
# и фиксированной оплатой(второй предок). 
# Описать в базовом классе абстрактный метод для расчета среднемесячной зарплаты. 
# Для «почасовиков» формула для расчета такая: “среднемесячная зарплата=20.8*8*ставка в час”, 
# для работников с фиксированной оплатой “среднемесячная зарплата = фиксированной месячной оплате”. 
# Задание: упорядочить всю последовательность рабочих по убыванию среднемесячной зарплаты. 
# При совпадении зарплаты – упорядочить данные в алфавитном порядке по имени. 
# Вывести идентификатор работника, имя и среднемесячную зарплату для всех элементов списка.

from abc import ABC, abstractmethod

class Worker (ABC):
    idnew = 1
    name = ""
    medSalary = 0
    @abstractmethod
    def salarySize(self):
        pass
    def printWorker(self):
        print("ID -", self.id, "\tИмя -", self.name, "\tСреднемесячная запрлата -", "%.0f" % self.medSalary)

class Hour (Worker):
    hourSize = 0
    def __init__(self, name, size):
        self.id = Worker.idnew
        Worker.idnew+=1
        self.name = name
        self.hourSize = size
        
    def salarySize(self):
        # "среднемесячная зарплата = 20.8*8*ставка в час"
        self.medSalary = 20.8*8*self.hourSize

class Fix (Worker):
    fixSize = 0
    def __init__(self, name, size):
        self.id = Worker.idnew
        Worker.idnew+=1
        self.name = name
        self.fixSize = size
    def salarySize(self):
        # "среднемесячная зарплата = фиксированной месячной оплате"
        self.medSalary = self.fixSize

wks = [Hour("Taisia", 300), Hour("Anfisa", 300), Hour("Andrey", 400), Hour("Evgeniy", 250), Fix("Dmitriy", 45000), Fix("Mariya", 45000), Fix("Alexey", 50000), Fix("Bladimir", 80000)]
for it in wks:
    it.salarySize()
wks = sorted(wks, key=lambda worker: worker.name)
wks = sorted(wks, key=lambda worker: worker.medSalary)
sum = 0
for it in wks:
    it.printWorker()
    sum+=it.medSalary
sum/=len(wks)
print("\tСреднемесячная запрлата по коллективу -", "%.0f" % sum)

