# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, otherUser, amount) - have this method decrease the user's balance by the amount and add that amount to other otherUser's balance


class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def displayUserBalance(self):
        print("-" * 80)
        print(f"Getting {self.username}'s balance")
        print(f"User: {self.username}, Balance: ${self.balance}")
        return self

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.username}")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount} from {self.username}")
        return self

    def transferMoney(self, otherUser, amount):
        print("-" * 80)
        print(
            f"Transferring {amount} from {self.username} to {otherUser.username}.")
        self.withdraw(amount)
        otherUser.deposit(amount)
        print("Transfer Complete")


user1 = User("Aaron", 50000)
# user2 = User("Taylor", 1000)

# user1.displayUserBalance()
# user2.displayUserBalance()

# user1.transferMoney(user2, 1000)

# user1.displayUserBalance()
# user2.displayUserBalance()

# user1.deposit(500)
# user1.displayUserBalance()

user1.displayUserBalance()

user1.deposit(500).deposit(500).withdraw(10000)

user1.displayUserBalance()
