import json
from difflib import get_close_matches

# Loading the JSON file.
data = json.load(open('data.json'))


# Returning the definition of the Word
def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input('Did you mean %s instead? if yes, press \'Y\' else \'N\' for no.: ' % get_close_matches(word, data.keys())[0])
        if choice == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == 'N':
            return 'The word doesn\'t exist. please double check it.!'
        else:
            return 'We didn\'t understand your entry.'
    else:
        return 'The word doesn\'t exist. please double check it.!'


# Taking input from the user
input_word = input('Enter a Word: ')
# printing the definition
output = definition(input_word)
# checking, if output type is list, then only it will iterate else print the O/P
if type(output) == list:
    for meaning in output:
        print(meaning)
else:
    print(output)
