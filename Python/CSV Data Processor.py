import csv

def analyze_employee_data():
    try:
        employees = []

        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            employees = [
                {"name": row["name"], "salary": int(row["salary"])}
                for row in reader
            ]

        high_salary = [
            emp for emp in employees
            if emp["salary"] > 50000
        ]

        average_salary = sum(
            emp["salary"] for emp in employees
        ) / len(employees)

        print("Employees with Salary > 50000:")
        for emp in high_salary:
            print(emp)

        print(f"\nAverage Salary: {average_salary:.2f}")

    except FileNotFoundError:
        print("employees.csv not found")

analyze_employee_data()