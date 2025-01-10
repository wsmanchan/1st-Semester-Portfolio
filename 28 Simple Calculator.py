#Stacie Chan
#28 Simple Calculator
#11/19/2024

#Init
#Functions
#Add num1 w/ num2 and print the result
def add(num1,num2):
    result = num1 + num2 #One solution
    print("The result is: " + str(result))

def sub(num1,num2):
    result = num1 - num2
    print("The result is: " +str(result))

def multi(num1,num2):
    result = num1 * num2
    print("The result is: " +str(result))

def divi(num1,num2):
    result = num1 / num2
    print("The result is: " +str(result))

def simple_calculator():
    print("Welcome to Simple Calculator")
    while True:
        print("Select an operation: ")
        print("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")

        option= int(input("(1-5) Select option: ")) #This is collecting a integar
        if option == 1:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            add(int(int1),int(int2))

        if option == 2:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            sub(int(int1), int(int2))

        if option == 3:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            multi(int(int1),int(int2))

        if option == 4:
            int1 = input("Enter first number: ")
            int2 = input("Enter second number: ")
            divi(int(int1,),int(int2))

        if option == 5:
            break


#Main
simple_calculator()
