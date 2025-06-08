grade=[]
for i in range(5):
    grade_input=float(input(f'pleas enter grade number{i+1} '))
    grade.append(grade_input)
def calculate_average(grades):
    return sum(grades)/len(grades)
average=calculate_average(grade)
print(f'your average is {average}')
if average >= 17:
    print("Excellent!")
elif average >= 14:
    print("Good job!")
elif average >= 10:
    print("You passed.")
else:
    print("You failed. Try harder next time.")