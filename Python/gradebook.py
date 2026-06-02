import json

students = {}

def add_grade(student, grade):
    if grade < 0 or grade > 100:
        print("Invalid grade")
        return

    if student not in students:
        students[student] = []

    students[student].append(grade)

def calculate_gpa(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)

def save_data(filename):
    with open(filename, "w") as file:
        json.dump(students, file)

def load_data(filename):
    global students

    try:
        with open(filename, "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        print("File not found")

def class_average():
    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)

# Add grades
add_grade("John", 85)
add_grade("John", 90)
add_grade("Alice", 78)
add_grade("Alice", 88)
add_grade("Bob", 92)

# Save data
save_data("grades.json")

# Load data
load_data("grades.json")

# Print student GPAs
print("Student GPAs")
for student, grades in students.items():
    print(f"{student}: {calculate_gpa(grades):.2f}")

# Print class average
print(f"\nClass Average: {class_average():.2f}")