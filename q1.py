

employees = []
l=[]
print(''''1.addingemployee
            2.highest paid employee
            3.display employees
            4.Exit''')
n= int(input('enter an option'))


def add_employee(employee_id, name, position, salary):
    employee_tuple = (employee_id, name, position, salary)
    employees.append(employee_tuple)

def find_highest_paid():
    for i in employees:
        l.append(i[3])
    a = l.index(max(l))
    q= employees[a]
    print('Highest paid employee :')
    print("Employee ID:", int(q[0]))
    print("Name:", q[1])
    print("Position:", q[2])
    print("Salary:", q[3])
    print("")


        
def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("Details of all employees:")
    for employee in employees:
        
        print("Employee ID:", employee[0])
        print("Name:", employee[1])
        print("Position:", employee[2])
        print("Salary:", employee[3])
        print("")

add_employee(1, "John Doe", "Manager", 50000)
add_employee(2, "Jane Smith", "Developer", 60000)
add_employee(3, "Bob Johnson", "Designer", 55000)

display_employees()
find_highest_paid()


