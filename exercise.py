class Counter:
    def __init__(self):
        self.counter = 0
    def increase(self):
        self.counter += 1
        return self.counter
    def decrease(self):
        self.counter -= 1
        return self.counter
    def print_info(self):
        return self.counter
counter_now = Counter()
counter_now.increase()
print("Значение счетчика после увеличения: ", counter_now.print_info())
counter_now.decrease()
print("Значение счетчика после уменьшения: ", counter_now.print_info())
print("Состояние счетчика: ", counter_now.print_info())
