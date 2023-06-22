# Exercise 26.6. Nato Alphabet Project

# Instructions:
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f: (temp_c * 9/5) + 32 = temp_f

import pandas as pd

logo = """
Welcome to the:
 _       __   _____  ___        __    _     ___   _      __    ___   ____ _____ 
| |\ |  / /\   | |  / / \      / /\  | |   | |_) | |_|  / /\  | |_) | |_   | |  
|_| \| /_/--\  |_|  \_\_/     /_/--\ |_|__ |_|   |_| | /_/--\ |_|_) |_|__  |_|  

"""

print(logo)
df_nato = pd.read_csv("day_26/exercise_26_6_nato_alphabet_project_data.csv")

# Create a dictionary in pandas comprehension dictionary with the letter as a key, and the code as a value.
nato_dic = {row["letter"]: row["code"] for (index, row) in df_nato.iterrows()}

# Create a list of phonetic code words from a word that the user inputs.
user_word = (input("Enter a word:")).upper()

result = [f"{letter}: {nato_dic[letter]}" for letter in user_word]

print(result)
