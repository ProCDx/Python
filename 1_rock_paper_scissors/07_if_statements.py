# RPS - If Statements
# if runs a block of code only when a condition is True.

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"

result = check_win("rock", "rock")
print(result)
