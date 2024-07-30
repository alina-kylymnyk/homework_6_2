import sqlite3

def get_top_students(db_path):
    query = """
    SELECT student_id, AVG(grade) AS average_grade
    FROM grades
    GROUP BY student_id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query)
        results = cur.fetchall()

    return results

if __name__ == "__main__":
    db_path = 'tables.db'  
    top_students = get_top_students(db_path)
    
    print("Top 5 students with the highest average grades:")
    for student_id, average_grade in top_students:
        print(f"Student ID: {student_id}, Average Grade: {average_grade:.2f}")
