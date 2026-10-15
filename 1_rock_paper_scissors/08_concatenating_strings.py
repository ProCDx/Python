# RPS - Concatenating Strings
# + joins strings together.

def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"

print(check_win("rock", "rock"))
