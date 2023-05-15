# Exercise 5.1 - Rock Paper Scissors

# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g. :180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# print(student_heights)
# print(type(student_heights))
count = 0
count_age = 0
for age in student_heights:
    # Count how many times the for loop pases through the list
    count += student_heights.count(age)
    count_age = count_age + age

# Divide the sum of ages between the count of how many elements we have in the list
average_age = round(count_age / count)
print(average_age)
