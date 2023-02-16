# Define a function to perform calculations
def calculate(operation, x, y):
    # Use a dictionary to map the choice to the corresponding operation
    operations = {
        "add": lambda x, y: x + y, # Add
        "sub": lambda x, y: x - y, # Subtract
        "multiply": lambda x, y: x * y, # Multiply
        "division": lambda x, y: x / y, # Divide
    }
    # Check if the choice is valid
    if operation in operations:
        # Perform the calculation and return the result
        return operations[operation](x, y)
    else:
        # Return an error message
        return "Invalid choice"


if __name__ == "__main__":
    # Ask the user to choose an operation
    print("Choose an operation:")
    print("add. Add")
    print("sub. Subtract")
    print("multiply. Multiply")
    print("division. Divide")

    # Get the user's choice
    choice = input("Enter your choice, add sub multiply division: ")

    # Get the user's numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Call the calculate function and print the result
    print(num1, choice, num2, "=", calculate(choice, num1, num2))
