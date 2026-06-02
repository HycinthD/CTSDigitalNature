# cognizant-python-_exercise-
## EX:01:Simple Hello World 
## code:
```
print("Hello World!")
```
## output:
<img width="1267" height="105" alt="image" src="https://github.com/user-attachments/assets/a957fb80-2aed-4fd5-8e86-01ebbc86a3db" />


## EX:02:Jupyter Notebook 
## code:
```
print("Hello from Jupyter!")

```
## output:
<img width="783" height="315" alt="image" src="https://github.com/user-attachments/assets/109fe388-5c19-436c-b27f-d11eab873cc8" />

## EX:03:VS Code Setup 
## code:
```
print("Hello World")
```
## output:
<img width="305" height="51" alt="image" src="https://github.com/user-attachments/assets/bfc22fae-08d1-4686-8b5b-f9394c30a0a9" />


## EX:04:Float Precision 
## code:
```
num = 10.56789

print("Original:", num)
print("2 decimal places:", round(num, 2))
print("3 decimal places:", round(num, 3))

```
## output:
<img width="1271" height="282" alt="image" src="https://github.com/user-attachments/assets/668868e7-e70a-4a8a-9cab-01cceb7ec561" />

## EX:05:Multiple Assignment
## code:
```
def display_coordinates(coords):
    if not isinstance(coords, tuple) or len(coords) != 2:
        print("Invalid coordinates")
        return

    x, y = coords  # Multiple assignment
    print(f"Coordinates: ({x}, {y})")

coordinates = (10, 20)
display_coordinates(coordinates)
```
## output:
<img width="1333" height="86" alt="image" src="https://github.com/user-attachments/assets/e4de5c34-ba0c-42c5-8467-0947e0df7494" />


## EX:06:Modulo Operator 
## code:
```
def evenorodd(n):
    if n%2 == 0: return "The number is even"
    return "The number is odd"

n = int(input("Enter the number: "))
t = evenorodd(n)
print(t)
    
```
## output:
<img width="521" height="181" alt="image" src="https://github.com/user-attachments/assets/f4f77938-1929-4656-88ef-a6d39369a484" />


## EX:07:Floor Division
## code:
```
def split_bill(total_bill, people):
    if total_bill < 0 or people <= 0:
        print("Invalid input")
        return

    share = total_bill // people
    print(f"Individual Share: {share}")

total_bill = 1250
people = 4

split_bill(total_bill, people)
```
## output: 
<img width="520" height="128" alt="image" src="https://github.com/user-attachments/assets/9fee2a46-55cd-43ab-aeaa-bd89dc61419b" />


## EX:08:Min max
## code:
```
def find_salary_range(salaries):
    if not salaries:
        print("Invalid salary list")
        return

    lowest_salary = min(salaries)
    highest_salary = max(salaries)

    print(f"Lowest Salary: {lowest_salary}")
    print(f"Highest Salary: {highest_salary}")

salaries = [50000, 75000, 62000, 95000]

find_salary_range(salaries)

```
## output:
<img width="519" height="157" alt="image" src="https://github.com/user-attachments/assets/8b1bb6f0-b7cc-4306-a80f-a5e637f049ae" />



## EX:09: String
## code:
```
text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
```
## output:
<img width="1066" height="130" alt="image" src="https://github.com/user-attachments/assets/49ecf2f9-5851-4232-b0f2-290b4f78444c" />


## EX:10 Numeric Input
## code:
```
def next_year_age():
    age = input("Enter your age: ")

    if not age.isdigit():
        print("Invalid age")
        return

    age = int(age)
    print(f"Next year you'll be {age + 1}")

next_year_age()
```
## output:
<img width="515" height="159" alt="image" src="https://github.com/user-attachments/assets/5f3f91f3-75cf-4799-882f-bdafe19799d9" />


## EX:11 Float Input
## code:
```
def kg_to_lbs():
    weight = input("Enter weight in kilograms: ")

    try:
        kg = float(weight)

        if kg < 0:
            print("Invalid weight")
            return

        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Invalid input")

kg_to_lbs()256
```
## output:
<img width="516" height="164" alt="image" src="https://github.com/user-attachments/assets/f5bdc6bf-693f-4b82-a6e7-296e79ef88ae" />


