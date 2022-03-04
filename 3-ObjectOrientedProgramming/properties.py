# Without the @property decorator
# class BankAccount:
#     def __init__(self, account_holder_name):
#         self.account_holder_name = account_holder_name
#         self._balance = 0

#     def get_balance(self):
#         return self._balance

#     def set_balance(self, balance):
#         if not type(balance) in (int, float):
#             print('ok')
#             return 0
#         if balance < 0 or balance > 100000:
#             return 0
#         self._balance = round(balance)

#     balance = property(get_balance, set_balance)

# WITH the @property decorator

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if not type(balance) in (int, float):
            print('ok')
            return 0
        if balance < 0 or balance > 100000:
            return 0
        self._balance = round(balance)


account = BankAccount("Antoine")
account.balance = 56.2
print(account.balance)
# account.set_balance(56.6)
