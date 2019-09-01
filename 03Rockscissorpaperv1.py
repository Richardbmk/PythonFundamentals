print("... rock ... ... paper... ....scissor...GAME:")


player1 = input("Player 1, is your turn to choose:")
player2 = input("Player 2, is your turn to choose:")

if player1 == "rock" and player2 == "scissor":
    print("player1 you WIN!")
elif player1 == "paper" and player2 == "rock":
    print("player1 you WIN!")
elif player1 == "scissor" and player2 == "paper":
    print("player1 you WIN!")
elif player2 == "rock" and player1 == "scissor":
    print("player2 you WIN!")
elif player2 == "paper" and player1 == "rock":
    print("player2 you WIN!")
elif player2 == "scissor" and player1 == "paper":
    print("player2 you WIN!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went worng...")
