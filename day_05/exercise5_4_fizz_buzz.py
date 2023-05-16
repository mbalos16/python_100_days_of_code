# Exercise 5.4 - Fizz Buzz FizzBuzz

# Write your code below this row 👇
for number in range(1, 101):
    # We check if the number can be divided by 3 and 5. If so, we print FizzBuzz.
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")

    # We check if the number can be divided by 5. If so, we print Buzz.
    elif number % 5 == 0:
        print("Buzz")

    # We check if the number can be divided by 3. If so, we print Fizz.
    elif number % 3 == 0:
        print("Fizz")
    else:
        # If none of the previous conditions are true, we print the number.
        print(number)
