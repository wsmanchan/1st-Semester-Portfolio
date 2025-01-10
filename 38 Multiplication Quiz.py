#Stacie Chan
#1/8/2025
#38 Multiplication Quiz

#Init
import random

quiz = 0                           #All the global variables start from 0
Correct = 0
Incorrect = 0
total_quiz = 0
#Function
def multiplication_quiz():
    global quiz                    #This is global variables
    global Correct
    global Incorrect
    global total_quiz
    print("Welcome to the Multiplication Quiz.")
    while True:                     # This is to loop the quiz if the player want to play again
        total_quiz = total_quiz + 5 # This part is to loop the whole quiz by 5 if the player wishes to play again.
        for i in range(5):          #This give out five questions at a time
            quiz = quiz + 1
            print("Question " + str(quiz) +  " of " + str(total_quiz)+ " : ")
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            computer = num1 * num2          #This part is where the computer solve the number before hand
            print("What is " + str(num1) + " * " + str(num2) + "?")
            person_answer= int(input("Your answer is: "))  #This is where the person add the number
            if person_answer == computer:
                print("Correct")
                Correct = Correct + 1     #This here is to add a number to keep track of how many is correct
            else:
                print("Incorrect")
                Incorrect = Incorrect + 1 #This here is to add a number to keep track

        print("You got " + str(Correct)+ " out of " + str(quiz) + " questions correct!")

        play = input("Would you like to play again? ")  #This part is to ask if the player want to play again
        if play.lower == "yes" :                           #If yes it would automatically loop itself
            print("You can continue playing.")
        if play.lower == "no" :
            print("Thank you for playing.")
            break                                           #If no it will stop looping itself







#Main
multiplication_quiz()
