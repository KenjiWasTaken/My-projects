inventory = {
    "apple": 5,
    "banana": 2,
    "orange": 0
}

def check_available(fruit):
    fruit = fruit.lower()

    if fruit in inventory:
        if inventory[fruit] > 0:
            print(f"We have {inventory[fruit]} {fruit}")
        else:
            print(f"Sorry, we are out of {fruit}")
    else:
        print("We don't have that")

while True:
    ask = input("Enter Fruit : ")

    result = check_available(ask)
