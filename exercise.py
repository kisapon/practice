class Student:
    def __init__(self, surname, birth, group, rating):
        self.surname = surname
        self.birth = birth
        self.group = group
        self.rating = rating
    def change_surname(self, input_surname):
        self.surname = input_surname
    def change_birth(self, input_birth):
        self.birth = input_birth
    def change_group(self, input_group):
        self.group = input_group
    def print_info(self):
        print("Фамилия:", self.surname)
        print("Дата рождения:", self.birth)
        print("Группа:", self.group)
        print("Успеваемость:", self.rating)
student = Student("Иванов", "01.01.2007", 632, [3, 5, 2, 4, 5])
print("Информация о студенте:")
student.print_info()
print()
input_surname = input("Введите фамилию: ")
student.change_surname(input_surname)
input_birth = input("Введите дату рождения: ")
student.change_birth(input_birth)
input_group = input("Введите группу: ")
student.change_group(input_group)
print("\nИнформация о студенте после изменений:")
student.print_info()
