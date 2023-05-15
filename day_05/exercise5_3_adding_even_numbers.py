# Exercise 5.3 - Adding even numbers

# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.


# Write your code below this row 👇
sum_of_even = 0
for even in range(1, 101):
    # We check if the number in the range is even or not by checking if the division by 2 rests 0.
    if int(even) % 2 == 0:
        # If the division by 2 of the number gives us 0, the number is added to the sum.
        sum_of_even += even
# We print the result
print(sum_of_even)
