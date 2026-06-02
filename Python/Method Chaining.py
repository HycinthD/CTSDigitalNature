class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary >= 0:
            self.salary = salary
        return self

    def apply_raise(self, amount):
        if amount > 0:
            self.salary += amount
        return self

    def display_salary(self):
        print(f"Final Salary: {self.salary}")
        return self

employee = Employee("John")

employee.set_salary(50000).apply_raise(5000).display_salary()