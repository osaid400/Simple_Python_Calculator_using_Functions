
# Calculator using Functions:

def add (a , b):
    return (a + b)

def subtract (a , b):
    return (a - b)

def multiply (a , b):
    return (a * b)

def divide (a , b):
    return (a / b)    

def power (a , b):
    return (a ** b)    

while True:
    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("0. Exit")

    try:
        operation = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input! Please enter a number from 0 to 5.")
        continue

    if operation == 0:
        print("Calculator closed. Goodbye!")
        break

    if operation < 0 or operation > 5:
        print("Invalid operator! Please choose a number from 0 to 5.")
        continue

    try:
        a = float(input("Enter your 1st Number: "))
        b = int(input("Enter your 2nd Number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if operation == 1:
        print(f"Result: {a} + {b} = {add(a, b)}")

    elif operation == 2:
        print(f"Result: {a} - {b} = {subtract(a, b)}")

    elif operation == 3:
        print(f"Result: {a} * {b} = {multiply(a, b)}")

    elif operation == 4:
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {a} / {b} = {divide(a, b)}")

    elif operation == 5:
        print(f"Result: {a} ** {b} = {power(a, b)}")






