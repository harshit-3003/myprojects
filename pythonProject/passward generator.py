import random
latters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1','2','3','4','5','6','7','8','9','0']

symbol=['~','!','@','$','%','&','(',',)','_','-','+,','=','/']

print("welcome to PyPassward Generator!")
nr_latter=int(input("How many Latters you want in your passward\n"))
nr_numbers=int(input("How many Number you want in your passward\n"))
nr_symbol=int(input("How many symbol you want in your passward\n"))

# Easy Way
passward=""
for char  in range(1,nr_latter+1):
    randomp=random.choice(latters)
    passward=passward+randomp
for int in range(1,nr_numbers+1):
    passward=passward+random.choice(numbers)
for int in range(1,nr_symbol+1):
    passward=passward+random.choice(symbol)
print(passward)

# HARD Way
passward_list=[]
for char  in range(1,nr_latter+1):
    randomp=random.choice(latters)
    passward_list.append(randomp)
for int in range(1,nr_numbers+1):
    passward_list.append(random.choice(numbers))
for int in range(1,nr_symbol+1):
    passward_list.append(random.choice(symbol))
random.shuffle(passward_list)
passward=""
for char in passward_list:
    passward+=char
print(f"Your Passward could be:{passward}")