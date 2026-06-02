import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"

employees = {
    "101": Employee("101", "John", 50000),
    "102": Employee("102", "Alice", 60000)
}

data = {}

for emp_id, emp in employees.items():
    data[emp_id] = {
        "name": emp.name,
        "salary": emp.salary
    }

with open("emps.json", "w") as file:
    json.dump(data, file, indent=4)

with open("emps.json", "r") as file:
    loaded_data = json.load(file)

print("Employees:")
for emp_id, details in loaded_data.items():
    employee = Employee(emp_id, details["name"], details["salary"])
    print(employee)