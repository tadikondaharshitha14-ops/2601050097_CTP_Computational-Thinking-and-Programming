from abc import ABC, abstractmethod


# Abstract class
class BankAccount(ABC):

    def __init__(self, name: str, balance: float) -> None:
        self.name: str = name
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


# Inheritance
class SavingsAccount(BankAccount):

    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


# Main program
account: SavingsAccount = SavingsAccount("Harshitha", 10000)

account.deposit(2000)
account.withdraw(3000)

print("Customer:", account.name)
print("Balance:", account.balance)