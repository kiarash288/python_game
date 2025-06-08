def calculate_total_with_tax(prices, tax_rate=0.10):
    total = sum(prices)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax

# گرفتن ورودی قیمت‌ها از کاربر
prices = []
n = int(input("چند قیمت می‌خوای وارد کنی؟ "))
for i in range(n):
    price = float(input(f"قیمت {i+1}: "))
    prices.append(price)

# گرفتن مالیات اختیاری از کاربر
tax_input = input("درصد مالیات رو وارد کن یا Enter بزنی پیش‌فرض 10٪ استفاده میشه: ")
if tax_input:
    tax_rate = float(tax_input) / 100
else:
    tax_rate = 0.10

result = calculate_total_with_tax(prices, tax_rate)
print(f"مجموع قیمت‌ها با مالیات {tax_rate*100}% برابر است با: {result:.2f}")
