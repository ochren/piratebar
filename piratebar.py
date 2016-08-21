print('Welcome to Piratebar, you swashbuckler!\n')

import random

answers = {}

questions = {
    "strong": "Do ye like yer drinks strong?\n",
    "salty": "Do ye like it with a salty tang?\n",
    "bitter": "Are ye a lubber who likes it bitter?\n",
    "sweet": "Would ye like a bit of sweetness with yer poison?\n",
    "fruity": "Are ye one for a fruity finish?\n",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def piratebar():
    """Finds out what a pirate likes in his or her drink"""
    print("Argh! Say yes or no to pick what's in yer drink!\n")
    for key, value in questions.items():
        reply = raw_input(value).lower()
        if reply == "yes":
            answers[key] = True
        else:
            answers[key] = False
    return answers
            
def drinkulike(answers, ingredients):
    """Mixes the stuff together to create the final drink"""
    print("\nStuff in yer drink:")
    for key, value in answers.items():
        if value is True:
            print "{0}".format(ingredients[key][random.randint(0,2)])
    return
        
if __name__ == '__main__':
    piratebar()
    drinkulike(answers, ingredients)

