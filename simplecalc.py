#Sadie Levitt
#simple calculator

#init
#function
def add (num1,num2):
    result = num1 + num2
    print ("The result is: " + str(result))
#main
print ("Welcome to simple calculator")
print ("Select an operation: ")
print ("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit """)
option = input ("(1-5) Select option: ")
if option == 1:
    int1= input("Enter first number: ")
    int2 = input("Enter second number: ")
    add (int1, int2)


