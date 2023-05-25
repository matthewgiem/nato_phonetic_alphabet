import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

alternative_nato_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("what word would you like translated? ")
return_list = []
for x in word:
    if x != " ":
        return_list.append(alternative_nato_dictionary[x.upper()])

print(return_list)
