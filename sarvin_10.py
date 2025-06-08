def budget_manager():
    budget=int(input('pleas enter your budget '))
    def manager():
        nonlocal budget
        action=input('pleas enter add or get or spend ').lower()
        if action=='add':
             amount=int(input('pleas enter your amount '))
             budget+=amount
             print(f'your current budget is {amount} and your income is {budget}')
        elif action=='spend':
            amount=int(input('pleas enter tour amount '))
            if budget>amount:
                budget-=amount
                
                print(f'your spendation is {amount} and your current budget is {budget}')
            else:
                print(f'your {budget} is not enough your spendation is {amount} whic is more than your {budget}')
        elif action=='get':
            print(f'your current budget is{budget}')
        else:
            print('unvalid operation!')
    manager()
budget_manager()