import random

def randomize():
    number = random.randint(1, 100)
    return number

sc_num = randomize()
attempts = 0

def check_guess(guess):
    global sc_num
    global attempts
    try:
        guess = int(guess)
    except ValueError:
        print("Not a valid number!")
        return False

    if guess > 100 or guess < 1:
        print("Please enter a number from 1-100!")
        return False
    attempts += 1

    if guess > sc_num:
        print("Too high!")
        return False
    elif guess < sc_num:
        print("Too low")
        return False
    else:
        print(f"Correct! It was {sc_num}")
        print(f"You guessed {attempts} times")
        return True

def guess():

    guess = input("Guess : ")

    if check_guess(guess):
        return True
    

while True:
    print(f"# attempts: {attempts}")
    print("I'm thinking of a number from 1-100")

    if guess():
        break