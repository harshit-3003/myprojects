states=["jammu kashmir","uttar pradesh","madhya pradesh","goa","Maharashtra","Rajasthan","Uttrakhand","Punjab"]


extra_state=input("Do u want to add nore state? y for yes and n for no")
if extra_state == "y"  :

    state1=input("enter the new state")
    states.append(state1)
    print(states)
else :
    print(states)