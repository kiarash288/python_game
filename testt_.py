def number(weight,height):
    bmi=weight/(height**2)
    return bmi
weight_input=float(input('pleas enter your weight in kg '))
height_input=float(input('pleas enter yout height in m '))
result=number(weight_input,height_input)
print(f'your bmi is {result}')
if 18.5<result<24.9:
    print('your weight is proper')
elif 25<result<29.9:
    print('you are in the over weight range')
elif result>30:
    print('you have obesity')