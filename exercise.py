import sqlite3

class Students:
    """описание студента"""
    def __init__(self, name, surname, patronymic, group, rating):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.rating = rating

con = sqlite3.connect("StudentsDB.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS StudentsDB (
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

def add_student():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    group = input("Введите группу: ")
    rating = []
    for i in range(1, 5):
        rate = int(input(f"Введите {i}-ую оценку: "))
        rating.append(rate)
    cursor.execute("""INSERT INTO StudentsDB (name, surname, patronymic, group_name, rate1, rate2, rate3, rate4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
(name, surname, patronymic, group, rating[0], rating[1], rating[2], rating[3]))
    con.commit()
    st_id = cursor.lastrowid
    print("Студент добавлен. Его ID:", st_id)

def view_all_students():
    cursor.execute("""SELECT * FROM StudentsDB""")
    items = cursor.fetchall()
    for item in items:
        print(f"ID: {item[0]}\tИмя: {item[1]}\tФамилия: {item[2]}\tОтчество: {item[3]}"
              f"\tГруппа: {item[4]} \tОценки: [{item[5]}, {item[6]}, {item[7]}, {item[8]}]")

def view_student():
    student_id = input("Введите ID студента: ")
    cursor.execute("""SELECT * FROM StudentsDB WHERE id = ?""", (student_id,))
    item = cursor.fetchone()
    if item:
        average = round(((float(item[5]) + float(item[6]) + float(item[7]) + float(item[8])) / 4), 2)
        print(f"ID: {item[0]}\tИмя: {item[1]}\tФамилия: {item[2]}\tОтчество: {item[3]}"
              f"\tГруппа: {item[4]}\tОценки: [{item[5]}, {item[6]}, {item[7]}, {item[8]}]\t Средний балл: {average}")
    else:
        print("Студент с таким ID не найден.")

def editing_student():
    student_id = input("Введите ID студента: ")
    cursor.execute("""SELECT * FROM StudentsDB WHERE id = ?""", (student_id,))
    item = cursor.fetchone()
    if item:
        name = input("Введите новое имя: ")
        surname = input("Введите новую фамилию: ")
        patronymic = input("Введите новое отчество: ")
        group = input("Введите новую группу: ")
        rating = []
        for i in range(1, 5):
            rate = int(input(f"Введите новую {i}-ую оценку: "))
            rating.append(rate)
        cursor.execute("""UPDATE StudentsDB SET name = ?, surname = ?, patronymic = ?, group_name = ?, 
                    rate1 = ?, rate2 = ?, rate3 = ?, rate4 = ? WHERE id = ?""",
        (name, surname, patronymic, group, rating[0], rating[1], rating[2], rating[3], student_id))
        con.commit()
        print("Студент изменен.")
    else:
        print("Студент с таким ID не найден.")

def delete_student():
    student_id = input("Введите ID студента: ")
    cursor.execute("""SELECT * FROM StudentsDB WHERE id = ?""", (student_id,))
    item = cursor.fetchone()
    if item:
        cursor.execute("DELETE FROM StudentsDB WHERE id = ?", (student_id,))
        print("Студент удален.")
    else:
        print("Студент с таким ID не найден.")
    con.commit()

# def average_rating():

print("Приложение по работе со студентами.")
while True:
    print("Функционал:")
    print(f"1 -> Добавление нового студента. \n2 -> Просмотр всех студентов."
          f" \n3 -> Просмотр одного студента, включая его средний балл. \n4 -> Редактирование студента."
          f"\n5 -> Удаление студента. \n6 -> Просмотр среднего балла студентов у конкретной группы. \n7 -> Выход.")
    choice = input("Выберите функцию: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_students()
    elif choice == '3':
        view_student()
    elif choice == '4':
        editing_student()
    elif choice == '5':
        delete_student()
    elif choice == '7':
        con.close()
        break
    else:
        print("Такой функции нет! Попробуйте снова.")