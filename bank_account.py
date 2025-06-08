class BalanceException(Exception):
    pass
class BankAccount():
    def __init__(self,initialAmount,accountName):
        self.balance=initialAmount
        self.name=accountName
        print(f'\n Account  {self.name}  created .\n Balance:{self.balance:.2f}')
    def getBalance(self):
        print(f'Account {self.name} balance = {self.balance:.2f}')
    def deposit(self,amount):
        self.balance+=amount
        print('\n deposit complete ')
        self.getBalance()
    def checkTransaction(self,amount):
        if self.balance>=amount:
            return 
        else:
            raise BalanceException(f'sorry {self.name} only has balance of {self.balance}$')

    def withdraw(self,amount):
        try:
            self.checkTransaction(amount)
            self.balance-=amount
            print('\n withdraw is completed')
            self.getBalance()
        except BalanceException as error:
            print(f'\n withdraw is interrupted:{error}')
    def transfer(self,amount,accName):
        try:
            print('\n******** Transfer started')
            self.checkTransaction(amount)
            self.withdraw(amount)
            accName.deposit(amount)
            print('\n**********\n  Transfer completed')
        except BalanceException as error:
            print(f'\n Transfer is interrupted:{error}')
class IntrestRewaradAccount(BankAccount):
    def deposit(self,amount):
        self.balance+=amount*1.05
        print('\n deposit completed')
        self.getBalance()
class TaxTransform(IntrestRewaradAccount):
    def __init__(self,initialAmount,accountName):
        super().__init__(initialAmount,accountName)
        self.fee=5
    def transfer(self,accountName,amount):
        try:
            print('\n******\n Transfer stated')
            self.checkTransaction(amount+self.fee)
            self.balance=self.balance-(self.fee+amount)
            self.withdraw(amount+self.fee)
            accountName.deposit(amount)
        except BalanceException as error:
            print(f'\n Transfer intterupted {error}')