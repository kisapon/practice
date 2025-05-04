class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    def GetName(self):
        return self.__name
    def GetSurname(self):
        return self.__surname
    def GetRate(self):
        return self.__rate
    def GetDays(self):
        return self.__days
    def GetSalary(self):
        salary = self.__rate * self.__days
        print("Зарплата работника: ", salary)
        return salary
worker = Worker("Иван", "Иванов", 1000, 15)
worker.GetSalary()
