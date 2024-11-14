'''def greet_with_name(name):
    if (region == 1):
        print("namaste",name)
    elif(region == 2):
        print("hello",name)
    else:
        print("not in the list")
name=input("enter your name :")

region=int(input("enter your country(1 for india and 2 for england):"))
greet_with_name(name)
def life_in_weeks(age):
    a=(90-age)*52
    print(f"You Have {a} weeks left")
life_in_weeks(12)'''
#### for two parameters
'''def greet_with_name(name,location):
    if (location == "india"):
        print(f"namste {name} from {location}")
    elif(location == "england"):
        print(f"       hello {name} from {location}      ")
    else:
        print("not in the list")
name=input("enter your name :")
location = input("enter your country:").lower()
greet_with_name(name,location)
greet_with_name(name="vaibhav",location="india").count()
count +=1'''

    

        
        
    
def calculate_love_score(name1,name2):
    name3=name1+name2
    lower_name3=name3.lower()
    t=lower_name3.count("t")
    r=lower_name3.count("r")
    u=lower_name3.count("u")
    e=lower_name3.count("e")
    l=lower_name3.count("l")
    o=lower_name3.count("o")
    v=lower_name3.count("v")
    print(int(str(t+r+u+e)+str(l+o+v+e)))
calculate_love_score(name1="Kanye West",name2="Kim Kardashian")