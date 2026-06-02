def get_salary(data, department, employee):
    if department not in data:
        print("Department not found")
        return

    if employee not in data[department]:
        print("Employee not found")
        return

    print(f"Salary: {data[department][employee]}")

employees = {
    "IT": {
        "John": 50000,
        "Alice": 60000
    },
    "HR": {
        "Bob": 45000
    }
}

get_salary(employees, "IT", "Alice")