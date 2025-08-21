from Dao.abstractclass import EmployeeDaoService
from db.connection import Connection
from models.employee import Employee
from typing import List

class EmployeeDaoImplementation(EmployeeDaoService):
    DISPLAY_ALL = "SELECT * from employees"
    INSERT_EMPLOYEE = "INSERT INTO employees(name,age,qualification,date_of_joining,is_active) VALUES (%s, %s, %s, %s, %s)"
    FIND_BY_ID = "SELECT * from employees WHERE emp_id =%s"
    UPDATE_EMPLOYEE = "UPDATE employees set name=%s, age=%s WHERE emp_id=%s"
    DISABLE_EMPLOYEE = "UPDATE employees set isActive='n' WHERE emp_id = %s"
   

    def __init__(self):
        self.conn = Connection().get_connection()

    def insert_employees(self,employee:Employee)->bool:
        try:
            cursor = self.conn.cursor()  #create a cursor object to connect it with databse
            cursor.execute(self.INSERT_EMPLOYEE, (employee.name,employee.age,employee.qualification,employee.date_of_joining,employee.is_active)) 
            self.conn.commit()
            return cursor.rowcount == 1 
        except Exception as e:
            print("Error inserting employee:",e)
            return False
        finally:
            cursor.close()

    def display_all_employees(self)->List[Employee]:
        employees=[]  #to store the records from db
        try:
            cursor = self.conn.cursor(dictionary=True)  #return data in dic 
            cursor.execute(self.DISPLAY_ALL) #fire the query
            rows = cursor.fetchall()
            for row in rows:
                employees.append(Employee(emp_id = row["emp_id"],    #red names should be same as insert names which v r going to insrt as column name
                                        name = row["name"],
                                        age= row["age"],
                                        qualification = row["qualification"],
                                        date_of_joining =row["date_of_joining"],
                                        is_active=row["is_active"]))
        except Exception as e:
            print("Error fetching employees:",e)
        finally:
            cursor.close()
        return employees

    def find_by_emp_id(self, emp_id:int):
        employee = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.FIND_BY_ID,(emp_id,))    #we put comma bcoz in tuple single value pass cheyumbo we should put comma
            row = cursor.fetchone()
            if row:
                employee =Employee(
                    emp_id = row["emp_id"],    #red names should be same as insert names which v r going to insrt as column name
                    name = row["name"],
                    age= row["age"],
                    qualification = row["qualification"],
                    date_of_joining =row["date_of_joining"],
                    is_active = row["is_active"] )
                
        except Exception as e:
            print("Error finding employee:",e)
        finally:
            cursor.close()
        return employee
    
    def update_employee(self,employee:Employee,emp_id:int)->bool:
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.UPDATE_EMPLOYEE,
                           (employee.name,
                           employee.age,emp_id))
            self.conn.commit()
            return cursor.rowcount ==1
        except Exception as e:
            print("Error updating employee:",e)
            return False
        finally:
            cursor.close()

    
    def disable_employee(self,employee:Employee,emp_id:int)->bool:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.DISABLE_EMPLOYEE,
                           (emp_id,))
            self.conn.commit()
            return cursor.rowcount ==1
        except Exception as e:
            print("Error in Disabling employee:",e)
            return False
        finally:
            cursor.close()