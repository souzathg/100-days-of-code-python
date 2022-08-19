from art import *

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "You can't divide a number by 0."

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation]
        answer = round(function(num1, num2), 3)

        print(f"{num1} {operation} {num2} = {answer}")

        question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")

        if question == 'y':
            num1 = answer
        elif question == 'n':
            calculator()
        else:
            should_continue = False


calculator()
