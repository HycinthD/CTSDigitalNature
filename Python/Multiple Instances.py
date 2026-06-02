class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}")

emp1 = Employee("John", 101)
emp2 = Employee("Alice", 102)
emp3 = Employee("Bob", 103)

employees = [emp1, emp2, emp3]

for employee in employees:
    employee.display_info()