import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("what word would you like translated? ")
return_list = [nato_dictionary[x.upper()] for x in word if x != " "]
print(return_list)