## EX:12 Simple if
## code:
```
def check_pass(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    if marks >= 50:
        print("Pass")

marks = 75
check_pass(marks)
```
## output:
<img width="515" height="133" alt="image" src="https://github.com/user-attachments/assets/d98c099b-204c-45f2-a2df-abfbd6f3053d" />


## EX:13 if-elis-else
## code:
```
def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"Score: {score}")
    print(f"Grade: {grade}")

score = 88
assign_grade(score)
```
## output:
<img width="512" height="152" alt="image" src="https://github.com/user-attachments/assets/19c5d31a-16db-427d-a4e0-c2ca0aab7b89" />


## EX:14 if else
## code:
```
def check_even_odd(num):
    if not isinstance(num, int):
        print("Invalid input")
        return

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = 8
check_even_odd(num)
```
## output:
<img width="517" height="125" alt="image" src="https://github.com/user-attachments/assets/d851b52d-c246-4e44-b7b6-910e3fe4d440" />


## EX:15 Nested If
## code:
```
def validate_login(user, pwd):
    if not user or not pwd:
        print("Username or password cannot be blank")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("Invalid Username")

user = "admin"
pwd = "pass123"

validate_login(user, pwd)
```
## output:
<img width="521" height="135" alt="image" src="https://github.com/user-attachments/assets/3eae46e6-1e77-4d2c-af4f-13aa79c4af72" />


## EX 16 : For Loop
## Code:
```
def forloop():
    num=int(input("Enter a number: "))
    for i in range(1,num+1):
        print(i,end=" ")

forloop()
```
## Output:
<img width="1458" height="91" alt="image" src="https://github.com/user-attachments/assets/871b44d0-952a-4a22-8cee-4fd6a94f9ab4" />


## EX 17 : While Loop
## Code:
```
def iter():
    num=int(input("Enter a number: "))
    while (num>0):
        print(num)
        num-=1
iter()
```
## Output:
<img width="1447" height="178" alt="image" src="https://github.com/user-attachments/assets/713bc141-6316-4098-b494-eeddcf617b55" />


## EX 18 : Break
## Code:
```
def first_even(start, end):
    if start > end:
        print("Invalid range: start should be less than or equal to end")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First even number is:", i)
            break
    else:
        print("No even number found in the given range")

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

first_even(start, end)

```
## Output:
<img width="1447" height="114" alt="image" src="https://github.com/user-attachments/assets/0101d995-e419-42b0-b66b-d90f29059ec1" />

## EX 19 : Continue

## Code:
```
def first_even(start, end):
    if start > end:
        print("Invalid range: start should be less than or equal to end")
        return
    sum=0
    for i in range(start, end + 1):
        if i % 2 == 0:
            continue
        sum+=i
    print("The sum of odd numbers in the given range is: ",sum)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

first_even(start, end)
```
## Output:
<img width="1440" height="118" alt="image" src="https://github.com/user-attachments/assets/1fc3073b-55a1-45cd-9613-0e83fbb12e52" />

## EX 20 : Pass

## Code:
```
def empty_function():
    pass

empty_function()
print("Function defined")
```
## Output:
<img width="1450" height="93" alt="image" src="https://github.com/user-attachments/assets/b10b472b-0db3-4461-b5c9-558a5d980e7c" />

## EX 21 : Consistent Indentation

## Code:
```
def check_nested():
    if True:
        if True:
            print("Nested")

check_nested()
print("Confirmation message")
```
## Output:
<img width="1456" height="98" alt="image" src="https://github.com/user-attachments/assets/9ab57df8-f8f9-4c07-9cff-54ec2a95baf3" />

## EX 22 : Comment Usage

## Code:
```
def calculate_salary():
    base_salary = int(input("Enter base salary: "))
    bonus = int(input("Enter bonus: "))
    total_salary = base_salary + bonus
    print("Total Salary:", total_salary)

calculate_salary()
```
## Output:
<img width="1461" height="149" alt="image" src="https://github.com/user-attachments/assets/17ce1751-03c5-4d1a-ba87-ee1a7180c5c4" />

## EX 23 : Import Standard Module

