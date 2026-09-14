balance = 100000

def check_balance(balance):
    print(f"Balance : {balance}")

def deposit(balance):
    depo = input("How much would you like to deposit? : ")

    try:
        depo = int(depo)
    except ValueError:
        print("Failed to deposit!")
        return balance

    balance += depo
    print(f"Your balance is now {balance}")
    return balance

def withdraw(balance):
    withdraw = input("How much would you like to withdraw? : ")

    try:
        withdraw = int(withdraw)
    except ValueError:
        print("Failed to withdraw!")
        return balance

    balance -= withdraw
    print(f"Your balance is now {balance}")
    return balance

while True:
    print("""
=== ATM ===
1. Check balance
2. Deposit
3. Withdraw
4. Exit""")

    choice = input("Choice : ")

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        break

    else:
        print("Invalid action!")