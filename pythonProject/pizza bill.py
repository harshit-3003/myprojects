print("Welcome to the PIzza Deliverry")
size=input("What size do u like to have? S,M,L:")
pepperoni=input("do u want pepperoni on your pizza ? y for yes :")
extra_cheese=input("do u want extra cheese? y or n:")
small=15
medium=20
large=25
"""if (size=="S"):
    if(pepperoni=="y"):
        if(extra_cheese=="y"):
            print(f"the cost for ur pizza will be :{15+2+1}")
        print(f"the cost of the pizza will be :${15+2}")
    else:
        print("the cost for ur pizza will be :$15")




if(size=="M"):
    if(pepperoni=="y"):
        if(extra_cheese=="y"):
            print(f"the cost for ur pizza will be :{20+3+1}")
        else:
            print(f"the prise of the pizza will be:${20+3}")
    else:
        print("the cost for ur pizza will be :$20")
if(size=="L"):
    if(pepperoni=="y"):
        if(extra_cheese=="y"):
            print(f"the cost for ur pizza will be :{25+3+1}")
        else:
            print(f"the prise of the pizza will be:${25+3}")
        print(f"the cost of the pizza will be :${25+3}")
    else:
        print("the cost for ur pizza will be :$25")"""
    
bill=0
if size=="S":
    bill+=15
if size=="M":
    bill+=20
if size=="L":
    bill+=25
else:
    print("you are wrong")
if pepperoni=="y":
    if size=="S":
        bill += 2
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"your total cost for the pizza is =${bill}")