## Code:
```
import math

def calc():
    radius=float(input("Enter the radius: "))
    area=math.pi*(radius**2)
    print(f"{area:.2f}")

calc()
```
## Output:
<img width="1460" height="87" alt="image" src="https://github.com/user-attachments/assets/832becbd-123d-4e71-a22e-7738fb3763c5" />


## EX 24 : All Import

## Code:
```
from math import *

def square():
    num=int(input("Enter the number"))
    print(sqrt(num))

square()
```
## Output:
<img width="1449" height="146" alt="image" src="https://github.com/user-attachments/assets/3fa89bee-883c-410c-bd23-d2b73372d2b4" />


## EX 25 : Parameters

## Code:
```
def add(a,b):
    res=a+b
    return res

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
res=add(a,b)
print("The sum of two numbers is :",res)
```
## Output:
<img width="1466" height="137" alt="image" src="https://github.com/user-attachments/assets/27c0838d-8342-4734-a4fa-8b45bb7e49e8" />


## EX 26 : Multiple Parameters

## Code:
```
def area(length,breadth):
    res=length*breadth
    return res

length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
res=area(length,breadth)
print("The sum of two numbers is :",res)
```
## Output:
<img width="1453" height="124" alt="image" src="https://github.com/user-attachments/assets/a272e002-2acd-4951-bdb6-432015a4ffba" />

## EX 27 : Len Function

## Code:
```
def length(text):
    print(len(text))

text=input("Enter the text")
length(text)
```
## Output:
<img width="1456" height="145" alt="image" src="https://github.com/user-attachments/assets/a208f0bf-813a-42eb-af69-616273f54c85" />

## EX 28 : Write to File

## Code:
```
def write_to_file():
    file = open("message.txt", "w")
    file.write("Hello World")
    file.close()
    print("File written successfully")

write_to_file()
```
## Output:
<img width="1452" height="120" alt="image" src="https://github.com/user-attachments/assets/ae10a0aa-6d76-498b-9b48-1ab8dc14eb28" />

## EX 29 : Read from File

## Code:
```
def read_file():
    file = open("message.txt", "r")
    content = file.read()
    file.close()
    print("File Content:")
    print(content)

read_file()
```
## Output:
<img width="1455" height="167" alt="image" src="https://github.com/user-attachments/assets/3ce41407-6ee1-412c-82fb-c8f008dc3689" />

## EX 30 : Basic Try Except

## Code:
```
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

x = float(input("Enter numerator: "))
y = float(input("Enter denominator: "))
safe_divide(x, y)

```
## Output:
<img width="1460" height="160" alt="image" src="https://github.com/user-attachments/assets/e005a51c-58e5-45e6-99dd-a89a2f456bdb" />

## EX 31 : Create List

## Code:
```
def show_cart():
    cart = []
    n = int(input("Enter number of items: "))
    for i in range(n):
        item = int(input(f"Enter item {i+1}: "))
        cart.append(item)
    if len(cart) == 0:
        print("Cart is empty")
        return
    print("Shopping Cart Items:")
    for item in cart:
        print(item)

show_cart()

```
## Output:
<img width="1451" height="208" alt="image" src="https://github.com/user-attachments/assets/1759b5ab-d71c-4483-a061-9319cdb78259" />


## EX 32 : Append to List

## Code:
```
def add_expense():
    expenses = [100, 200, 150]
    print("Expenses before adding:", expenses)
    new_expense = int(input("Enter new expense amount: "))
    if new_expense <= 0:
        print("Invalid expense amount")
        return
    expenses.append(new_expense)
    print("Updated Expenses List:")
    for expense in expenses:
        print(expense)
add_expense()

```
## Output:
<img width="1459" height="259" alt="image" src="https://github.com/user-attachments/assets/f7d76e33-fda5-4fc6-874b-f6b57508c005" />


## EX 33 : Update Dictionary

## Code:
```
def update_employee():
    emp1 = {"id": 101, "name": "John", "salary": 30000}
    emp2 = {"dept": "IT", "location": "Chennai"}

    if not isinstance(emp1, dict) or not isinstance(emp2, dict):
        print("Invalid input")
        return

    emp1.update(emp2)

    print("Updated Employee Data:")
    for key, value in emp1.items():
        print(key, ":", value)

update_employee()

```
## Output:
<img width="1444" height="220" alt="image" src="https://github.com/user-attachments/assets/f4b4c4d5-a4e6-49f8-bd8b-9c118ac56e92" />


