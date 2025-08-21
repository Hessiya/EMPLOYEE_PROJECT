from validate.validation import validate_name,validate_age, validate_qualification,validate_date_of_joining

class Employee:
     def __init__(self,name:None,age:None,qualification:None,date_of_joining:None,emp_id:None,is_active ="Y"):
          self.__emp_id = emp_id
          self.__name = name
          self.__age = age
          self.__qualification = qualification
          self.__date_of_joining = date_of_joining 
          self.__is_active = is_active

     @property
     def emp_id(self):
          return self.__emp_id

     @property
     def name(self):
          return self.__name 
     @name.setter
     def name(self,value):
          validate_name(value)
          self.__name = value

     @property
     def age(self):
          return self.__age 
     @age.setter
     def age(self,value):
          validate_age(value)
          self.__age = value

     @property
     def qualification(self):
          return self.__qualification 
     @qualification.setter
     def qualification(self,value):
          validate_qualification(value)
          self.__qualification = value

     @property
     def date_of_joining(self):
          return self.__date_of_joining 
     @date_of_joining.setter
     def date_of_joining(self,value):
          validate_date_of_joining(value)
          self.__date_of_joining = value

     @property
     def is_active(self):
          return self.__is_active
     @is_active.setter
     def is_active(self,is_active):
          self.is_active=is_active

     def _str_(self):
          return f"EmployeeID : {self._emp_id},Name:{self.name},Age:{self.age},Qualification:{self.qualification},DateOfJoining:{self.date_of_joining},is_active :{self._is_active}"