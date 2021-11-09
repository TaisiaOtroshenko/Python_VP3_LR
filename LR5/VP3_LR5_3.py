# Задача 3. Создать класс Mail и описать в нем имя отправителя, имя получателя, место получения и место отправления, при этом место отправления и получения могут быть заданы индексами(целым числом), либо названием города(строкой). Описать метод travel, определяющий покинет ли письмо пределы города (места получения и отправления отличаются).

class Mail:
    sender = ""
    recipient = ""   
    place_departure = ""
    place_receipt = ""
    def __init__(self, sender, recipient, place_departure, place_receipt):
        self.sender= sender
        self.recipient = recipient
        self.place_departure = place_departure
        self.place_receipt = place_receipt
    def travel(self):
        if (self.place_departure==self.place_receipt):
            print("Письмо не покинет город")
        else:
            print("Письмо покинет город")
    def print(self):
        print("Имя отправителя -", self.sender, "\nИмя получателя -", self.recipient, "\nМесто получения -", self.place_departure, "\nМесто отправления -", self.place_receipt)

m1 = Mail("Taisia", "Olga", "Kaluga", "Kaluga")
m1.print()
m1.travel()
m2 = Mail("Taisia", "Olga", 249030, 245030)
m2.print()
m2.travel()
