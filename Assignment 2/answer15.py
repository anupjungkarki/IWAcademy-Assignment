# Imagine you are designing a banking application. What would a customer look like? What attributes would she have?
# What methods would she have?
class BankingCustomer:
    # A customer in a bank
    def __init__(self, account_number, account_holder, opening_balance, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = opening_balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount  # to put money in the bank account

    def withdraw(self, amount):
        self.balance -= amount  # To withdraw money

    def get_balance(self):
        return self.balance  # Current Amount in Bank

    def __str__(self):
        return 'Account Number:' + self.account_number + ' Name:' + self.account_holder + ' Account Type:' + self.account_type + ' Balance:' + str(
            self.balance)


acc1 = BankingCustomer('12345', 'Anup Karki', 20000.00, 'current')
print(acc1)
