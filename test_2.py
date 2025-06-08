def bmi(weight,height):
    return weight/(height**2)
user_weight=float(input('pleas enter your weight in kg '))
user_height=float(input('pleas enter your height in m '))
result=bmi(user_weight,user_height)
print(f'your BMI is {result}')
if result<18.5:
    print('you are under weight')
elif 18.5<result<24.9:
    print('your weight is proper')
elif 25<result<30:
    print('you are in over weight range')
else:
    print('you have obesity')