## EX 34 : Nested Dictionary

## Code:
```
def get_salary(dept, emp_name):
    employees = {
        "AI": {
            "Santhiya": 60000,
            "Arun": 55000
        },
        "IT": {
            "Kiran": 70000,
            "Meena": 65000
        }
    }
    if dept not in employees:
        return "Department not found"
    if emp_name not in employees[dept]:
        return "Employee not found"
    return employees[dept][emp_name]
print(get_salary("AI", "Santhiya"))
```
## Output:
<img width="1449" height="130" alt="image" src="https://github.com/user-attachments/assets/9ee1facf-98c8-4db3-9af1-b89e1243c8d0" />


## EX 35 : Create Tuple

## Code:
```
def get_coordinates():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    coordinates = (x, y)
    if len(coordinates) != 2:
        return "Invalid coordinates"
    print("Coordinates:", coordinates)

get_coordinates()

```
## Output:
<img width="1458" height="191" alt="image" src="https://github.com/user-attachments/assets/98e6e874-a9b3-4dfb-ab99-fa1c0d8b8a67" />


## EX 36 : Set Intersection

## Code:
```
def common_elements():
    set1 = set()
    set2 = set()
    n1 = int(input("Enter number of elements in set1: "))
    for i in range(n1):
        set1.add(int(input("Enter element for set1: ")))
    n2 = int(input("Enter number of elements in set2: "))
    for i in range(n2):
        set2.add(int(input("Enter element for set2: ")))
    common = set1 & set2
    print("Set1:", set1)
    print("Set2:", set2)
    print("Common elements:", common)

common_elements()
```
## Output:
<img width="1458" height="344" alt="image" src="https://github.com/user-attachments/assets/2cd28707-3662-42a2-98a8-6a8902dd240d" />


## EX 37 : Multiple Instances

## Code:
```
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}"


def main():
    emp1 = Employee("Santhiya", 101)
    emp2 = Employee("Arun", 102)
    emp3 = Employee("Meena", 103)

    employees = [emp1, emp2, emp3]

    for emp in employees:
        print(emp.display())


main()

```
## Output:
<img width="1458" height="169" alt="image" src="https://github.com/user-attachments/assets/755e25ec-9273-47a5-898e-bf190029bce7" />


## EX 38 : Method Chaining

## Code:
```
class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            self.salary = 0
        else:
            self.salary = salary
        return self

    def apply_raise(self, percent):
        if percent < 0:
            percent = 0
        self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print("Employee:", self.name)
        print("Final Salary:", self.salary)
        return self


def main():
    emp = Employee("Santhiya")
    emp.set_salary(50000).apply_raise(10).display()


main()

```
## Output:
<img width="1448" height="143" alt="image" src="https://github.com/user-attachments/assets/6519ac85-078c-470f-aa13-09849cdb525f" />


## EX 39 : Polymorphism

## Code:
```
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Tester(Employee):
    def work(self):
        print("Tester tests the application")


def main():
    employees = [Developer(), Tester(), Employee()]

    for emp in employees:
        emp.work()


main()

```
## Output:
<img width="1452" height="210" alt="image" src="https://github.com/user-attachments/assets/2f672f3c-1bdc-4313-9f42-d870343ab491" />


## EX 40 :Class Methods

## Code:
```
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")

        if not salary.isdigit():
            return "Invalid salary"

        return cls(name, int(salary))


def main():
    emp = Employee.from_string("Santhiya,75000")
    print(emp.display())


main()
```
## Output:
<img width="1465" height="205" alt="image" src="https://github.com/user-attachments/assets/65cfba7b-c5cb-43ae-a9be-21d3beb4faa3" />


## EX 41 : Employee Management System

## Code:
```
import json
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary
        }
def save_employees(emp_list):
    data = {}

    for emp in emp_list:
        data[emp.emp_id] = emp.to_dict()

    with open("emps.json", "w") as file:
        json.dump(data, file)

    return "Data saved successfully"


def load_employees():
    try:
        with open("emps.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "No file found"


def main():
    e1 = Employee(101, "Santhiya", 60000)
    e2 = Employee(102, "Hycinth", 55000)

    employees = [e1, e2]

    print(save_employees(employees))
    print(load_employees())


main()

```
## Output:
<img width="1448" height="154" alt="image" src="https://github.com/user-attachments/assets/20e14705-ef78-482c-a63b-29a252b0f28f" />


