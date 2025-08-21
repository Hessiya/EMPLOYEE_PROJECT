from Dao.abstractclass import EmployeeDaoService
from Dao.abstractImple import EmployeeDaoImplementation
from models.employee import Employee
from datetime import datetime

class EmployeeManagementLib:
    """Handles Employee CRUD logic"""

    dao_service: EmployeeDaoService = EmployeeDaoImplementation()

    @staticmethod
    def display_all():
        employees = EmployeeManagementLib.dao_service.display_all_employees()
        if not employees:
            print("No employees found.")
        for employee in employees:
            print(employee)

    @staticmethod
    def add_employee():
        try:
            name = input("Enter the Employee Name: ")
            age = int(input("Enter the Age: "))
            qualification = input("Enter the Qualification: ")
            doj = input("Enter Date of Joining (dd/MM/yyyy): ")

            # convert string to datetime.date
            util_date = datetime.strptime(doj, "%d/%m/%Y")
            conv_date = util_date.date()

            employee = Employee(
                name=name,
                age=age,
                qualification=qualification,
                date_of_joining=conv_date,
                emp_id=None,  # auto-increment in DB
            )

            if EmployeeManagementLib.dao_service.insert_employees(employee):
                print("Employee inserted successfully.")
            else:
                print("Something went wrong while inserting employee.")
        except Exception as e:
            print("Error while adding employee:", e)

    @staticmethod
    def update_employee():
        try:
            search_id = int(input("Enter the Employee ID to update: "))
            employee = EmployeeManagementLib.dao_service.find_by_emp_id(search_id)
            if not employee:
                print("Employee not found.")
                return
            print("Current Record:", employee)

            confirm = input("Do you want to edit this data? (y/n): ")
            if confirm.lower() == 'y':
                new_name = input("Enter new name (leave blank to keep same): ")
                new_age = input("Enter new age (leave blank to keep same): ")

                if new_name.strip():
                    employee.name = new_name
                if new_age.strip():
                    employee.age = int(new_age)

                if EmployeeManagementLib.dao_service.update_employee(employee, search_id):
                    print("Employee updated successfully.")
                else:
                    print("Something went wrong while updating employee.")
        except Exception as e:
            print("Error while updating employee:", e)

    @staticmethod
    def search_employee():
        try:
            search_id = int(input("Enter the Employee ID to search: "))
            employee = EmployeeManagementLib.dao_service.find_by_emp_id(search_id)
            if not employee:
                print("Employee not found.")
                return
            print(employee)
        except Exception as e:
            print("Error while searching employee:", e)

    @staticmethod
    def disable_employee():
        try:
            search_id = int(input("Enter the Employee ID to disable: "))
            employee = EmployeeManagementLib.dao_service.find_by_emp_id(search_id)
            if not employee:
                print("Employee not found.")
                return
            print("Employee Found:", employee)

            confirm = input("Do you want to disable this employee? (y/n): ")
            if confirm.lower() == 'y':
                if EmployeeManagementLib.dao_service.disable_employee(employee, search_id):
                    print("Employee disabled successfully.")
                else:
                    print("Something went wrong while disabling employee.")
        except Exception as e:
            print("Error while disabling employee:", e)