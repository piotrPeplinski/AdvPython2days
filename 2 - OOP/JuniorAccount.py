from BankAccount import BankAccount
#interest_rate
#add_interest
class JuniorAccount(BankAccount):
    def __init__(self, account_holder, interest_rate, initial_balance=0):
        super().__init__(account_holder,initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance*(1+(self.interest_rate/100))
        return True

account1 = JuniorAccount('Piotr',5, 200)
account1.deposit(300)
account1.add_interest()
print(vars(account1))