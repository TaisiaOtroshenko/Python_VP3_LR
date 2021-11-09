# Задача 1. Создайте класс Geolocation, содержащий метод forward для изменения координат при движении по оси Ох и Oy, метод decline -для изменения координат по осям Ох, Oy,Oz, метод printPosition – для печати координат.  Создайте класс-наследник aircraft и определите на нём метод wing, печатающий сообщение о том, что у самолёта 2 крыла. Создайте класс-наследник aircraft, переопределяющий метод wing. Сместите самолёт и вертолёт на произвольные расстояния и выведите  сообщение о количестве крыльев и координатах летательных аппаратов.
class Geolocation:
    x = 0
    y = 0
    z = 0
    def forward(self, x, y):
            self.x = x
            self.y = y
    def decline(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
    def printPosition(self):
            print("Координаты по х =", self.x, "y =", self.y, "z =", self.z)

class Aircraft(Geolocation):
    def wing(self):
        print("У самолета 2 крыла")
class Helicopter(Aircraft):
    def wing(self):
        print("У вертолета нет крыльев. У него лопасти, дурачок")

fly1 = Aircraft()
fly1.wing()
fly1.printPosition()
fly2 = Helicopter()
fly2.wing()
fly2.printPosition()
print("Перестановка")
fly1.forward(3,8)
fly2.decline(4,4,10)
fly1.wing()
fly1.printPosition()
fly2.wing()
fly2.printPosition()
