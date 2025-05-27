#Stacie Chan
#1/28/2025
#44 Slot Machine

#Init
import random
import time
credit = 100
symbols = ["♠", "♡", "7"]

#Functions
def slot_machine():
    global credit
    print("Welcome to the 3-slot machine.")         #This part is to greet the user into the slot machine
    while True:
        print("You currently have this many credits: " + str(credit))
        print("Each spin is 10 credits.")
        try:
            question = input("Press 's' to spin or 'q' to quit: ")  #This part is to ask if the user wishes to paly the slot machine
            if question =="s" and credit >= 10:
                credit = credit - 10
                print("spinning...")
                time.sleep(4)                                       #This part is to pretend to wait for the slot machine to spin
                slot1 = random.choice(symbols)
                slot2 = random.choice(symbols)
                slot3 = random.choice (symbols)
                print(slot1)                                        #This here is to print the symbols of the slot machine that randomly choosen
                print(slot2)
                print(slot3)

                if slot1 == slot2 == slot3 == "7":                       #This part is part is to check if the slot machine rolled a jackpot
                    print("Congratulations you win the Jackpot!")
                    credit = credit + 50
                    print("+50 credit")
                elif slot1 == slot2 == slot3:                       #This part is to see if the user won by getting three of the same symbols
                    print("Congratulations you win.")
                    credit = credit + 20
                    print("+20 credit")

                else:                                               #This here to say the user losts by not winning
                    print("Sorry but you lost.")


            if question == "q" or credit < 10:                                     #This part is to allow the user to stop playing the slot machine if they wish to stop
                print("Thank you for playing!")
                break
        except:                                                     #This part is to make sure the user are not entering the wrong choice when wanting to stop or play
            print("Please enter 's' or 'q' to signify if you want to spin or quit.")
#Main

slot_machine()

