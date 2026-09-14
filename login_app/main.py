users = {
    "ken": "python123",
    "alex": "banana",
    "bob": "qwerty"
}

def check_login(usrname):
    usrname = usrname.lower()

    if usrname in users:
        password = input("Password : ")

        if password == users[usrname]:
            print(f"Login sucessful!")
            return False
        
        print("Wrong password!")
        return False
    else:
        print(f"User not found")
        return True

while True:
    usrname = input("Username : ")

    login = check_login(usrname)
    if not login:
        break
