import sqlite3

def get_average_grade_by_teacher(db_path, teacher_name):
    query = """
    SELECT AVG(g.grade) AS average_grade
    FROM grades g
    JOIN subjects subj ON g.subject_id = subj.id
    JOIN teachers t ON subj.teacher_id = t.id
    WHERE t.teacher_name = ?;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (teacher_name,))
        result = cur.fetchone()

    return result[0] if result else None

if __name__ == "__main__":
    db_path = 'tables.db'  
    teacher_name = 'John'  # ім'я викладача
    average_grade = get_average_grade_by_teacher(db_path, teacher_name)
    
    if average_grade is not None:
        print(f"Average grade given by teacher '{teacher_name}': {average_grade:.2f}")
    else:
        print(f"No grades found for teacher '{teacher_name}'.")
