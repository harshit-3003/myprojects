# comparison with followers
import random

count=0


data = [
    {'name': 'virat kohli', 'followers': 270, 'description': 'cricketer', 'country': 'india'},
    {'name': 'ms dhoni', 'followers': 50, 'description': 'cricketer', 'country': 'india'},
    {'name': 'deepika padukone', 'followers': 80, 'description': 'actress', 'country': 'india'},
    {'name': 'cristiano ronaldo', 'followers': 640, 'description': 'footballer', 'country': 'Portugal'},
    {'name': 'instagram', 'followers': 346, 'description': 'platform', 'country': 'us'},
    {'name': 'ariana grande', 'followers': 183, 'description': 'actress', 'country': 'us'},
    {'name': 'sunil chhetri', 'followers': 8, 'description': 'footballer', 'country': 'india'},
    {'name': 'Dwayne Johnson', 'followers': 181, 'description': 'actor and professional wrestler', 'country': 'us'},
    {'name': 'arijit singh', 'followers': 10, 'description': 'singer', 'country': 'india'}
]
account_b=random.choice(data)

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(user_guess,a_followers,b_followers):
    if(a_followers>b_followers):
       return user_guess=="a"
    else:
        return user_guess=="b"
game_shold_continue=True
while game_shold_continue:
    account_a = account_b

    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Compare B: {format_data(account_b)}")

    guess=input("who has more followers ?Type 'A' or 'B'").lower()
    print("\n"*40)
    a_follower_count=account_a["followers"]
    b_follower_count=account_b["followers"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        count += 1
        print(f"YOU ARE  RIGHT!{count}")

    else:
        print(f"SORRY!{count}")
        exit()
