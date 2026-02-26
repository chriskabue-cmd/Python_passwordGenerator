#These libs helps with file handling,security
import random 
import string 
import hashlib 
import getpass 
import os 

users_file = "users.txt"
generated_file = "generated_passwords.txt"
#simple storage using text files

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
#converts password into a secure hash

def register():
    print("\nRegister Here")

    user = input("Create username: ")
    pw = getpass.getpass("Create password: ")

    if not os.path.exists(users_file):
        open(users_file, "w").close()

    f = open(users_file, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        u = line.split(",")[0]
        if u == user:
            print("Username already taken.\n")
            return

    hashed = hash_password(pw)

    f = open(users_file, "a")
    f.write(user + "," + hashed + "\n")
    f.close()

    print("Registration successful!\n")


def login():
    print("\nLogin")

    tries = 3

    while tries > 0:
        user = input("Username: ")
        pw = getpass.getpass("Password: ")

        if not os.path.exists(users_file):
            print("No users registered yet.\n")
            return None

        hashed = hash_password(pw)

        f = open(users_file, "r")
        lines = f.readlines()
        f.close()

        found = False

        for line in lines:
            u, p = line.strip().split(",")
            if u == user and p == hashed:
                found = True
                break

        if found:
            print("Login successful. Welcome", user, "\n")
            return user
        else:
            tries -= 1
            print("Wrong details. Attempts left:", tries)

    print("Too many failed attempts.\n")
    return None


def generate(user):
    print("Generate Password")

    try:
        length = int(input("Length: "))
    except:
        print("Invalid length\n")
        return

    chars = ""

    if input("Uppercase? y/n: ") == "y":
        chars += string.ascii_uppercase
    if input("Lowercase? y/n: ") == "y":
        chars += string.ascii_lowercase
    if input("Numbers? y/n: ") == "y":
        chars += string.digits
    if input("Symbols? y/n: ") == "y":
        chars += string.punctuation

    if chars == "":
        print("You didn’t choose anything.\n")
        return

    password = ""
    for i in range(length):
        password += random.choice(chars)

    print("Your password is:", password)

    if len(password) >= 12:
        print("This looks like a strong password.")
    else:
        print("Try a longer password for better security.")

    if input("Save password? y/n: ") == "y":
        f = open(generated_file, "a")
        f.write(user + ":" + password + "\n")
        f.close()
        print("Saved.\n")


def menu():
    while True:
        print("\nPassword System")
        print("1.Register")
        print("2.Login")
        print("3.Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            u = login()
            if u:
                generate(u)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice\n")


menu()