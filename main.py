import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="srividya14",
    database="employee_db"
)

cursor = db.cursor()


print("Database connected successfully!")




# Add Employee
def add_employee():

    emp_id = int(input("Enter Employee ID: "))
    empname = input("Enter Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))

    query = """
    INSERT INTO employee
    (emp_id, empname, department, designation, salary)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        emp_id,
        empname,
        department,
        designation,
        salary
    )

    cursor.execute(query, values)
    db.commit()

    print("Employee added successfully!")


# View Employees
def view_employees():

    cursor.execute("SELECT * FROM employee")

    records = cursor.fetchall()

    if len(records) == 0:
        print("No employees found.")

    else:

        for employee in records:

            print("\n-----------------------------")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1])
            print("Department  :", employee[2])
            print("Designation :", employee[3])
            print("Salary      :", employee[4])
            print("-----------------------------")


# Search Employee
def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    query = "SELECT * FROM employee WHERE emp_id = %s"

    cursor.execute(query, (emp_id,))

    employee = cursor.fetchone()

    if employee:

        print("\n-----------------------------")
        print("Employee ID :", employee[0])
        print("Name        :", employee[1])
        print("Department  :", employee[2])
        print("Designation :", employee[3])
        print("Salary      :", employee[4])
        print("-----------------------------")

    else:
        print("Employee not found.")


# Update Employee
def update_employee():

    emp_id = int(input("Enter Employee ID: "))

    salary = float(input("Enter New Salary: "))

    query = """
    UPDATE employee
    SET salary = %s
    WHERE emp_id = %s
    """

    cursor.execute(query, (salary, emp_id))
    db.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully!")

    else:
        print("Employee not found.")


# Delete Employee
def delete_employee():

    emp_id = int(input("Enter Employee ID: "))

    query = "DELETE FROM employee WHERE emp_id = %s"

    cursor.execute(query, (emp_id,))
    db.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")

    else:
        print("Employee not found.")


# Main Menu
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")