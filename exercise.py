class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def print_info(self):
        print("Первое число: ", self.num1)
        print("Второе число: ", self.num2)
    def sum_even(self):
        summ = self.num1 + self.num2
        print("Сумма чисел: ", summ)
    def maximum_num(self):
        max_num = max(self.num1, self.num2)
        print("Наибольшее число: ", max_num)
        if self.num1 == self.num2:
            print("Числа равны")
numbers = Numbers(5, 2)
numbers.print_info()
numbers.sum_even()
numbers.maximum_num()
