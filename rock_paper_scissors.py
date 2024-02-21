from random import randint

t = ["Rock", "Paper", "Scissors"]

comp_choice = t[randint(0,2)]

player_choice = 1
computer_win = 0
player_win = 0

while player_choice == 1:
    player_choice = input("Chose Rock, Paper, Scissors?")
    comp_choice = t[randint(0,2)]
    if player_choice == comp_choice:
        print("Tie!")
        print("Score")
        print("Computer win:", computer_win)
        print("player win:", player_win)

    elif player_choice == "Rock":
        if comp_choice == "Paper":
            print("You lose! Computer chose", comp_choice, "player chose", player_choice)
            computer_win += 1
            print("Score")
            print("computer win:" , computer_win)
            print("player win:", player_win)

        else:
            print("You win! player chose", player_choice, "computer chose", comp_choice)
            player_win +=1
            print("Score")
            print("computer win:", computer_win)
            print("player win:",player_win)
        
    elif player_choice == "Paper":
        if comp_choice == "Scissors":
            print("You lose! Computer chose", comp_choice, "player chose", player_choice)
            computer_win += 1
            print("Score")
            print("computer win:" , computer_win)
            print("player win:", player_win)

        else:
            print("You win! player chose", player_choice, "computer chose", comp_choice)
            player_win +=1
            print("Score")
            print("computer win:", computer_win)
            print("player win:",player_win)

    elif player_choice == "Scissors":
        if comp_choice == "Rock":
            print("You lose! Computer chose", comp_choice, "player chose", player_choice)
            computer_win += 1
            print("Score")
            print("computer win:" , computer_win)
            print("player win:", player_win)

        else:
            print("You win! player chose", player_choice, "computer chose", comp_choice)
            player_win +=1
            print("Score")
            print("computer win:", computer_win)
            print("player win:",player_win)
    else:
        print("Tha's not a valid play. Check your spelling!")