

import pandas as pd


#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index,row) in nato.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

words = input("Enter a word:").upper()
result = [nato_alphabet[letter] for letter in words]
print(result)