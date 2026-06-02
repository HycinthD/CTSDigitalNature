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


## EX:16
## code:
```
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = int(input("Enter a number: "))
result = sum_of_numbers(num)

print("Sum of first", num, "numbers is:", result)
```
## output:
<img width="1251" height="133" alt="image" src="https://github.com/user-attachments/assets/1aaf1930-d304-4413-bbea-167898289f6b" />

## EX:17
## code:
```
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial of", num, "is:", result)
```
## output:
<img width="1260" height="136" alt="image" src="https://github.com/user-attachments/assets/626d95bb-8b86-498f-ba10-c71a0b920e8b" />

## EX:18
## code:
```
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number is:", reverse)
```
## output:
<img width="1245" height="125" alt="image" src="https://github.com/user-attachments/assets/b4e8161c-6237-4a88-9d39-a78da358d1e7" />
