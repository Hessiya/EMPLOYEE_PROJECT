from db.connection import Connection
from lib.EmployeeLib import EmployeeManagementLib

# def main ():
# #     #Get connection from Singleton
#    conn = DBConnection().get_connection()


# if __name__ =="__main__":
#    main()
def main():

    while True:
        print("\n=====EMPLOYEE MANAGEMNET MENU======")
        print("1. ADD EMPLOYEE")
        print("2. DISPLAY ALL EMPLOYEE")
        print("3. UPDATE EMPLOYEE")
        print("4. SEARCH EMPLOYEE BY ID")
        print("5. DISABLE EMPLOYEE")
        print("6. EXIT")
        choice = input("Enter your choice:")
        if choice == "1":
            EmployeeManagementLib.add_employee()
        elif choice =="2":
            EmployeeManagementLib.display_all()
        elif choice =="3":
            EmployeeManagementLib.update_employee()
        elif choice =="4":
            EmployeeManagementLib.search_employee()
        elif choice =="5":
            EmployeeManagementLib.disable_employee()
        elif choice =="6":
            break
        else:
            print("Invalid choice, try again!!!")

            
if __name__ =="__main__":
    main()