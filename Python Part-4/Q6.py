from abc import ABC, abstractmethod

class Employee:

    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print(f"Intern Salary is {80_000}")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print(f"Full Time Employee Salary is {8_00_000}")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print(f"Contract Employee Salary is {4_00_000}")


intern = Intern()
fulltimeemployee = FullTimeEmployee()
contractemployee = ContractEmployee()

intern.calculate_salary()
fulltimeemployee.calculate_salary()
contractemployee.calculate_salary()