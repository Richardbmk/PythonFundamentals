from random import choice, randint

print("... rock ... ... paper... ....scissor...GAME:")

player1 = input("Player 1, is your turn to choose:")
player1 = player1.lower()

machine = choice(["rock", "paper", "scissor"])
print(f"The machine choose: {machine}")

if player1 == machine:
    print("It's a tie!")
elif player1 == "rock":
    if machine == "scissor":
        print("player1 you WIN!")
    elif machine == "paper":
        print("machine you WIN!")
elif player1 == "paper":
    if machine == "rock":
        print("player1 you WIN!")
    elif machine == "scissor":
        print("machine you WIN!")
elif player1 == "scissor":
    if machine == "paper":
        print("player1 you WIN!")
    elif machine == "rock":
        print("machine you WIN!")
else:
    print("Something went worng...")
