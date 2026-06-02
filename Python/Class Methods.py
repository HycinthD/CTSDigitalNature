class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_data):
        try:
            name, salary = emp_data.split(",")

            if not name.strip() or int(salary) < 0:
                print("Invalid employee data")
                return None

            return cls(name.strip(), int(salary))

        except ValueError:
            print("Invalid employee data")
            return None

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

employee = Employee.from_string("Shubh,75000")

if employee:
    employee.display_info()