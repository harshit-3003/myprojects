import random
person=input("what do you choose ? 0 for rock,1 for papper,2 for scissor:\n")
computer=random.randint(0,2)
if person=="0":
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
    if computer==0:
         
         print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
         print("Draw\n")
         

    if computer==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("you lost\n")
    if computer==2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("you won\n")
    
if person=="1":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
    if computer==0:
          print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
          print("you Won")
    if computer==1:
          print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
          print("Draw")
    if computer==2:
         print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
         print("You loose")
if person=="2":
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer==0:
       print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
       print("you loose")
    if computer==1:
     print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")       
     print("You won")   
    if computer==2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Draw")
         
         
    