## EX 42 : Data Analysis Pipeline

## Code:
```
import statistics

def process_sales():
    try:
        file = open("sales.txt", "r")
        data = file.read().split()
        file.close()

        sales = []

        for value in data:
            try:
                sales.append(float(value))
            except ValueError:
                print("Skipping invalid data:", value)

        if len(sales) == 0:
            print("No valid sales data found")
            return

        mean_value = statistics.mean(sales)
        median_value = statistics.median(sales)

        print("Sales Data:", sales)
        print("Mean:", mean_value)
        print("Median:", median_value)

    except FileNotFoundError:
        print("File not found: sales.txt")
    except Exception as e:
        print("Error occurred:", e)

process_sales()

```
## Output:
<img width="1443" height="165" alt="image" src="https://github.com/user-attachments/assets/e3174060-4376-4cc2-8433-99d6b80233a2" />


## EX 43 : Configuration Manager

## Code:
```
import configparser

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()

    def load_config(self):
        self.config.read(self.file_path)
        return self.config


class DatabaseConfig(Config):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.settings = {}

    def validate_keys(self):
        required_keys = ["host", "port", "username", "password", "dbname"]

        if "database" not in self.config:
            print("Missing [database] section")
            return False

        for key in required_keys:
            if key not in self.config["database"]:
                print("Missing key:", key)
                return False

        return True

    def get_settings(self):
        if not self.validate_keys():
            return None

        self.settings = dict(self.config["database"])
        return self.settings


config = DatabaseConfig("db.ini")
config.load_config()

settings = config.get_settings()

print("Database Settings:")
print(settings)

```
## Output:
<img width="1451" height="147" alt="image" src="https://github.com/user-attachments/assets/284a23cd-50c9-400d-bc52-090b5094105c" />


## EX 44 : CSV Data Processor

## Code:
```
import csv

def process_csv():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)
            employees = list(reader)

        for emp in employees:
            emp["salary"] = int(emp["salary"])

        high_salary_employees = [
            emp for emp in employees if emp["salary"] > 50000
        ]

        salaries = [emp["salary"] for emp in employees]
        avg_salary = sum(salaries) / len(salaries)

        print("All Employees:")
        for emp in employees:
            print(emp)

        print("\nEmployees with salary > 50000:")
        for emp in high_salary_employees:
            print(emp)

        print("\nAverage Salary:", avg_salary)

    except FileNotFoundError:
        print("employees.csv file not found")
    except Exception as e:
        print("Error:", e)

process_csv()
```
## Output:
<img width="1459" height="264" alt="image" src="https://github.com/user-attachments/assets/45399ae4-f4c2-423a-a93d-106ac81b6463" />


## EX 45 : Expense Tracker

## Code:
```
import csv
from datetime import datetime

def expense_tracker():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

        current_month = datetime.now().month
        current_year = datetime.now().year

        for exp in expenses:
            exp["amount"] = float(exp["amount"])

        filtered_expenses = [
            exp for exp in expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d").month == current_month
            and datetime.strptime(exp["date"], "%Y-%m-%d").year == current_year
        ]

        category_totals = {}

        for exp in filtered_expenses:
            cat = exp["category"]
            category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

        print("Filtered Expenses (Current Month):")
        for exp in filtered_expenses:
            print(exp)

        print("\nCategory-wise Total:")
        for cat, total in category_totals.items():
            print(cat, ":", total)

    except FileNotFoundError:
        print("expenses.csv file not found")
    except Exception as e:
        print("Error:", e)

expense_tracker()
```
## Output:
<img width="1442" height="291" alt="image" src="https://github.com/user-attachments/assets/e2da9ae7-a13a-4ebc-ad11-b06280c4413c" />


## EX 46 : API Response Handler

