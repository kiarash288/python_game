from bank_account import *

Kokab=BankAccount(3000,'Kokab')
Sara=BankAccount(42000,'Sara')
Kokab.getBalance()
Sara.getBalance()
Kokab.deposit(29000)
Sara.withdraw(1000000)
Sara.transfer(2000,Kokab)
Mina=IntrestRewaradAccount(1000,'Mina')
Mina.getBalance
Mina.deposit(100)
Ahmad=TaxTransform(1000,'Ahmad')
Ahmad.transfer(Mina,150)
Nasrin=TaxTransform(4000,Mina)