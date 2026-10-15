# RPS - Dictionaries
# A dictionary stores key: value pairs - handy for returning several values.

def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print(choices)   # {'player': 'rock', 'computer': 'paper'}
