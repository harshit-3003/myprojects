'''print(3 * (3 + 3) // 3 - 3 )
score=0
score+=5   #assignment
height=108
is_winning=True
print(f"Your score is ={score},Your height is= {height},you are winning is={is_winning}")   #f strimg






def myfunction(a,b):
    s=a+b
    return s

myfunction(5,4)'''
'''x=int(input())
if (x<3):
    print("gold")
elif(x==3 or x<6):
    print("silver")
else:
    print("Bronze")'''
'''t=int(input(""))
for i in range(t):
    x=int(input())
    if ((x//30)==0):
        print("no")
    else:
        print("yes")'''
'''t=int(input(""))
for i in range(t):
    x,y=map(int,input().split())
    if (y>x):
        
        z=x*3
        print(z)
    else:
        print("0")
    '''
    
'''t=int(input(""))
for i in range(t):
    x=list(map(int,input()).split())
    print(x.max())
    '''
'''t=int(input(""))
for i in range(t):
    x=list(map(int,input().split()))
    x.sort()
    max_value=max(x)
    if(max_value==x[0]):
        print("Alice ")
    elif(max_value==x[1]):
        print(" Bob")
    elif(max_value==x[2]):
        print("Charlie")
    '''
# cook your dish here

'''x,y=input().split()
x=float(x)
y=float(y)
if(x%5==0 and y-x>=0.5):
    amount=y-(x+0.5)
print(amount)
'''
'''t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    profit=((x*10)/100)+x
    print(profit)
    loss=x-y
    print(loss)
    total=profit-loss
    print(total)'''
'''t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x<=2*y):
        print("yes")
    else:
        print("no")
        '''