## Code:
```
import requests

def get_weather(city):
    try:
        if city.strip() == "":
            return "Invalid city name"

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        if response.status_code != 200:
            return "Error fetching data"

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]

        return f"Temperature: {temp}°C, Condition: {weather}"

    except requests.exceptions.RequestException:
        return "Network error"


print(get_weather("Chennai"))

```
## Output:
<img width="1616" height="110" alt="image" src="https://github.com/user-attachments/assets/6f670994-952c-4aa8-a202-b68c53e6cd56" />


## EX 47 : Compute Calculator Program

## Code:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        result = calculate(a, b, op)

        print("Result:", result)

    except ValueError:
        print("Invalid number input")


main()

```
## Output:
<img width="1643" height="147" alt="image" src="https://github.com/user-attachments/assets/012ced8b-1f63-4b11-8339-545b48e43bfe" />


## EX 48 : Shopping Cart System

## Code:
```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        total = sum(item.total_price() for item in self.items)
        gst = total * 0.18
        final_total = total + gst
        return total, gst, final_total

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, "-", item.quantity, "x", item.price, "=", item.total_price())

        total, gst, final_total = self.calculate_total()

        print("\nTotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final_total)


def main():
    cart = ShoppingCart()

    cart.add_item(CartItem("Rice", 50, 2))
    cart.add_item(CartItem("Milk", 30, 3))
    cart.add_item(CartItem("Soap", 40, 1))

    cart.remove_item("Soap")

    cart.print_receipt()


main()

```
## Output:
<img width="1460" height="314" alt="image" src="https://github.com/user-attachments/assets/ffc6052c-49ad-4d56-aeb2-3e20889b0e0f" />


## EX 49 : Temperature Converter GUI

## Code:
```
class TemperatureConverter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


def main():
    converter = TemperatureConverter()

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1-4): ")

    try:
        temp = float(input("Enter temperature: "))

        if choice == "1":
            print("Result:", round(converter.c_to_f(temp), 2))

        elif choice == "2":
            print("Result:", round(converter.f_to_c(temp), 2))

        elif choice == "3":
            print("Result:", round(converter.c_to_k(temp), 2))

        elif choice == "4":
            print("Result:", round(converter.k_to_c(temp), 2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid temperature input")


main()

```
## Output:
<img width="1454" height="267" alt="image" src="https://github.com/user-attachments/assets/54d45727-7150-42b2-9bb1-3b88e553d7a5" />


## EX 50 : Backup Utility

## Code:
```
import shutil
import os

def backup_files(source_files, backup_folder):
    copied_files = set()

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    log_file = open("backup.log", "a")

    for file in source_files:
        try:
            if file in copied_files:
                log_file.write(f"SKIPPED (duplicate): {file}\n")
                continue

            if not os.path.exists(file):
                log_file.write(f"NOT FOUND: {file}\n")
                continue

            destination = os.path.join(backup_folder, os.path.basename(file))
            shutil.copy(file, destination)

            copied_files.add(file)
            log_file.write(f"COPIED: {file} -> {destination}\n")

        except PermissionError:
            log_file.write(f"PERMISSION ERROR: {file}\n")
        except Exception as e:
            log_file.write(f"ERROR: {file} -> {e}\n")

    log_file.close()
    print("Backup completed. Check backup.log")

files = input("Enter file names separated by space: ").split()
backup_folder = "backup"

backup_files(files, backup_folder)

```
## Output:
<img width="1459" height="141" alt="image" src="https://github.com/user-attachments/assets/62919d79-4fac-4640-9c6d-0c87af3bbacf" />


## EX 51 : URL Shortener

## Code:
```
import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def _generate_short_code(self, url):
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:6]

    def shorten_url(self, url):
        if not url:
            return "Invalid URL"

        short_code = self._generate_short_code(url)
        self.url_map[short_code] = url

        return short_code

    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")


def main():
    shortener = URLShortener()

    url = "https://www.google.com"
    short_code = shortener.shorten_url(url)

    print("Short URL code:", short_code)
    print("Original URL:", shortener.get_original_url(short_code))


main()

```
## Output:
<img width="1464" height="153" alt="image" src="https://github.com/user-attachments/assets/e9a33c1c-4b9a-4e65-beac-595d015e0703" />


## EX 52 : Gradebook System 

## Code:
```
import json
def calculate_gpa(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def add_student_grade(data, name, grade):
    if name not in data:
        data[name] = []

    if 0 <= grade <= 100:
        data[name].append(grade)
    else:
        print("Invalid grade ignored")


def class_average(data):
    all_grades = []

    for grades in data.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


def save_data(data, filename="grades.json"):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename="grades.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def main():
    students = load_data()

    add_student_grade(students, "Santhiya", 85)
    add_student_grade(students, "Hycinth", 90)
    add_student_grade(students, "Roshini", 78)

    print("GPA Santhiya:", calculate_gpa(students["Santhiya"]))
    print("Class Average:", class_average(students))

    save_data(students)


main()

```
## Output:
<img width="1448" height="116" alt="image" src="https://github.com/user-attachments/assets/1fc16f44-624f-4b2e-93a5-32b4ad543279" />


## EX 53 : Task Scheduler

## Code:
```
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def is_overdue(self):
        return self.due_date < datetime.now()


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda t: t.due_date)

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def display_tasks(self):
        print("\n--- Task List ---")
        for task in self.get_sorted_tasks():
            status = "Overdue" if task.is_overdue() else "Pending"
            print(task.name, "-", task.due_date.date(), "-", task.priority, "-", status)


def main():
    scheduler = TaskScheduler()

    scheduler.add_task(Task("Finish Project", "2026-05-20", "High"))
    scheduler.add_task(Task("Study SQL", "2026-06-05", "Medium"))
    scheduler.add_task(Task("Practice Python", "2026-05-10", "High"))

    scheduler.display_tasks()

    print("\nOverdue Tasks:")
    for task in scheduler.get_overdue_tasks():
        print(task.name)


main()

```
## Output:
<img width="1452" height="240" alt="image" src="https://github.com/user-attachments/assets/1f99a778-a708-4930-82ec-773087c1aa51" />




## EX 54 : Inventory Manager

## Code:
```
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"


class Perishable(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years


class InventoryManager:
    def __init__(self):
        self.products = {}
        self.low_stock_alert = set()

    def add_product(self, product):
        self.products[product.name] = product

        if product.stock < 5:
            self.low_stock_alert.add(product.name)

    def update_stock(self, name, new_stock):
        if name in self.products:
            self.products[name].stock = new_stock

            if new_stock < 5:
                self.low_stock_alert.add(name)
            elif name in self.low_stock_alert:
                self.low_stock_alert.remove(name)

    def show_inventory(self):
        print("\n--- Inventory ---")
        for product in self.products.values():
            print(product.display())

    def show_low_stock(self):
        print("\n--- Low Stock Items ---")
        for item in self.low_stock_alert:
            print(item)


def main():
    manager = InventoryManager()

    p1 = Perishable("Milk", 50, 3, "2026-06-10")
    p2 = Electronics("Phone", 15000, 10, 2)
    p3 = Product("Book", 200, 2)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    manager.show_inventory()
    manager.show_low_stock()

    manager.update_stock("Phone", 3)

    print("\nAfter Update:")
    manager.show_inventory()
    manager.show_low_stock()


main()

```
## Output:
<img width="1472" height="510" alt="image" src="https://github.com/user-attachments/assets/fb48a2c4-b760-4c3a-93a4-d5aeca610734" />


## EX 55 : Budget Planner

## Code:
```
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.spent += amount

    def status(self):
        if self.spent > self.limit:
            return f"{self.name}: Budget exceeded!"
        return f"{self.name}: Within budget"


class BudgetPlanner:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def show_status(self):
        print("\n--- Budget Status ---")
        for c in self.categories:
            print(c.status())

    def show_chart(self):
        names = [c.name for c in self.categories]
        spent = [c.spent for c in self.categories]

        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()


def main():
    planner = BudgetPlanner()

    food = Category("Food", 5000)
    travel = Category("Travel", 3000)
    shopping = Category("Shopping", 4000)

    food.add_expense(4500)
    travel.add_expense(3500)
    shopping.add_expense(2000)

    planner.add_category(food)
    planner.add_category(travel)
    planner.add_category(shopping)

    planner.show_status()
    planner.show_chart()


main()

```
## Output:
<img width="1452" height="499" alt="image" src="https://github.com/user-attachments/assets/00b1cb11-cc10-475c-902e-ba2d2c7e7762" />
