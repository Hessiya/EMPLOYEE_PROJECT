from abc import ABC, abstractmethod
from typing import List
from models.employee import Employee

class EmployeeDaoService(ABC):
    @abstractmethod
    def display_all_employees(self)->List[Employee]:
        pass

    @abstractmethod
    def insert_employees(self, employee:Employee)->bool:
        pass

    @abstractmethod
    def find_by_emp_id(self, emp_id:int) ->Employee:   # fixed
        pass

    @abstractmethod
    def update_employee(self, employee:Employee, emp_id:int)->bool:  # fixed
        pass

    @abstractmethod
    def disable_employee(self, employee:Employee, emp_id:int)->bool:  # fixed
        pass