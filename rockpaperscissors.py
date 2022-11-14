from random import randint
random = [ "paper" , "rock" , "scissors" ]
computer = random[ randint(0,2)]
player = False
print("rock, paper, scissors: all lowercase responses!\n")
count_player = 0
count_comp = 0
while player == False:
    player = input( "Pick your weapon :) : rock, paper, scissors: ")
    if player == computer:
        print(f"computer picked {computer}\n")
        print( "It's a tie!" )
    elif player == "rock":
        if computer == "paper":
            print(f"computer picked {computer}\n")
            print( "Computer won!" )
            count_comp+=1
        elif computer == "scissors":
            print(f"computer picked {computer}\n")
            print( "Player won!" )
            count_player+=1
    elif player == "paper":
        if computer == "rock":
            print(f"computer picked {computer}\n")
            print( "Player won!")
            count_player+=1
        elif computer == "scissors":
            print(f"computer picked {computer}\n")
            print( "Computer won!" )
            count_comp+=1
    elif player == "scissors":
        print(f"computer picked {computer}\n")
        if computer == "rock":
            print( "Computer won!" )
            count_comp+=1
        elif computer == "paper":
            print(f"computer picked {computer}\n")
            print( "Player won!")
            count_player+=1
    print( f" The score is:\n  Player/Computer: {count_player}/{count_comp}" )
    ok = input( "New round? yes/no" )
    if ok == "yes":
        player = False
    else:
        count_player = 0
        count_comp = 0
        player = True