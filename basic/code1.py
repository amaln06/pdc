# Basic calculator for addition and subtraction

def calculator():
    print("Simple Calculator for Addition and Subtraction")
    print("Enter two numbers and choose an operation (+ or -)")

    try:
        # Taking user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Taking user input for operation
        operation = input("Enter the operation (+ or -): ")

        # Performing the calculation based on the operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        else:
            print("Invalid operation. Please enter + or -.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the calculator function
calculator()
