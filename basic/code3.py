# Define a function to perform addition or subtraction
def calculate(num1, num2, operation):
    """
    This function performs addition or subtraction based on the operation.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('+' or '-').

    Returns:
    float: The result of the operation.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        return "Invalid operation. Please use '+' or '-'."

# Example usage
result = calculate(10, 5, '+')
print("Result:", result)

result = calculate(10, 5, '-')
print("Result:", result)

# Trying with an invalid operation
result = calculate(10, 5, '*')
print("Result:", result)
