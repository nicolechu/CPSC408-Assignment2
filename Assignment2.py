import sqlite3

conn = sqlite3.connect('Assignment2.sqlite')
c = conn.cursor()


def get_user_input():
    # Display menu options to user
    print("\n1: Display all students")
    print("2: Create new student")
    print("3: Update student major")
    print("4: Update student advisor")
    print("5: Delete student")
    print("6: Search by major")
    print("7: Search by GPA")
    print("8: Search by advisor")
    print("Q: Quit")

    return input("Choose number from menu: ")


# Display all students & their attributes
def display_all_students():
    # display attributes except isDeleted, display only students who aren't deleted
    c.execute("SELECT StudentId,FirstName,LastName,Major,GPA,FacultyAdvisor FROM Student WHERE isDeleted <> 1")
    all_rows = c.fetchall()
    return all_rows


# Create students
def create_student():
    # retrieve user input for every attribute
    f_name = input("Enter Student First Name: ")
    l_name = input("Enter Student Last Name: ")

    # validate user input for GPA is a float
    while True:
        gpa = input("Enter Student GPA: ")
        try:
            gpa = float(gpa)
            break;
        except ValueError:
            print("Invalid input. Numbers only.")

    major = input("Enter Student Major: ")
    advisor = input("Enter Student Advisor: ")



    # use user input to insert new student, set isDeleted to 0 (false)
    c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'isDeleted')"
              "VALUES (?, ?, ?, ?, ?, ?)", (f_name, l_name, gpa, major, advisor, 0))
    conn.commit()
    sid = c.lastrowid
    return "Student created w/ ID", sid


# Update students (major & advisor only)
def update_major():
    # retrieve user input to retrieve Student to be updated & new major
    stu_id = input("Enter Student ID: ")
    major = input("Enter Student's new major: ")

    c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (major, stu_id))
    conn.commit()
    return "Student major updated"


def update_advisor():
    # retrieve user input to retrieve Student to be updated & new advisor
    stu_id = input("Enter Student ID: ")
    advisor = input("Enter Student's new advisor: ")

    c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (advisor, stu_id))
    conn.commit()
    return "Student advisor updated"


# Delete students by ID
def delete_student():
    # retrieve user input to retrieve Student to be deleted
    stu_id = input("Enter Student ID: ")

    # perform soft delete (isDeleted set to 1)
    c.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1, stu_id))
    conn.commit()
    return "Student deleted"


# Search & display students by Major, GPA & Advisor
def search_major():
    major = input("Enter major to search: ")
    input_param = (major,)

    c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE isDeleted <> 1 AND Major = ?', input_param)
    all_rows = c.fetchall()
    return all_rows


def search_gpa():
    gpa = input("Enter GPA to search: ")

    c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE isDeleted <> 1 AND GPA = ?', gpa)
    all_rows = c.fetchall()
    return all_rows


def search_advisor():
    advisor = input("Enter Faculty Advisor to search: ")
    input_param = (advisor,)

    c.execute('SELECT StudentId, FirstName, LastName, Major, GPA, FacultyAdvisor FROM Student WHERE isDeleted <> 1 AND FacultyAdvisor = ?', input_param)
    all_rows = c.fetchall()
    return all_rows


user = ''
while user != 'Q':
    user = get_user_input()

    if user == '1':
        print(display_all_students())
    elif user == '2':
        print(create_student())
    elif user == '3':
        print(update_major())
    elif user == '4':
        print(update_advisor())
    elif user == '5':
        print(delete_student())
    elif user == '6':
        print(search_major())
    elif user == '7':
        print(search_gpa())
    elif user == '8':
        print(search_advisor())
    elif user == 'Q':
        print("Bye.")
        quit()
    else:
        print("Invalid input.")
