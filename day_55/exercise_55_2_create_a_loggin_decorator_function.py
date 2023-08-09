# Exercise 55.2. Create a loggin decorator function
# Create the logging_decorator() function 👇


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(
            f"You called {function.__name__} function: {args[0]}, {args[1]}, {args[2]}"
        )
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def multiply(first_number, second_number, third_number):
    return first_number * second_number * third_number


multiply(1, 2, 3)
