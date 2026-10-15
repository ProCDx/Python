# RPS - Else and Elif Statements
# elif checks another condition, else runs when nothing above matched.

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! You lose."
    else:
        return "Some other result"

print(check_win("rock", "scissors"))
