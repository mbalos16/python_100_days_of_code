# Definition of the operations
import art_exercise10_2_calculator


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary with all the operations available
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art_exercise10_2_calculator.logo)
    # Pick a first number
    num1 = float(input("What's the first number? "))
    # Show the operations available
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue == False
            calculator()


calculator()
