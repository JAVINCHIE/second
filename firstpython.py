#English dictionary

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return(data[word])
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("did you mean %s instead? Enter Y if yes or N if no: " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "word doesn't exist. Double check it."
        else:
            return "we didn't understand your query."
    else:
        print("the word does not exist. please double check it")

word = input("enter word: ")

output = print(translate(word))

if type(output) == list:
    for item in ouput:
        print(item)
else:
    print(output)
