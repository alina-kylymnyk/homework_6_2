import sqlite3

def get_top_student_for_subject(db_path, subject_id):
    query = """
    SELECT student_id, AVG(grade) AS average_grade
    FROM grades
    WHERE subject_id = ?
    GROUP BY student_id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (subject_id,))
        result = cur.fetchone()

    return result

if __name__ == "__main__":
    db_path = 'tables.db'  
    subject_id = 1  
    top_student = get_top_student_for_subject(db_path, subject_id)
    
    if top_student:
        student_id, average_grade = top_student
        print(f"Student ID: {student_id}, Average Grade: {average_grade:.2f}")
    else:
        print("No data found for the given subject ID.")
