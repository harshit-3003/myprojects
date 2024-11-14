import random
friends=["alice","Bob","Charlie","David","Emanuel"]
'''pick=random.choice(friends)'''                                  # 1st method
pick=random.randint(0,4)                                           # 2nd method

print(friends[pick])