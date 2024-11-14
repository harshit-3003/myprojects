# calculator
def addi(a,b):
    print(a+b)
def subsa(a,b):
    print(a-b)
def subsb(a,b):
    print(b-a)
def mult(a,b):
    print(a*b)
def diva(a,b):
    print(a/b)
def divb(b,a):
    print(b/a)
def calulation(a):
    b = int(input("enter second number"))
    x = a
    cal = input("enter the operation u want to perform")
    if (cal == "addition"):
        x = addi(a, b)
    if (a > b):
        if (cal == "substraction"):
            x = subsa(a, b)
        if (cal == "Division"):
            x = diva(a, b)
    if (b > a):
        if (cal == "substraction"):
            x = subsb(a, b)
        if (cal == "Division"):
            x = divb(b, a)
    if (cal == "multiplication"):
        x = mult(a, b)
x = 0
a = int(input("enter First Number"))

num=True
while(num==True):
    b = int(input("enter second number"))
    x=a
    cal=input("enter the operation u want to perform")
    if (cal == "addition"):
        x=addi(a,b)
    if (a>b):
        if (cal == "substraction"):
            x=subsa(a,b)
        if (cal == "Division"):
            x=diva(a,b)
    if (b>a):
        if (cal == "substraction"):
            x=subsb(a,b)
        if (cal == "Division"):
            x=divb(b,a)
    if (cal == "multiplication"):
        x=mult(a,b)
    proceesing = input("do u want to proced with x")
    if (proceesing == "yes"):
        num=True

    elif (proceesing == "no"):
        num=False
        a = int(input("enter First Number"))
        calulation(a)


    else:
        exit()


x=0
a=int(input("enter First Number"))
calculation(a)

