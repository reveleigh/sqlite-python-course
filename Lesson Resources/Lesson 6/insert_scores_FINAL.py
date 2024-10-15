import sqlite3

def add_test_score():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    student_name = input("Enter student name: ")
    test_name = input("Enter test name: ")
    score = int(input("Enter score: "))

    cursor.execute() # Add the missing code here
    conn.commit()

    print("Score added successfully!")

    cursor.execute() # Add the missing code here
    highest_scorer = cursor.fetchone()

    if highest_scorer:
        print("\nHighest scorer for this test:")
        print("-" * 30)
        print("Student Name:", highest_scorer[0])
        print("Score:", highest_scorer[1])
        print("-" * 30)

    conn.close()

add_test_score()