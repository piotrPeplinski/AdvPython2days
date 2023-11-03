class BankAccount:
    total_accounts = 0

    def __init__(self,account_holder:str, initial_balance:int|float=0):
        """Bank account repr

        Args:
            account_holder (str): Owner of the account
            initial_balance (int | float, optional): Initial deposit. Defaults to 0.
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_accounts += 1
        

    def deposit(self, amount:int|float)->bool:
        """
        Method allows to deposit funds to an account
        """
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount):
        if amount > 0 and amount <=self.balance:
            self.balance-=amount
            return True
        else:
            return False
        
    @classmethod
    def account_summary(cls):
        return cls.total_accounts
        
    @staticmethod    
    def currency_converter(amount, exchange_rate):
        return amount * exchange_rate
    
    def __str__(self):
        return f'Account | Balance: {self.balance}'

