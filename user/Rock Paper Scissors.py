#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to false
player = False

    1 player = input ("Rock, Psper, Scissors")
        if player == computer:
            print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
                print("You lose!", computer, "cut", player)
        else:
                print("You win!", player, "covers", compuer)
    elif player == "Scissors":
        if computer == "Rock":
                    print("You lose...", computer, "smashes" player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a vaild play. Check your spelling!")
    #players was set to Ture, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
                    
