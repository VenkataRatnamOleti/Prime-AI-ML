salary = int(input("Enter Salary: "))

tax = 0

if salary < 30000:
    tax = 5
elif 30000 <= salary <= 70000:
    tax = 15
elif salary > 70000:
    tax = 25

print(f"Final Tax is {(salary/100)*tax}")