#coffee machine

MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":150,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "cost":250,
    },
    "cappuccino":{
        "ingredients":{
            "water":50,
            "milk":100,
            "coffee":18,
        },
        "cost":300,
    },
}
resource={
    "water":300,
    "milk":200,
    "coffee":100,
}
profit=0
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>=resource[item]:
            print(f"Sorry  there is  not  enough {item}")
            return False
        return True
def make_coffee(drink_name,order_ingredient):
    for item in order_ingredient:
        resource[item] -= order_ingredient[item]
    print(f"here is your coffee{drink_name}")
def process_coins():
    print("Please insert coins")
    total=int(input("how many 10 notes? :"))*10
    total += int(input("how many 50 notes? :"))*50
    total += int(input("how many 100 notes? :"))*100
    total += int(input("how many 200 notes? :"))*200
    return total
def is_transactions_successful(money_received,drink_cost):
    global profit
    if money_received>=drink_cost:
        change = round(money_received-drink_cost ,2)
        print(f" here is your  change{change}")
        profit += drink_cost
        return True
    else:
        print("sorry insufficient money")
        return False


is_on=True
while True:
    user=input("what would u like to have sir :(e for espresso,l for latte,c for cappuccino,r for report)")
    if user=="off":
        is_on=False
    elif user=="report":
        print(f"water:{resource['water']}ml")
        print(f"Milk:{resource['milk']}ml")
        print(f"coffee:{resource['coffee']}ml")
        print(f"Money: ruppees{profit}")
    else:
        drink = MENU[user]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transactions_successful(payment,drink["cost"]):
                make_coffee(user,drink["ingredients"])
