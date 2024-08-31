class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

# Taking input for the account owner
owner_name = input("Enter the owner's name: ")

# Creating an instance of BankAccount
account = BankAccount(owner_name)

# Performing a series of transactions with user input
while True:
    action = input("Would you like to deposit, withdraw, or check balance? (Enter 'exit' to quit): ").lower()
    
    if action == "deposit":
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif action == "check balance":
        print(f"Current Balance: {account.get_balance()}")
    elif action == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")

# Printing the final balance
print(f"Final Balance: {account.get_balance()}")




#   Output
#   Enter the owner's name: Shirsho
#   Would you like to deposit, withdraw, or check balance? (Enter 'exit' to quit): deposit
#   Enter the amount to deposit: 5
#   Deposited: 5.0
#   Would you like to deposit, withdraw, or check balance? (Enter 'exit' to quit): withdraw
#   Enter the amount to withdraw: 2
#   Withdrew: 2.0
#   Would you like to deposit, withdraw, or check balance? (Enter 'exit' to quit): check balance
#   Current Balance: 3.0
#   Would you like to deposit, withdraw, or check balance? (Enter 'exit' to quit): exit
#   Exiting the program.
#   Final Balance: 3.0