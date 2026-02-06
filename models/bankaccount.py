class BankAccount:
        def __init__(self,ac,balance=0):
            self.ac=ac #public
            self.balance = balance #private

        def __add__(self, other):
            new_balance = self.balance + other.balance
            new_account = BankAccount(ac="CombinedAccount", balance=new_balance)
            return new_account

        def __str__(self):
            return f"Account: {self.ac}, Balance: {self.balance:.2f}a"