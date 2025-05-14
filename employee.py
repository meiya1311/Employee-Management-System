 
#dictionary to store emp details
employees={}


def add_employee(emp_id,name,age,salary,department):
   employees[emp_id]={"Name":name,"Age":age,"salary":salary,"Department":department}
   


#view employee
def view_employee():
   if employees:
      for emp_id,emp_details in employees.items():

        print(f"ID:{emp_id},Details:{emp_details}")
   else:
      print("No Employees Added Yet!")
      
def update_employee(emp_id,name=None,age=None,salary=None,department=None):
    try:
        if emp_id in employees:
            if name:
                employees[emp_id]["Name"]=name
            if age:
                employees[emp_id]["Age"]=age
            if salary:
                employees[emp_id]["salary"]=salary
            if department:
                employees[emp_id]["Department"]=department
            print(f"Employee {emp_id} Updated Successfully ...!")
      
        else:
            print(f"Employee with ID {emp_id} not found")
    except KeyError as e:
       print(f"Error updating Employee Details:{e}")
def remove_employee(emp_id):
    try:
        emp=employees.pop(emp_id)
        print(f"Employee {emp['Name']}Removed Succesfully...!")
    except KeyError :
        
        print(f"Employee {emp['ID']}is not found...!")
#save to file function
def save_to_file(filename):
   try:
      with open(filename,"w")as file:
         for emp_id,details in employees.items():
            line=f"{emp_id}:->{details['Name']},{details['Age']},{details['salary']},{details['Department']}\n"
            file.write(line)
      print("Employee Data Saved Successfully...")
   except exception as e:
      print(f"Error:{e}")

#load from file
def load_from_file(filename):
   try:
      with open(filename,"r")as file:
         global employees
         employees={}#clear the existing dictionary
         for line in file:
            emp_data=line.strip().split(',')
            emp_id,name,age,salary,department=emp_data

            employees[emp_id]={"Name":name,"Age":age,"salary":salary,"Department":department}

      print("Employee Data Loaded Successfully...")
   except Exception as e:
      print(f"Error:{e}")
   
            
   


#main function
def menu():

    while True:
        print("Welcome to the Employment Management system")
        print("1.Add Employee")
        print("2.View Employee")
        print("3.Update Employee")
        print("4.Delete Employee")
        print("5.Save to file")
        print("6.Load from File")
        print("7.Exit")

        choice=input("Enter Your Choice :")
        if choice=="1":
           emp_id=input("Enter the employee ID:")
           name=input("Enter the employee name:")
           age=input("Enter the employee age:")
           salary=input("Enter the employee salary:")
           department=input("Enter the department:")



           add_employee(emp_id,name,age,salary,department)
        elif choice=="2":
           view_employee()
        elif choice == "3":
           emp_id=input("Enter the Employee ID to Update:")
           name=input("Enter new name (Leave Blank to skip)")or None
           age=input("Enter new age (Leave Blank to skip)")or None
           salary=input("Enter new salary (Leave Blank to skip)")or None
           department=input("Enter new department (Leave Blank to skip)")or None
           update_employee(emp_id,name,age,salary,department)
        elif choice=="4":
           emp_id=input("Enter the Employee ID to Remove:") 
           remove_employee(emp_id)
        elif choice=="5":
           filename=input("Enter file name to save:")
           save_to_file(filename)
        elif choice=="6":
           filename=input("Enter file name to load to:")
           load_from_file(filename)
        elif choice=="7":
           break





menu()
