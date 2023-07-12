# Exercise 30.3. Improve the Nato Alphabet Project

import pandas as pd

logo = """
 _       __   _____  ___        __    _     ___   _      __    ___   ____ _____ 
| |\ |  / /\   | |  / / \      / /\  | |   | |_) | |_|  / /\  | |_) | |_   | |  
|_| \| /_/--\  |_|  \_\_/     /_/--\ |_|__ |_|   |_| | /_/--\ |_|_) |_|__  |_|  
"""

print(logo)
df_nato = pd.read_csv("day_30/exercise30_3_nato_alphabet_project_data.csv")
nato_dic = {row["letter"]: row["code"] for (index, row) in df_nato.iterrows()}

translation = True
while translation:
    try:
        user_word = (input("Enter a word:")).upper()
        result = [f"{letter}: {nato_dic[letter]}" for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(result)
        translation = False


# Teacher's solution
# def generate_phonetic():
#     try:
#         user_word = (input("Enter a word:")).upper()
#         result = [f"{letter}: {nato_dic[letter]}" for letter in user_word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(result)
# generate_phonetic()