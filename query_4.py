import sqlite3

def get_average_grade(db_path):
    query = """
    SELECT AVG(grade) AS average_grade
    FROM grades;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchone()

    return result

if __name__ == "__main__":
    db_path = 'tables.db'  
    average_grade = get_average_grade(db_path)
    
    if average_grade:
        print(f"Average Grade: {average_grade[0]:.2f}")
    else:
        print("No data found.")
