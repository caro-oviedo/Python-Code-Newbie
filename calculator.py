
def add_numbers(num1, num2):
    """ Adds the numbers """

    return num1 + num2


def subtract_numbers(num1, num2):
    """ subtracts the numbers"""
    return num1-num2


def multiply_numbers(num1, numb2):
    """ Multiplies the numbers"""
    return num1 * numb2

def divide_numbers(num1, num2):
    """ Divide num1 by numb2"""
    return num1 / num2

def compute(num1, operator, num2):
    """ Computes the final result"""
    result = 0

    if operator == "+":
        result = add_numbers(num1, num2)
    elif operator == "-":
        result = subtract_numbers(num1, num2)
    elif operator == "*":
        result = multiply_numbers(num1, num2)
    else:
        result = divide_numbers(num1, num2)
    
    print(f"The final result is {result} ")


def main():
    """ top-level function. It calls the compute() function """
    first_number = float (input("Enter the first number") )
    second_number = float (input("Enter the next number") )

    user_input = input("Enter an operator (+,-,*,/): ")
    if user_input in valid_operators:
        compute(first_number, user_input, second_number)
    else:
        print("Invalid operator. Cannot compute the result")


print("=" * 25)
print("This is a simple calculator")
print("It supports the following operations: ")
print("i) Addition"
        "\nii)Subtraction"
        "\niii)Multiplication and"
        "\niv)Division")
print("=" * 25)

valid_operators = ["+", "-", "*", "/"]

main()
    
