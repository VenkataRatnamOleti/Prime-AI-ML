class BankAccount:

    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Deposited Successfully!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} Withdrawed Successfully!")

    def check_balance(self):
        print(f"Available Balance : {self.balance}")


venkat = BankAccount("8132", "Venkat", 1100.10)
venkat.deposit(100)
venkat.check_balance()
venkat.withdraw(200)
venkat.check_balance()