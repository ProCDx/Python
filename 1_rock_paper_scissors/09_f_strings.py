# RPS - f-strings
# An f-string puts variables directly inside {} in a string.

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"

print(check_win("paper", "paper"))
