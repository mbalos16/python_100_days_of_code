# Exercise 26.3. Data overlap

# Instructions: 
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.


import pandas as pd

# import list ONE and create a new int list.
with open ("day_26/exercise_26_3_data_overlap_file1.py") as file_one:
    file_one_list = file_one.readlines()
    list_one_num = [int(number) for number in file_one_list]

# import list two and create a new int list.
with open ("day_26/exercise_26_3_data_overlap_file2.py") as file_two:
    file_two_list = file_two.readlines()
    list_two_num = [int(number) for number in file_two_list]

# create a new list of numbers that are in both lists
# result = [new_item for item in list if test]
result = [num for num in list_one_num if num in list_two_num]

# Write your code above 👆
print(result)