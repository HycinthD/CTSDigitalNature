with open("employees.csv", "w") as file:
    file.write("name,salary\n")
    file.write("John,45000\n")
    file.write("Alice,60000\n")
    file.write("Bob,75000\n")
    file.write("David,50000\n")

print("employees.csv created successfully")