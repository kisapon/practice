class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def GetSalary(self):
        salary = self.rate * self.days
        print("Зарплата работника: ", salary)
worker = Worker("Иван", "Иванов", 1000, 15)
worker.GetSalary()
