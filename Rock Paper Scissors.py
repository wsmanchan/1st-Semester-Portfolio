#Stacie Chan
#1/6/2025
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
tie = 0

#Function
def Rock_Paper_Scissors_game():
    global wins  #These are my global variable to track of the wins, losses, and tie
    global losses
    global tie
    print("Welcome, Let's play Rock Paper Scissors.")
    while True:   #This is to loop the game until the player does not want to play any more
        print("Please select either rock paper or scissors")
        player = input("Your Option: ") #This is the person selection
        print("You chose:", player)

#This is the computer selection
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("Computer choses Rock")
        elif computer == 2:
            computer = "paper"
            print("Computer choses Paper")
        else:
            computer = "scissors"
            print("Computer choses scissors")

        # The outcome
        if player == "rock" and computer == "rock":
            print("You tied with the computer.")
            tie += 1
        elif player == "rock" and computer == "paper":
            print("You lost to the computer.")
            losses += 1
        elif player == "rock" and computer == "scissors":
            print("You won against the computer.")
            wins += 1
        elif player == "paper" and computer == "paper":
            print("You tied with the computer.")
            tie += 1
        elif player == "paper" and computer == "rock":
            print("You won against the computer.")
            wins += 1
        elif player == "paper" and computer == "scissors":
            print("You lost to the computer.")
            losses += 1
        elif player == "scissors" and computer == "scissors":
            print("You tied with the computer.")
            tie += 1
        elif player == "scissors" and computer == "paper":
            print("You won against the computer.")
            wins += 1
        elif player == "scissors" and computer == "rock":
            print("You lost against the computer.")
            losses += 1

        print("This is how many times you win:" + str(wins)) #This print the wins, losses, and tie to the player
        print("This is how many times you lose:" + str(losses))
        print("This is how many times you tie:" + str(tie))

        # Play Again
        play = input("Would you like to play again?")
        if play == "yes":
            print("You can continue playing")
        elif play == "no":
            print("Thanks for playing.")
            break


#Main
Rock_Paper_Scissors_game()
