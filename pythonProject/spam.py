p1 = "make a lot of monney"
p2 = "by now"
p3 ="subscribe this"
p4 = "click this"

message=input("enter your string :")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("its a scam")
else:
    print("not a spam")