class Class:
    def __init__(self, attribute1=None, attribute2=None):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        print("Объект создан с значениями:", self.attribute1, "и", self.attribute2)

    def __del__(self):
        print("Объект с", self.attribute1, "и", self.attribute2,"удалён")

#демонстрация ввозможностей класса
object1 = Class("значение1", "значение2")
object2 = Class() #значения по умолчанию
object1.attribute1 = "новое значение1"
object1.attribute2 = "новое значение2"
print("Новые объекты:", object1.attribute1, "и", object1.attribute2)
del object1
del object2




