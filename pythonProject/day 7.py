import random
word_list=["animal","bird","bat","dog","reptile"]
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
for position in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
correct_latter=[]

gameover=False

while not gameover:
    guess=input("Enter your Guess :").lower()
    display=""
    for latter in chosen_word:
        if latter ==guess:
            display+=latter
            correct_latter.append(guess)
        elif latter in correct_latter:
            display+=latter
        else:
            display+="_"
    print(display)
    if "-" not in display:
        gameover=True

        print("You win")
import random
word_list=["animal","bird","bat","dog","reptile"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
placeholder=""
for position in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
correct_latter=[]

gameover=False

while not gameover:
    guess=input("Enter your Guess :").lower()
    display=""
    for latter in chosen_word:
        if latter == guess:
            display += latter
            correct_latter.append(guess)
        elif latter in correct_latter:
            display+=latter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            gameover=True
            print("You Lose.")
            
        
    if "-" in display:
            gameover=True
            print("You win")


