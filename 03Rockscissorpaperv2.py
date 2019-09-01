print("... rock ... ... paper... ....scissor...GAME:")


player1 = input("Player 1, is your turn to choose:")
print("***NO CHEATING!****\n" * 20)
player2 = input("Player 2, is your turn to choose:")


if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissor":
        print("player1 you WIN!")
    elif player2 == "paper":
        print("player2 you WIN!")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 you WIN!")
    elif player2 == "scissor":
        print("player2 you WIN!")
elif player1 == "scissor":
    if player2 == "paper":
        print("player1 you WIN!")
    elif player2 == "rock":
        print("player2 you WIN!")
else:
    print("Something went worng...")
