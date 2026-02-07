# for number in range(1, 11):
#     print(number)

# for number in range(10, 0, -1):
#     print(number)

# for number in range(0, 50, 2):
#     print(number)

# user_input = int(input("Enter a Number: "))
# for multiple in range(1, user_input):
#     print(user_input, "x", multiple, "=", user_input * multiple)
#     multiple += 1

# for i in range(1, 20):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)

# for i in range(1, 10):
#     if i == 6:
#         break
#     else:
#         print(i)

# number = 1
# while number < 6:
#     print(number)
#     number += 1

# user_input = int(input("Enter a Number: "))
# while user_input > 1:
#     print(user_input)
#     user_input -= 1

# user_input = ""
# while user_input != "exit":
#     user_input = input("Enter something: ")
#     print("You Typed: ", user_input)
# print("Goodbye!")

# total = 0
# user_input = ""

# while user_input != 0:
#     user_input = int(input("Enter a Number (0 to exit): "))
#     if user_input == 0:
#         break
#     total = total + user_input
#     print("The Sum of Your Number with previous entry is:", total)

# print("Exiting...")


num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial = factorial * num
    num -= 1

print("Factorial is:", factorial)

