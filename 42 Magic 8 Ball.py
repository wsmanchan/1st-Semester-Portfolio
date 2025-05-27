#Stacie Chan
#1/24/2025
#Magic 8 Ball


#Initizile
import random
import time
magic_list= ["yes", "no" , "maybe", "definitely yes", "definitely no" , "Absolutly yes!" , "Absolutly no!", "mostly no" , "mostly yes", "probability yes" , "probabily no", "perhaps", " likely yes", "likely no", "perchance"]

#Functions
def magic_ball():
    print("Welcome to the Magic 8 ball!")
    while True:
        try:
            question = input("please enter your question here: ")
            if "?" in question:
                print("shake...")
                time.sleep(2)
                print("shake....")
                time.sleep(2)
                print("shake.....")
                time.sleep(2)

                print(random.choice(magic_list))
                print("Would you like to use the magic 8 ball again?")
                repeat = input("Please enter yes or no: ")
                if repeat == "no":
                    print("Thank you for using this magic 8 ball.")
                    break
                else:
                    continue

        except:
            print("Please enter a question")
#Main
magic_ball()
