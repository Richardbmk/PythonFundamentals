from random import choice, randint
player_wins = 0
computer_wins = 0
winning_score = int(input("How many times you wanna play? "))

while player_wins < winning_score and computer_wins < winning_score:
    print("... rock ... ... paper... ....scissor...GAME:")
    print(f"Player Score: {player_wins} computer Score: {computer_wins}")

    player = input("Player 1, is your turn to choose: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer choose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissor":
            print("player you WIN!")
            player_wins += 1
        else:
            print("computer WIN!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player you WIN!")
            player_wins += 1
        else:
            print("computer WIN!")
            computer_wins += 1
    elif player == "scissor":
        if computer == "paper":
            print("player you WIN!")
            player_wins += 1
        else:
            print("computer WIN!")
            player_wins += 1
    else:
        print("please enter a valid moove...")
print(f"FINAL SCORES... Player:{player_wins} computer...{computer_wins}")

if player_wins > computer_wins:
    print("CONGRATS, YOU WIN! :-)")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO :( THE COMPUTER WON...")

# to style you code in python use:
# autopep8 --in-place ugly_code.py
