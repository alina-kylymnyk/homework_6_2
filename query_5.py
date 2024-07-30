import sqlite3

def get_courses_by_teacher(db_path, teacher_id):
    query = """
    SELECT subject_name
    FROM subjects
    WHERE teacher_id = ?;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (teacher_id,))
        results = cur.fetchall()

    return results

if __name__ == "__main__":
    db_path = 'tables.db'  
    teacher_id = 1  # ID викладача, для якого потрібно знайти курси
    courses = get_courses_by_teacher(db_path, teacher_id)
    
    if courses:
        print(f"Courses taught by Teacher ID {teacher_id}:")
        for course in courses:
            print(course[0])
    else:
        print(f"No courses found for Teacher ID {teacher_id}.")
