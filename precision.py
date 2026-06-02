def calculate_net_salary(salary, tax_rate):
    if salary < 0:
        return "Invalid salary! Salary cannot be negative."
    if not (0 <= tax_rate <= 1):
        return "Invalid tax rate! Tax rate must be between 0 and 1."

    return salary - (salary * tax_rate)

salary = 75000.5
tax_rate = 0.18

result = calculate_net_salary(salary, tax_rate)

if isinstance(result, str):
    print(result)
else:
    print(f"Net Salary after Tax: {result:.2f}")