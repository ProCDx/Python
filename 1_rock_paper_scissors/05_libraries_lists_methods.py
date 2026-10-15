# RPS - Libraries, Lists, Methods
# import brings in a library. A list holds an ordered collection.
# random.choice() is a function from the random library that picks one item.

import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]          # a list
    computer_choice = random.choice(options)        # library function
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

print(get_choices())

# Lists also have methods (functions attached to an object):
food = ["pizza", "carrots", "eggs"]
food.append("bread")
print(food)
