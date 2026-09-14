inventory = {
    "apple": 5,
    "banana": 3,
    "orange": 0
}

def check_inventory():
    for item in inventory:
        print(f"{item}: {inventory[item]}")   

def add_item():
    add = input("What do you want to add? : ")
    quantity = input("How much do you want to add? : ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Not a valid number!")
        return

    if add not in inventory:
        print(f"Added {quantity} new {add}")
        inventory[add] = quantity
    else:
        print(f"Added {quantity} to {add}")
        inventory[add] += quantity

def remove_item():
    remove = input("What do you want to remove? : ")
    quantity = input("How much do you want to remove? : ")
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Not a valid number!")
        return

    if remove not in inventory:
        print(f"There is no {remove} in inventory!")
    else:
        if quantity > inventory[remove]:
            print(f"You don't have that much {remove}")
            return
        inventory[remove] -= quantity
        print(f"Removed {quantity} {remove}!")

while True:
    print("""== INVENTORY ===
1. Check inventory
2. Add item
3. Remove item
4. Exit""")

    choice = input("Choice : ")

    if choice == "1":
        check_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        break

    else:
        print("Invalid action!")