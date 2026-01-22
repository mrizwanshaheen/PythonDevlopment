correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempts += 1

if attempts == 3:
    print("Access Denied")


i = 0
while (i < 10):
    print("you are in while loop")
    i = i +1

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


for amount in range(100, 1100, 100):
    print("Amount:", amount)

for i in range(5, 0, -1):
    print(i)

for _ in range(3):
    print("Python")

for i in range(5):
    if i == 2:
        break
    print(i)


correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempts += 1
        
if attempts == 3:
    print("Access Denied")

correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempts += 1
        
if attempts == 3:
    print("Access Denied")

user_input = ""
while user_input != "exit":
    user_input = input("Type 'exit' to quit: ")
    print("You typed:", user_input)

print("Goodbye!")

server_online = False
while not server_online:
    # check server status
    server_online = check_server()  # returns True/False

    if not server_online:
        print("Server is offline. Retrying...")
        time.sleep(5)  # wait for 5 seconds before retrying

choice = ""
while choice != "quit":
    print("1. Play")
    print("2. Settings")
    print("3. Quit")
    choice = input("Choose option: ")

# Scenario 1: Even numbers
# Print all even numbers from 2 to 20 using a for loop.

for i in range(2, 20, 2):
    print(i)