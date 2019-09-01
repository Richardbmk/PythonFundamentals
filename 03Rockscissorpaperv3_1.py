from random import choice, randint

print("... rock ... ... paper... ....scissor...GAME:")

player1 = input("Player 1, is your turn to choose:").lower()

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"The computer choose: {computer}")

if player1 == computer:
    print("It's a tie!")
elif player1 == "rock":
    if computer == "scissor":
        print("player1 you WIN!")
    else:
        print("computer you WIN!")
elif player1 == "paper":
    if computer == "rock":
        print("player1 you WIN!")
    else:
        print("computer you WIN!")
elif player1 == "scissor":
    if computer == "paper":
        print("player1 you WIN!")
    else:
        print("computer you WIN!")
else:
    print("please enter a valid moove...")
