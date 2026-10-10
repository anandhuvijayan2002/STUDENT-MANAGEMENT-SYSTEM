import sqlite3
conn = sqlite3.connect("student_management.db")
cursor = conn.cursor()
 
 # Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")
# Default users
cursor.execute("""
INSERT OR IGNORE INTO users (username, password, role)
VALUES ('teacher', '1234', 'teacher')
""")

cursor.execute("""
INSERT OR IGNORE INTO users (username, password, role)
VALUES ('student', '1234', 'student')
""")

conn.commit()
# ------------------------------- LOGIN -------------------------------------------------




def login():

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Teacher Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "3":
        print("Thank you!")
        return False

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        role = result[0]

        if role == "teacher":
            teacher_menu()

        elif role == "student":
            student_menu()

    else:
        print("Invalid username or password!")

    return True


# ---------------- TEACHER MENU ----------------
def teacher_menu():

    while True:
        print("\n================================")
        print("         TEACHER MENU")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Enter Marks")
        print("6. Logout")

        choice = input("Enter your choice: ")

        # Add Student
        if choice == "1":

            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")

            cursor.execute("""
            INSERT INTO students (name, age, course, marks)
            VALUES (?, ?, ?, ?)
            """, (name, age, course, 0))

            conn.commit()

            print("Student added successfully!")

        # View Students
        elif choice == "2":

            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            print("\nID | Name | Age | Course | Marks")
            print("----------------------------------------")

            for student in students:
                print(student)

        # Update Student
        elif choice == "3":

            student_id = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")

            cursor.execute("""
            UPDATE students
            SET name=?, age=?, course=?
            WHERE id=?
            """, (name, age, course, student_id))

            conn.commit()

            print("Student updated successfully!")

        # Delete Student
        elif choice == "4":

            student_id = int(input("Enter student ID: "))

            cursor.execute(
                "DELETE FROM students WHERE id=?",
                (student_id,)
            )

            conn.commit()

            print("Student deleted successfully!")

        # Enter Marks
        elif choice == "5":

            student_id = int(input("Enter student ID: "))
            marks = int(input("Enter marks: "))

            cursor.execute(
                "UPDATE students SET marks=? WHERE id=?",
                (marks, student_id)
            )

            conn.commit()

            print("Marks updated successfully!")

        # Logout
        elif choice == "6":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


# ---------------- STUDENT MENU ----------------
def student_menu():

    username = "student"

    while True:

        print("\n================================")
        print("         STUDENT MENU")
        print("================================")
        print("1. View Students")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            print("\nID | Name | Age | Course | Marks")
            print("----------------------------------------")

            for student in students:
                print(student)

        elif choice == "2":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


# ---------------- MAIN PROGRAM ----------------
while True:

    continue_program = login()

    if not continue_program:
        break


conn.close()
