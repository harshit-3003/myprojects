#blackjack

import random

def black_jack():
 cards = [1,2,3,4,5,6,7,8,9,0,10,10,10,10,11]
 r=random.choice(cards)
 return r
def calculate_score(cards):
 if sum(cards)==21 and len(cards)==2:
  return 0
 if 11 in cards and sum(cards)>21:

  cards.remove(11)
  cards.append(1)
 return sum(cards)

def compare(u_score,c_score):
 if u_score==c_score:
  return "Draw"
 elif c_score==0:
  return "Lose,Opponent has blackjack"
 elif u_score==0:
  return "Win  with a blackjack"
 elif u_score>21:
  return "YOU went over.  you loose"
 elif c_score>21:
  return "opponent  went over .you win"
 elif u_score>computer_score:
  return "you win"
 else:
  return "you lose"



user_cards=[]
computer_card=[]
computer_score=-1
user_score=-1
for i in range(2):
 new_card=black_jack()
 user_cards.append(black_jack())
 computer_card.append(black_jack())
is_game_over=False
while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_card)

  print(f"YOURS CARDS :{user_cards} ")
  print(f"COMPUTERS  CARDS :{computer_card[0]}")


  if (user_score==0 or computer_score==0 or user_score>21):

   is_game_over=True
  else:
   user_should_deal=input("du u want to draw extra cards,type 'n' to pass:")
   if user_should_deal=="y":
    user_cards.append(black_jack())
   else:
    is_game_over=True
while computer_score!=0 and computer_score<17:
 computer_card.append(black_jack())
 computer_score=calculate_score(computer_card)
print(f"  YOUR  final hand :{user_cards},final score:{user_score}")
print(f"computer final hand :{computer_card},final score:{computer_score}")
print(compare(user_score,computer_score))