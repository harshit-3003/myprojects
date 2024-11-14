age=int(input("enter your age :"))
if(age>18):
    print("yes")
else:
    print("no")


a1=int(input("enter no.1 :"))
a2=int(input("enter your age 2 :"))
a3=int(input("enter your age  3:"))
a4=int(input("enter your age 4 :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("first no, is greater")
elif(a2>a1 and a2>a3 and a2>a4):
    print("second no. is greater")
elif(a3>a1 and a3>a2 and a3>a4):
    print("third no is greater")
elif(a1==a2==a3):
    print("all are equal")
else:
    print("fourth no. is greater")




