sc_num = 7

def check_guess(guess):
    guess = int(guess)

    if guess > sc_num:
        print("Too high!")
        return True
    elif guess < sc_num:
        print("Too Low!")
        return True
    else:
        print(f"Correct! It is {sc_num}")
        return False

while True:
    print("I'm thinking of a number from 1-10")
    guess = input("Guess : ")   

    check = check_guess(guess)

    if not check:
        break