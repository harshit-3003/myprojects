print("Welcome to the rollercoaster")
name=input("enter your name:\n")
age=int(input("Enter your age :\n"))
gender=input("male or female:\n")
height=int(input("Enter the height of the person in cm:\n"))
picture=input("do u want pictures ? type t for yes :")
cost1=5

if (height > 110):
    print("You are eligibe to ride")
    if (age<12):
        print("You are a child")
        print(f"cost for the ticket is ${cost1}.")
        if (picture=="t"):
            print("the cost is $8")
        else:
            print(f"cost for the ticket is ${cost1}.")
    
    if(age<12 and age>18):
        print("you are a teen")
        if (picture=='t'):
            print("the cost will be $10")
        else:
            print("the ticket cost $7.")
    else:
        print("You are adult.")
        if(picture=='t'):
            print("the cost will be $15")
        else:
            print("The ticket cost is $12.")
else:
    print("Sorry you are too small!")