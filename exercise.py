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
que1 = input("Хотите изменить фамилию? да/нет: ")
if que1 == "да":
    input_surname = input("Введите фамилию: ")
    student.change_surname(input_surname)
que2 = input("Хотите изменить дату рождения? да/нет: ")
if que2 == "да":
    input_birth = input("Введите дату рождения: ")
    student.change_birth(input_birth)
print("\nИнформация о студенте после изменений:")
student.print_info()
