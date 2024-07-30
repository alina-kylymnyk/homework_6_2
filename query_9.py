import sqlite3

def get_courses_by_student(db_path, student_id):
    query = """
    SELECT DISTINCT subj.subject_name
    FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN subjects subj ON g.subject_id = subj.id
    WHERE s.id = ?;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (student_id,))
        results = cur.fetchall()

    return [row[0] for row in results]

if __name__ == "__main__":
    db_path = 'tables.db'  
    student_id = 1  #ID студента
    courses = get_courses_by_student(db_path, student_id)
    
    if courses:
        print(f"Courses attended by student ID {student_id}:")
        for course in courses:
            print(f"- {course}")
    else:
        print(f"No courses found for student ID {student_id}.")
