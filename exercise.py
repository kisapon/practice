class Train:
    def __init__(self, name, number, time):
        self.name = name
        self.number = number
        self.time = time
    def print_info(self):
        print("Пункт назначения: ", self.name)
        print("Номер поезда : ", self.number)
        print("Время отправления: ", self.time)
train1 = Train("Томск", 112, "21:10")
train2 = Train("Москва", 331, "08:30")
train3 = Train("Пермь", 123, "17:50")
trains = [train1, train2, train3]
num = input("Введите номер поезда: ")
found = False
for i in trains:
    if i.number == int(num):
        i.print_info()
        found = True
        break
if not found:
    print("Нет поезда с таким номером")
