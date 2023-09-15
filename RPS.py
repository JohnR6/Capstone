print("Welcome to Rock Paper Scissors! Let us Begin")
p1_wins = 0
p2_wins = 0
ties = 0
while(True):
    p1 = input("Player 1's pick is: ")
    p2 = input("Player 2's pick is: ")
    
    if(p1 == p2):
        print("It's a tie!")
        ties += 1
    elif((p1 == "r" and p2 == "s") or (p1 == "s" and p2 == "p") or (p1 == "p" and p2 == "r")):
        print("Player 1 wins!")
        p1_wins += 1
    else:
        print("Player 2 wins!")
        p2_wins += 2
    again = input("Would you like to play again? (y/n) ")
    if not (again == "y"):
        break