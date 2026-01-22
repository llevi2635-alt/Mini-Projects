class Employee:
    def __init__(self, emp_id, name, salary, role):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.role = role

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.salary},{self.role}"


FILE_NAME = "employees.txt"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")
    role = input("Enter Role: ")

    emp = Employee(emp_id, name, salary, role)

    with open(FILE_NAME, "a") as file:
        file.write(str(emp) + "\n")

    print("✅ Employee added successfully\n")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()
            if not employees:
                print("No employees found\n")
                return

            print("\n--- Employee List ---")
            for emp in employees:
                emp_id, name, salary, role = emp.strip().split(",")
                print(f"ID: {emp_id}, Name: {name}, Salary: {salary}, Role: {role}")
            print()
    except FileNotFoundError:
        print("No employee file found\n")


def search_employee():
    search_id = input("Enter Employee ID to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for emp in file:
                emp_id, name, salary, role = emp.strip().split(",")
                if emp_id == search_id:
                    print(f"\nFound Employee:")
                    print(f"ID: {emp_id}, Name: {name}, Salary: {salary}, Role: {role}\n")
                    found = True
                    break
        if not found:
            print("❌ Employee not found\n")
    except FileNotFoundError:
        print("Employee file not found\n")


def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    employees = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            employees = file.readlines()

        with open(FILE_NAME, "w") as file:
            for emp in employees:
                emp_id = emp.split(",")[0]
                if emp_id != delete_id:
                    file.write(emp)
                else:
                    deleted = True

        if deleted:
            print("✅ Employee deleted successfully\n")
        else:
            print("❌ Employee not found\n")

    except FileNotFoundError:
        print("Employee file not found\n")


def main():

    print("===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        print("Exiting program 👋")

    else:
        print("❌ Invalid choice\n")


main()
