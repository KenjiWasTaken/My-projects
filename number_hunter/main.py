numbers = [4, 7, 2, 9, 1, 5]

def check_answer(answer):
    convert = int(answer)

    if convert in numbers:
        print(f"Found! {convert}")
        return True
    else:
        print("Not Found!")
        return False

while True:
    answer = input("Guess a number: ")
    result = check_answer(answer)

    if result:
        break