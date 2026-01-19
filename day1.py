
# Day 1 - Real Life Scenarios Using Python
# Author: Muhammad Rizwan
# Goal: Practice Python using real-world logic

print("===== PYTHON REAL LIFE SCENARIOS =====\n")

# -------------------------------
# Scenario 1: Age Verification
# -------------------------------
print("Scenario 1: Age Verification")

age = int(input("Enter your age: "))

if age >= 18:
    print("Result: You are eligible to register.\n")
else:
    print("Result: You must be at least 18 years old.\n")


# -------------------------------
# Scenario 2: Bank Deposit System
# -------------------------------
print("Scenario 2: Bank Deposit Calculator")

current_balance = float(input("Enter your current balance: "))
deposit_amount = float(input("Enter deposit amount: "))

new_balance = current_balance + deposit_amount
print("Result: Your new balance is:", new_balance, "\n")


# -------------------------------
# Scenario 3: Grade Calculator
# -------------------------------
print("Scenario 3: Grade Calculator")

marks = float(input("Enter your marks (0 - 100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Result: Your grade is", grade, "\n")


# -------------------------------
# Scenario 4: Odd or Even Checker
# -------------------------------
print("Scenario 4: Odd or Even Checker")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Result:", number, "is an EVEN number\n")
else:
    print("Result:", number, "is an ODD number\n")


# -------------------------------
# Scenario 5: Shopping Discount
# -------------------------------
print("Scenario 5: Shopping Discount")

total_purchase = float(input("Enter total purchase amount: "))

if total_purchase > 100:
    discount = total_purchase * 0.10
    final_amount = total_purchase - discount
    print("Result: 10% discount applied.")
    print("Total to pay:", final_amount)
else:
    print("Result: No discount applied.")
    print("Total to pay:", total_purchase)

print("\n===== END OF PROGRAM =====")
