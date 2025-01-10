#Stacie Chan
#10/17/2024
#Fantasy Name Project

#Main
print("Welcome to your fantasy name")  #This here is to welcome the player to the game.
print("Answer all the questions to find out your fantasy name")
print("Please answer the questions in lowercase")
ans = input("fairy or mermaid?") #Below is the different type of question the player may recieved based on the following answer they choose.
if ans == "fairy":
    ans = input("light or dark?")
    if ans == "dark":
        ans = input("hot or cold?")
        if ans == "hot":
             print("Your fantasy name is Alyssa.")
        else:
             print("Your fantasy name is Luna.")
    if ans == "light":
        ans = input("berry or citrus?")
        if ans == "berry":
            print("Your fantasy name is Sophie.")
        else:
            print("Your fantasy name is Claire.")
if ans == "mermaid":
    ans = input("dolphin or shark?")
    if ans == "dolphin":
        ans = input ("phone or computer?")
        if ans == "phone":
            print("Your fantasy name is Daphne.")
        else:
            print("Your fantasy name is Elena.")
    if ans == "shark":
        ans = input("vintage or modern?")
        if ans == "vintage":
            print("Your fantasy name is Kira.")
        else:
            print("Your fantasy name is Irena.")


