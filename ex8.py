a = True
while a == True:
    p1_input = input("P1: rock, paper or scissors?\n>> ")
    p2_input = input("P2: rock, paper or scissors?\n>> ")
    if p1_input == "rock":
        if p2_input == "rock":
            print("Two rocks and no roll! It's a tie!")
        elif p2_input == "paper":
            print("Paper beats rock, P2 wins!")
        elif p2_input == "scissors":
            print("Rock smashes scissors, P1 wins!")
        else:
            print("Looks like P2 was trying to play a different game.")
    elif p1_input == "paper":
        if p2_input == "rock":
            print("Paper beats rock, P1 wins!")
        elif p2_input == "paper":
            print("Two paper cuts! It's a tie!")
        elif p2_input == "scissors":
            print("Scissors cuts paper, P2 wins!")
        else:
            print("Looks like P2 was trying to play a different game.")
    elif p1_input == "scissors":
        if p2_input == "rock":
            print("Rock smashes scissors, P2 wins!")
        elif p2_input == "paper":
            print("Scissors cuts paper, P1 wins!")
        elif p2_input == "scissors":
            print("Metals clank, it's a tie!")
        else:
            print("Looks like P2 was trying to play a different game.")
    else:
        print("That was an exclusive 'or,' only enter rock, paper, or scissors!")

    b = True
    while b == True:
        again = input("Do you want to play again [y/n]?\n>> ")
        if again == "y":
            b = False
            a = True
        elif again == "n":
            a = False
            b = False
        else:
            print("Try answering that again with a letter 'y' or the letter 'n' instead of what was typed. :D")
