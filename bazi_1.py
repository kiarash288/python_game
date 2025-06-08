import random 
while True:
    your_input=input(' \n 1:stone\n 2:paper \n 3:scissor\n')
    if your_input.isdigit():
        your_choice=int(your_input)
        if 1<=your_choice<=3:
            break
        else:
            print('you mustenter 1 or 2 or 3')
    else:
        print('you should enter a valid number')
computer_choice=random.choice(['1','2','3'])
computer_value=int(computer_choice)
print('your choice is'+ " " + your_input + " " +'computer choice is' + " " +computer_choice)
if computer_value==your_choice:
    print('its tie!')
if (computer_value==3 and your_choice==1)or\
   (computer_value==1 and your_choice==3)or\
   (computer_value==2 and your_choice==1):
   print('you lose!')
else:
    print('you win!')


    