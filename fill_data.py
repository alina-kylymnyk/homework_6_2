import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 20

def generate_fake_data(number_groups, number_students, number_teachers, number_subjects, number_grades):
    fake_groups = []  
    fake_students = []  
    fake_teachers = [] 
    fake_subjects = [] 
    fake_grades = []  

    fake_data = Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.word())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.word())

    for student_id in range(1, number_students + 1):
        for subject_id in range(1, number_subjects + 1):
            for _ in range(random.randint(5, number_grades)):
                grade = random.randint(1, 5)
                date_of = fake_data.date_between(start_date='-2y', end_date='today')
                fake_grades.append((student_id, subject_id, grade, date_of))


    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_grades


def prepare_data(groups, students, teachers, subjects):
    for_groups = [(group,) for group in groups]

    for_students = [(student, random.choice(range(1, NUMBER_GROUPS + 1))) for student in students]

    for_teachers = [(teacher,) for teacher in teachers]

    for_subjects = [(subject, random.choice(range(1, NUMBER_TEACHERS + 1))) for subject in subjects]

    for_grades = grades
    
    return for_groups, for_students, for_teachers, for_subjects, for_grades


def insert_data_to_db(groups, students, teachers, subjects, grades):
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name) VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(student_name, group_id) VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name) VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id) VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        con.commit()

if __name__ == "__main__":
    groups, students, teachers, subjects, grades = generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_GRADES)
    groups, students, teachers, subjects, grades = prepare_data(groups, students, teachers, subjects)
    insert_data_to_db(groups, students, teachers, subjects, grades)

print("Database created and filled with random data!")




















# Підключення до бази даних
conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

# Заповнення таблиці groups
groups = ['Group A', 'Group B', 'Group C']
for group in groups:
    cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group,))

# Заповнення таблиці teachers
teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute('INSERT INTO teachers (teacher_name) VALUES (?)', (teacher,))

# Заповнення таблиці subjects
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History']
for subject in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

# Заповнення таблиці students
students = []
group_ids = [i for i in range(1, len(groups) + 1)]
for _ in range(30):
    name = fake.name()
    group_id = random.choice(group_ids)
    cursor.execute('INSERT INTO students (student_name, group_id) VALUES (?, ?)', (name, group_id))
    students.append((name, group_id))

# Заповнення таблиці grades
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)

for student_id in range(1, len(students) + 1):
    for _ in range(20):
        subject_id = random.randint(1, len(subjects))
        grade = random.randint(1, 5)
        date_of = random_date(start_date, end_date).strftime('%Y-%m-%d')
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date_of))

# Збереження змін і закриття з'єднання
conn.commit()
conn.close()
