import sqlite3

class Students:
    """описание студента"""
    def __init__(self, name, surname, patronymic, group, rating):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.rating = rating

    def calculate_average(self):
        return round(sum(self.rating) / len(self.rating), 2)

con = sqlite3.connect("StudentsDataBase.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentsDataBase (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
surname TEXT,
patronymic TEXT,
group_name TEXT,
rate1 INTEGER,
rate2 INTEGER,
rate3 INTEGER,
rate4 INTEGER
)""")
con.commit()

def add_student(student):
    cursor.execute(
        """INSERT INTO StudentsDataBase (name, surname, patronymic, group_name, rate1, rate2, rate3, rate4) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (student.name, student.surname, student.patronymic, student.group,
         student.rating[0], student.rating[1], student.rating[2], student.rating[3]))
    con.commit()
    st_id = cursor.lastrowid
    return st_id

def view_all_students():
    cursor.execute("""SELECT * FROM StudentsDataBase""")
    items = cursor.fetchall()
    students_data = []
    for item in items:
        students_data.append(item)
    return students_data

def view_student(st_id):
    cursor.execute("""SELECT * FROM StudentsDataBase WHERE id = ?""", (st_id,))
    item = cursor.fetchone()
    if item:
        return item
    else:
        return None

def editing_student(st_id, student):
    cursor.execute("""UPDATE StudentsDataBase SET name = ?, surname = ?, patronymic = ?, group_name = ?, 
                        rate1 = ?, rate2 = ?, rate3 = ?, rate4 = ? WHERE id = ?""",
                       (student.name, student.surname, student.patronymic, student.group, student.rating[0],
                        student.rating[1], student.rating[2], student.rating[3], st_id))
    con.commit()

def delete_student(st_id):
    cursor.execute("""SELECT * FROM StudentsDataBase WHERE id = ?""", (st_id,))
    item = cursor.fetchone()
    if item:
        cursor.execute("DELETE FROM StudentsDataBase WHERE id = ?", (st_id,))
        con.commit()
        print("Студент удален.")
    else:
        print("Студент с таким ID не найден.")

def group_average(group_name):
    cursor.execute("""SELECT AVG((rate1 + rate2 + rate3 + rate4) / 4.0) FROM StudentsDataBase WHERE group_name = ?""", (group_name,))
    result = cursor.fetchone()
    if result and result[0] is not None:
        print("Средний балл студентов этой группы: ", result[0])
    else:
        print("Группа не найдена или в ней нет студентов.")

print("Приложение по работе со студентами.")
while True:
    print("Функционал:")
    print(f"1 -> Добавление нового студента. \n2 -> Просмотр всех студентов."
          f" \n3 -> Просмотр одного студента, включая его средний балл. \n4 -> Редактирование студента."
          f"\n5 -> Удаление студента. \n6 -> Просмотр среднего балла студентов у конкретной группы. \n7 -> Выход.\n")
    try:
        choice = int(input("Выберите функцию: "))
        if choice == 1:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            patronymic = input("Введите отчество: ")
            group = input("Введите группу: ")
            rating = []
            for i in range(1, 5):
                try:
                    rate = int(input(f"Введите новую {i}-ую оценку: "))
                    rating.append(rate)
                except ValueError:
                    print("Введите целое число.")
            student = Students(name, surname, patronymic, group, rating)
            st_id = add_student(student)
            print("Студент добавлен. Его ID:", st_id)

        elif choice == 2:
            students_data = view_all_students()
            if students_data:
                for item in students_data:
                    student = Students(item[1], item[2], item[3], item[4], [item[5], item[6], item[7], item[8]])
                    print(
                        f"ID: {item[0]}\tИмя: {item[1]}\tФамилия: {item[2]}\tОтчество: {item[3]}"
                        f"\tГруппа: {item[4]} \tОценки: [{item[5]}, {item[6]}, {item[7]}, {item[8]}] \tСредний балл: {student.calculate_average()}") #выводим через item а не student
            else:
                print("Нет данных о студентах.")

        elif choice == 3:
            st_id = int(input("Введите ID: "))
            item = view_student(st_id)
            if item:
                student = Students(item[1], item[2], item[3], item[4], [item[5], item[6], item[7], item[8]])
                print(
                    f"ID: {item[0]}\tИмя: {item[1]}\tФамилия: {item[2]}\tОтчество: {item[3]}"
                    f"\tГруппа: {item[4]} \tОценки: {item[5]}, {item[6]}, {item[7]}, {item[8]} \tСредний балл: {student.calculate_average()}") #выводим через item а не student
            else:
                print("Студент с таким ID не найден.")

        elif choice == 4:
            st_id = int(input("Введите ID: "))
            ex_student_item = view_student(st_id)
            if ex_student_item:
                name = input("Введите новое имя: ")
                surname = input("Введите новую фамилию: ")
                patronymic = input("Введите новое отчество: ")
                group = input("Введите новую группу: ")
                rating = []
                for i in range(1, 5):
                    try:
                        rate = int(input(f"Введите новую {i}-ую оценку: "))
                        rating.append(rate)
                    except ValueError:
                        print("Введите целое число.")
                student = Students(name, surname, patronymic, group, rating)
                editing_student(st_id, student)
                print("Студент изменен.")
            else:
                print("Студент с таким ID не найден.")

        elif choice == 5:
            st_id = int(input("Введите ID: "))
            delete_student(st_id)

        elif choice == 6:
            group_name = input("Введите группу: ")
            group_average(group_name)
        elif choice == 7:
            con.close()
            break
        else:
            print("Такой функции нет! Попробуйте снова.")
    except ValueError:
        print("Номер функции - целое число!")
