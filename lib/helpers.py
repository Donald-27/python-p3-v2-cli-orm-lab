from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# Department functions already implemented above...

# Employee functions to implement:


def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(employee)
    else:
        print(f"Employee {id_} not found")


def create_employee():
    try:
        name = input("Enter the employee's name: ").strip()
        job_title = input("Enter the employee's job title: ").strip()
        department_id = input("Enter the employee's department id: ").strip()

        # Check if department exists before creating employee
        if not Department.find_by_id(department_id):
            print("Error creating employee:  department_id must reference a department in the database")
            return

        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if not employee:
        print(f"Employee {id_} not found")
        return

    try:
        name = input("Enter the employee's new name: ").strip()
        job_title = input("Enter the employee's new job title: ").strip()
        department_id = input("Enter the employee's new department id: ").strip()

        if not Department.find_by_id(department_id):
            print("Error updating employee:  department_id must reference a department in the database")
            return

        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id

        employee.update()
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error updating employee: ", exc)


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")


def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f"Department {department_id} not found")
