# Day 2 - Operators and Logic
# Author: Muhammad Rizwan

print("===== PYTHON OPERATORS & LOGIC =====\n")

a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print("\n--- Comparison Operators ---")
print(a > b)
print(a == b)
print(a != b)

print("\n--- Logical Operators ---")
age = 25
is_employee = True

if age > 18 and is_employee:
    print("Eligible person")

print("\n--- Electricity Bill Calculator ---")
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
else:
    bill = units * 10

print("Total bill: Rs.", bill)
