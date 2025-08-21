import re
from datetime import datetime

def validate_name(name: str) -> bool:
    """Name: only alphabets and spaces, length 2–30"""
    if not isinstance(name, str):
        return False
    pattern = re.compile(r"^[A-Za-z ]{2,30}$")
    return bool(pattern.match(name))

def validate_age(age: int) -> bool:
    """Employee age: between 18 and 65"""
    return isinstance(age, int) and 18 <= age <= 65

def validate_qualification(qualification: str) -> bool:
    """Qualification: alphabets, spaces, dots, length 2-20"""
    pattern = re.compile(r"^[A-Za-z. ]{2,20}$")
    return bool(pattern.match(qualification))

def validate_date_of_joining(date_of_joining: str) -> bool:
    """Joining date: valid date in YYYY-MM-DD format, not future"""
    try:
        date_obj = datetime.strptime(date_of_joining, "%d/%m/%Y").date()
        return date_obj <= datetime.today().date()
    except ValueError:
        return False
    


# from datetime import datetime, date
# import re

# def validate_name(name):
#     if not (isinstance(name,str) and len(name.strip())<3 and re.fullmatch(r"[A-Za-z_]+",name.strip())):
#         raise ValueError("Name must be at least 3 characers and contain only alphabets and spaces")
#     return True

# def validate_age(age):
#     if not (isinstance(age,int) and (18 <= age <=60)):
#         raise ValueError("Age must be an Integer between 18 and 60")
#     return True

# def validate_qualification(qualification):
#     if not (isinstance(qualification,str) and qualification.strip()):
#         raise ValueError("Invalid Qualification")
#     return True

# def validate_date_of_joining(date_of_joining):
#     try:
#         d = datetime.strptime(date_of_joining,"%d/%m/%y").date()
#         if d > date.today():
#             raise ValueError
#     except:
#         raise ValueError("Invalid Date")
#     return True