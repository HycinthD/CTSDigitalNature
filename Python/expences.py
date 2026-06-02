with open("expenses.csv", "w") as file:
    file.write("date,amount,category\n")
    file.write("2026-06-05,500,Food\n")
    file.write("2026-06-10,1200,Travel\n")
    file.write("2026-06-12,300,Food\n")
    file.write("2026-05-20,800,Shopping\n")
    file.write("2026-06-15,700,Travel\n")

print("expenses.csv created successfully")