print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=float(input("How much bill 125percentage tip would you like to give ? 10,12,15?"))
people=int(input("How many people to split bill?"))
totalbill=round((bill+(bill*(tip/100)))/people,2)
print(f"Each person should pay :{totalbill}")