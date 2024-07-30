import sqlite3

def get_students_by_group(db_path, group_id):
    query = """
    SELECT student_name
    FROM students
    WHERE group_id = ?;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (group_id,))
        results = cur.fetchall()

    return results

if __name__ == "__main__":
    db_path = 'tables.db'  
    group_id = 1  # ID групи, для якої потрібно знайти студентів
    students = get_students_by_group(db_path, group_id)
    
    if students:
        print(f"Students in Group ID {group_id}:")
        for student in students:
            print(student[0])
    else:
        print(f"No students found in Group ID {group_id}.")
