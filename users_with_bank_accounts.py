# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)  # added this line

#     def example_method(self):
#         # we can call the BankAccount instance's methods
#         self.account.deposit(100)
#         print(self.account.balance)		# or access its attributes


class User:
    def __init__(self, username):
        self.username = username
        self.account = BankAccount(int_rate=0.01, balance=0)

    def displayUserBalance(self):
        print("*" * 80)
        print(f"Getting {self.username}'s balance")
        print(f"User: {self.username}, Balance: ${self.account.balance}")
        print("*" * 80)

    def deposit(self, amount):
        print("[ + ] - ", end='')
        self.account.deposit(amount)
        print(f"Deposited ${amount} into {self.username}'s account")
        return self

    def withdraw(self, amount):
        print("[ - ] - ", end='')
        self.account.withdraw(amount)
        print(f"Withdrew ${amount} from {self.username}'s account")
        return self

    def transferMoney(self, otherUser, amount):
        print("*" * 80)
        print(
            f"Transferring {amount} from {self.username} to {otherUser.username}.")
        self.withdraw(amount)
        otherUser.deposit(amount)
        print("Transfer Complete")


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("[ERR] Not enough balance to yield Interest.")
        return self


user1 = User("Aaron")
user2 = User("Taylor")


user1.displayUserBalance()
user1.deposit(1000).withdraw(500).deposit(1500).displayUserBalance()
