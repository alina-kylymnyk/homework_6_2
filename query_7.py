import sqlite3

def get_grades_by_group_and_subject(db_path, group_id, subject_name):
    query = """
    SELECT s.student_name, g.grade, g.date_of
    FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN subjects subj ON g.subject_id = subj.id
    WHERE s.group_id = ? AND subj.subject_name = ?;
    """
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(query, (group_id, subject_name))
        results = cur.fetchall()

    return results

if __name__ == "__main__":
    db_path = 'tables.db' 
    group_id = 1  # ID групи
    subject_name = 'Mathematics'  #  назва предмета
    grades = get_grades_by_group_and_subject(db_path, group_id, subject_name)
    
    if grades:
        print(f"Grades for Group ID {group_id} in Subject '{subject_name}':")
        for student_name, grade, date_of in grades:
            print(f"Student: {student_name}, Grade: {grade}, Date: {date_of}")
    else:
        print(f"No grades found for Group ID {group_id} in Subject '{subject_name}'.")
