import random

while True:
    your_input = input("\nPlease enter a number\n1: stone\n2: paper\n3: scissor\n")
    
    if your_input.isdigit():
        your_choice = int(your_input)
        if 1 <= your_choice <= 3:
            break  # ورودی درست است، خارج می‌شویم از حلقه
        else:
            print("You must enter 1, 2, or 3")
    else:
        print("You must enter a valid number")

# ادامه بازی
computer_value = random.choice(["1", "2", "3"])
computer_choice = int(computer_value)

print(f"Your choice is {your_choice}, computer choice is {computer_choice}")

# 1: stone, 2: paper, 3: scissor
if your_choice == computer_choice:
    print("It's a tie!")
elif (your_choice == 1 and computer_choice == 3) or \
     (your_choice == 2 and computer_choice == 1) or \
     (your_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("You lose!")
