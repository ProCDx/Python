# RPS - User Input
# input() pauses the program and returns what the user typed (as a string).

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

print(get_choices())
